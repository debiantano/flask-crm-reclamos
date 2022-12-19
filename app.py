from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_mysqldb import MySQL
import vonage

VONAGE_API_KEY = "4e17b532"
VONAGE_API_SECRET = "phEdCRhz7w7OmhED"
VONAGE_NUMBER = "51925884305"

# Create a new Vonage Client object:
vonage_client = vonage.Client(
    key=VONAGE_API_KEY, secret=VONAGE_API_SECRET
)

app = Flask(__name__)

# MYSQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'crm_reclamos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.secret_key="u39@v9kGE#cs"
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

# SERVICIO TECNICO
@app.route("/servicio")
def servicio():
    return render_template("servicio.html")

@app.route("/servicio_reclamo", methods=["GET","POST"])
def servicio_reclamo():
    cursor = mysql.connection.cursor()
    
    if request.method == "POST":
        nombres = request.form["nombres"]
        ap_paterno = request.form["ap_paterno"]
        ap_materno= request.form["ap_materno"]
        correo = request.form["correo"]
        dni = request.form["dni"]
        
        cursor.execute("SELECT telefono FROM cliente WHERE nombres=%s and apellido_paterno=%s and apellido_materno=%s and correo=%s and dni=%s", (nombres, ap_paterno, ap_materno, correo, dni))
        
        data = cursor.fetchall()
        if data:
            session["telefono"] = data[0]["telefono"]
            return redirect(url_for("enviar"))
        else:
            flash('''<div id="overlay" class="fixed z-40 w-screen h-screen inset-0 bg-gray-900 bg-opacity-60"></div><div id="dialogo" class="fixed z-50 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 bg-white rounded-md px-8 py-6 space-y-5 drop-shadow-lg"><div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-red-100"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M11.001 10h2v5h-2zM11 16h2v2h-2z"></path><path d="M13.768 4.2C13.42 3.545 12.742 3.138 12 3.138s-1.42.407-1.768 1.063L2.894 18.064a1.986 1.986 0 0 0 .054 1.968A1.984 1.984 0 0 0 4.661 21h14.678c.708 0 1.349-.362 1.714-.968a1.989 1.989 0 0 0 .054-1.968L13.768 4.2zM4.661 19 12 5.137 19.344 19H4.661z"></path></svg></div><div class="py-5 border-t border-b border-gray-300 text-center"><p>Los datos del cliente no han sido encontrados</p></div><div class="flex justify-end"><button id="close" class="px-5 py-2 bg-purple-500 hover:bg-purple-700 text-white cursor-pointer rounded-md">Aceptar</button></div></div>''')
            return redirect(url_for("index"))

    return render_template("servicio_reclamo.html")

@app.route("/atencion_reclamo", methods=["GET","POST"])
def atencion_reclamo():
    cursor = mysql.connection.cursor()
    
    if request.method == "POST":
        nombres = request.form["nombres"]
        ap_paterno = request.form["ap_paterno"]
        ap_materno= request.form["ap_materno"]
        correo = request.form["correo"]
        dni = request.form["dni"]
        telefono = request.form["telefono"]
        msg = request.form["msg"]

        cursor.execute("INSERT INTO atencion_reclamo (nombres, apellido_paterno, apellido_materno, correo, dni, telefono, msg) VALUES(%s,%s,%s,%s,%s,%s,%s)", (nombres, ap_paterno, ap_materno, correo, dni, telefono, msg))
        mysql.connection.commit()

        flash('''<div id="overlay" class="fixed z-40 w-screen h-screen inset-0 bg-gray-900 bg-opacity-60"></div><div id="dialogo" class="fixed z-50 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 bg-white rounded-md px-8 py-6 space-y-5 drop-shadow-lg"><div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-green-100"><svg class="h-6 w-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div><div class="py-5 border-t border-b border-gray-300 text-center"><p>Validación exitosa</p></div><div class="flex justify-end"><button id="close" class="px-5 py-2 bg-purple-500 hover:bg-purple-700 text-white cursor-pointer rounded-md">Aceptar</button></div></div>''')

        return redirect(url_for("index"))

    return render_template("atencion_reclamo.html")



@app.route("/cancelar")
def cancelar():
    return render_template("cancelar.html")

@app.route("/preguntas")
def preguntas_frecuentes():
    return render_template("preguntas.html")

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

        cursor.execute("INSERT INTO cliente_reclamo (dni, motivo, detalle, solicitud) VALUES(%s,%s,%s,%s)", (session["telefono"], motivo, detalle, solicitud))
        mysql.connection.commit()

        flash('''<div id="overlay" class="fixed z-40 w-screen h-screen inset-0 bg-gray-900 bg-opacity-60"></div><div id="dialogo" class="fixed z-50 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 bg-white rounded-md px-8 py-6 space-y-5 drop-shadow-lg"><div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-green-100"><svg class="h-6 w-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div><div class="py-5 border-t border-b border-gray-300 text-center"><p>Validación exitosa</p></div><div class="flex justify-end"><button id="close" class="px-5 py-2 bg-purple-500 hover:bg-purple-700 text-white cursor-pointer rounded-md">Aceptar</button></div></div>''')

        return redirect(url_for("index"))
    return render_template("enviar.html")



@app.route('/send_sms', methods=['POST'])
def send_sms():
    """ A POST endpoint that sends an SMS. """

    # Extract the form values:
    numero = "51925884305"
    mensaje = request.form['mensaje']

    # Enviar SMS
    result = vonage_client.sms.send_message({
        'from': "Vonage APIs",
        'to': numero,
        'text': mensaje,
    })
    # Redirect the user back to the form:
    return redirect(url_for('index'))

'''
curl -X "POST" "https://rest.nexmo.com/sms/json" -d "from=Vonage APIs" -d "text=Mensaje de texto" -d "to=51925884305" -d "api_key=4e17b532" -d "api_secret=phEdCRhz7w7OmhED"
'''

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)