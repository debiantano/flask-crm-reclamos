# MODULOS DE PYTHON USADOS
from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_mysqldb import MySQL
from datetime import datetime
import vonage, requests

# PATRON STRATEGY
from strategy import Context, INotificacion, Error, Exito, Envio, FormIncompleto
CONTEXT = Context()

# API VONAGE
VONAGE_API_KEY = "4e17b532"
VONAGE_API_SECRET = "phEdCRhz7w7OmhED"
VONAGE_NUMBER = "51925884305"

app = Flask(__name__)

# MYSQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'crm_reclamos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config.from_object('config.DevelopmentConfig')
mysql = MySQL(app)


from factory import *
#############################################################################################################
@app.route("/")
def index():
    return render_template("index.html")

#############################################################################################################
# SERVICIO TECNICO
@app.route("/servicio")
def servicio():
    return render_template("servicio.html")

@app.route("/servicio_reclamo", methods=["GET","POST"])
def servicio_reclamo():
    cursor = mysql.connection.cursor()
    
    #Reclamo(nombres, ap_paterno, ap_materno, correo, dni, estado))
    if request.method == "POST":
        reclamo = ServicioReclamo(request.form["nombres"], request.form["ap_paterno"], request.form["ap_materno"], request.form["correo"], request.form["dni"], estado="pendiente", motivo="", detalle="", solicitud="", fecha=datetime.today().strftime('%Y-%m-%d'))
        
        cursor.execute("SELECT dni FROM cliente WHERE nombres=%s and apellido_paterno=%s and apellido_materno=%s and correo=%s and dni=%s", (reclamo.nombres, reclamo.ap_paterno, reclamo.ap_materno, reclamo.correo, reclamo.dni))
        
        data = cursor.fetchall()
        if data:
            session["dni"] = data[0]["dni"]
            return redirect(url_for("enviar"))
        else:
            flash(str(CONTEXT.request(Error)))
            return redirect(url_for("index"))
    return render_template("servicio_reclamo.html")



@app.route("/atencion_reclamo", methods=["GET","POST"])
def atencion_reclamo():
    cursor = mysql.connection.cursor()
    
    if request.method == "POST":
        r = AtencionReclamo(request.form["nombres"], request.form["ap_paterno"], request.form["ap_materno"], request.form["correo"], request.form["dni"], estado="pendiente", fecha=datetime.today().strftime('%Y-%m-%d'), msg=request.form["msg"])
        #nombres = request.form["nombres"]
        #ap_paterno = request.form["ap_paterno"]
        #ap_materno= request.form["ap_materno"]
        #correo = request.form["correo"]
        #dni = request.form["dni"]
        #telefono = request.form["telefono"]
        #msg = request.form["msg"]

        #cursor.execute("INSERT INTO atencion_reclamo (nombres, apellido_paterno, apellido_materno, correo, dni, telefono, msg) VALUES(%s,%s,%s,%s,%s,%s,%s)", (nombres, ap_paterno, ap_materno, correo, dni, telefono, msg))

        cursor.execute("INSERT INTO atencion_reclamo (nombres, apellido_paterno, apellido_materno, correo, dni, telefono, msg) VALUES(%s,%s,%s,%s,%s,%s,%s)", (r.nombres, r.ap_paterno, r.ap_materno, r.correo, r.dni, request.form["telefono"], r.msg))
        mysql.connection.commit()
        flash(str(CONTEXT.request(Exito)))

        return redirect(url_for("index"))

    return render_template("atencion_reclamo.html")

#############################################################################################################

@app.route("/preguntas")
def preguntas_frecuentes():
    return render_template("preguntas.html")

#############################################################################################################

@app.route("/robo-o-extravio")
def robo():
    return render_template("robo.html")

@app.route("/enviar", methods=["GET","POST"])
def enviar():
    cursor = mysql.connection.cursor()

    if request.method == "POST":
        motivo = request.form["motivo"]
        detalle = request.form["detalle"]
        solicitud = request.form["solicitud"]

        cursor.execute("INSERT INTO servicio_reclamo (dni, motivo, detalle, solicitud) VALUES(%s,%s,%s,%s)", (session["dni"], motivo, detalle, solicitud))
        mysql.connection.commit()
        flash(str(CONTEXT.request(Envio)))

        return redirect(url_for("index"))
    return render_template("enviar.html")

#############################################################################################################
# APIS EXTERNAS (VONAGE)

# Crear un nuevo objeto de cliente de Vonage:
vonage_client = vonage.Client(
    key=VONAGE_API_KEY, secret=VONAGE_API_SECRET
)

#############################################################################################################
# MSG API
@app.route('/send_sms', methods=['POST'])
def send_sms():
    # EndPoint via metodo POST que envia un mensaje

    # Extraer datos del formulario:
    numero = VONAGE_NUMBER
    tlf = request.form["tlf"]
    mensaje = request.form['mensaje']
    msg = f"❗Número extraviado: [{tlf}]\n{mensaje}"

    # Enviar SMS
    result = vonage_client.sms.send_message({
        'from': "Vonage APIs",
        'to': numero,
        'text': msg,
    })
    flash(str(CONTEXT.request(Envio)))
    return redirect(url_for('index'))

'''
curl -X "POST" "https://rest.nexmo.com/sms/json"
  -d "from=Vonage APIs"
  -d "text=A text message sent using the Vonage SMS API"
  -d "to=51925884305"
  -d "api_key=4e17b532"
  -d "api_secret=phEdCRhz7w7OmhED"
'''

#############################################################################################################
# WHATSAPP API
@app.route("/wsp", methods=["POST"])
def home():
    if request.form["wsp"] and request.form["tlf"]:
        
        url = "https://messages-sandbox.nexmo.com/v1/messages"
        tlf = request.form["tlf"]

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cliente WHERE telefono=%s", (tlf,))
        data = cursor.fetchall()

        if data:
            data = {
                "from":"14157386102",
                "to": f"{VONAGE_NUMBER}",
                "message_type": "text",
                "text": f'❗*Número extraviado*: {tlf}\n[+]Nombre cliente:\n{data[0]["apellido_paterno"]} {data[0]["apellido_materno"]} {data[0]["nombres"]}\n\n[+]Email de contacto:\n{data[0]["correo"]}\n\n[+]Mensaje:\n{request.form["wsp"]}',
                "channel": "whatsapp"
                }

            respuesta = requests.post(url, auth=("4e17b532", "phEdCRhz7w7OmhED"),json=data)

            flash(str(CONTEXT.request(Envio)))
            return redirect(url_for("index"))
        else:
            flash(str(CONTEXT.request(Error)))
            return redirect(url_for("index"))
    else:
        flash(str(CONTEXT.request(FormIncompleto)))
        return redirect(url_for("index"))

'''
curl -X POST https://messages-sandbox.nexmo.com/v1/messages 
    -u '4e17b532:phEdCRhz7w7OmhED'
    -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{
    "from": "14157386102",
    "to": "51925884305",
    "message_type": "text",
    "text": "Usando la api vonage de wsp",
    "channel": "whatsapp"
  }'
'''

#############################################################################################################
@app.route("/cancelar")
def cancelar():
    return render_template("cancelar.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)
