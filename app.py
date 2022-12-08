from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__)

# MYSQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'crm'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# LLAVE
app.secret_key = "my_secret_key"

# PAGINA PRINCIPAL DEL CRM //               index.html
@app.route("/")
def index():
    return render_template("index.html")

# PAGINA PRINCIPAL DE RECLAMOS              reclamo.html
@app.route("/reclamo")
def reclamo():
    return render_template("reclamo.html")


from strategy import Context, Exito, IMensaje, Error, Mensaje
CONTEXT = Context()


# ENVIAR LOS DATOS ID_CLIENTE NRO_BOLETA    activo.html
@app.route("/buscar", methods=["POST"])     
def buscar():
    cursor = mysql.connection.cursor()
    session["id_cliente"] = request.form["id_cliente"]
    session["nro_boleta"] = request.form["nro_boleta"]

    cursor.execute("SELECT id_cliente, nro_boleta,telefono FROM cliente WHERE id_cliente=%s and nro_boleta=%s", (session["id_cliente"], session["nro_boleta"]))
    data = cursor.fetchall()
    
    if data:
        session["telefono"] = data[0]["telefono"]
        cursor.execute("SELECT id_reclamo FROM reclamos_generales ORDER BY id_reclamo DESC LIMIT 1")
        session["id_reclamo"] = cursor.fetchall()[0]["id_reclamo"]
        
        flash(str(CONTEXT.request(Exito)))

        return redirect(url_for("activo"))
    else:
        flash(str(CONTEXT.request(Error)))

        return redirect(url_for("reclamo"))

# RENDERIZAR PAGINA HABILITADO PARA INTERACTUAR
@app.route("/activo", methods=["GET","POST"])
def activo():
    return render_template("activo.html",id_cliente=session["id_cliente"], nro_boleta=session["nro_boleta"], telefono=str(session["telefono"]), id_reclamo=session["id_reclamo"])

# MOSTRAR TABLA
@app.route("/tabla")
def tabla():
    caso = request.args["caso"]
    cur = mysql.connection.cursor()

    cur.execute("SELECT titulo,descripcion FROM reclamos_generales WHERE caso=%s", (caso,))
    tabla = cur.fetchall()

    c1 = '''
	<div class="fixed bg-gray-900 bg-opacity-60 h-screen inset-0 w-screen z-40"id=overlay></div><div class="fixed  -translate-x-1/2 -translate-y-1/2 bg-white drop-shadow-lg left-1/2 px-4 py-4 rounded-md space-y-4 top-1/2 z-50"id=dialogo><div class="flex flex-col"><div class="lg:-mx-8 overflow-x-auto sm:-mx-61"><div class="py-2 lg:px-8 sm:px-6"><div><table class="w-full text-left"><thead class="flex w-full bg-black text-white"><tr class="flex w-full mb-4"><th class="p-4 w-1/2">Pregunta<th class="p-4 w-1/2">Descripción<tbody class="flex w-full bg-grey-light flex-col items-center justify-between overflow-y-scroll"style=height:50vh>'''
    c2 = ''
    for i in tabla:
        c2 += '''<tr class="flex w-full mb-4"><td class="p-4 w-1/2">'''
        c2 += i["titulo"]
        c2 += '''<td class="p-4 w-1/2">''' 
        c2 += i["descripcion"] 
        c2 += '</tr>'
    c3= '''</table></div></div></div></div><center><button class="py-2 bg-pink-500 cursor-pointer hover:bg-pink-700 px-5 rounded-md text-white"id=close>Aceptar</button></center></div>'''
    flash(c1+c2+c3)
    return redirect(url_for("activo"))
    #return render_template("activo.html",id_cliente=session["id_cliente"], nro_boleta=session["nro_boleta"], telefono=str(session["telefono"]), id_reclamo=session["id_reclamo"], tabla=tabla)

# ENVIAR MENSAJE RECLAMO 
@app.route("/mensaje", methods=["POST"])
def enviar_mensaje():
    
    mensaje = request.form["mensaje"]
    
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO solucion_clientes (id_cliente, nro_boleta, solucion) VALUES(%s,%s,%s)", (session["id_cliente"], session["nro_boleta"], mensaje))
    mysql.connection.commit()

    flash(str(CONTEXT.request(Mensaje)))

    return redirect(url_for("reclamo"))

# TELEFONO
@app.route("/telefono", methods=["GET"])
def telefono():
    flash('''
    <div id="overlay" class="fixed z-40 w-screen h-screen inset-0 bg-gray-900 bg-opacity-60"></div><div id="dialogo" class="fixed z-50 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-md px-4 py-4 space-y-4 drop-shadow-lg"> <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-green-100"> <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" aria-hidden="true" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M15 3.75a.75.75 0 01.75-.75h4.5a.75.75 0 01.75.75v4.5a.75.75 0 01-1.5 0V5.56l-4.72 4.72a.75.75 0 11-1.06-1.06l4.72-4.72h-2.69a.75.75 0 01-.75-.75z" clip-rule="evenodd"></path><path fill-rule="evenodd" d="M1.5 4.5a3 3 0 013-3h1.372c.86 0 1.61.586 1.819 1.42l1.105 4.423a1.875 1.875 0 01-.694 1.955l-1.293.97c-.135.101-.164.249-.126.352a11.285 11.285 0 006.697 6.697c.103.038.25.009.352-.126l.97-1.293a1.875 1.875 0 011.955-.694l4.423 1.105c.834.209 1.42.959 1.42 1.82V19.5a3 3 0 01-3 3h-2.25C8.552 22.5 1.5 15.448 1.5 6.75V4.5z" clip-rule="evenodd"></path></svg> </div><div class="py-5 border-t border-b border-gray-300 text-center"> <p class="font-bold">Llamada de conciliación</p><p>telefono : ''' + str(session["telefono"]) + '''</p></div><center> <button id="close" class="px-5 py-2 bg-pink-500 hover:bg-pink-700 text-white cursor-pointer rounded-md"> Aceptar </button> </center> </div>
    ''')
    return redirect(url_for("activo"))

##########################################################################
# 3
@app.route("/verificar_tramite")
def verificar_tramite():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT departamento , count(*) AS cantidad FROM reclamos GROUP BY departamento")
    count = cursor.fetchall()
    
    cantidad = []
    for i in count:
        cantidad.append(i["cantidad"])
    lista = {'ventas': cantidad[3], 'cliente': cantidad[1], 'marketing': cantidad[2], 'administrativo': cantidad[0]}

    return render_template("verificar.html", data = lista)

@app.route("/verificar_tramite", methods=["POST"])
def verificar():
    cursor = mysql.connection.cursor()
    #OBTENER DATOS POR ID_RECLAMO
    nro_reclamo = request.form["nro_reclamo"]
    cursor.execute("SELECT id_reclamo,CONCAT(nombre,' ',apellido) AS usuario,direccion,telefono FROM reclamos WHERE id_reclamo=%s", (nro_reclamo))
    data = cursor.fetchall()[0]
    
    cursor.execute("SELECT departamento , count(*) AS cantidad FROM reclamos GROUP BY departamento")
    count = cursor.fetchall()
    
    cantidad = []
    for i in count:
        cantidad.append(i["cantidad"])
    lista = {'ventas': cantidad[3], 'cliente': cantidad[1], 'marketing': cantidad[2], 'administrativo': cantidad[0]}

    # OBTENER DATOS DEL CLIENTE EN TABLA
    cursor.execute('SELECT id_reclamo, CONCAT(YEAR(fecha),"-",MONTH(fecha),"-",DAY(fecha)) AS fecha, departamento, tipo_reclamo, subtipo, mensaje, estado FROM reclamos WHERE id_reclamo=%s', (nro_reclamo))
    tabla = cursor.fetchall()
    print(tabla[0])
    return render_template("verificar2.html", user=data, data=lista, tabla=tabla)

###########################################################################
# 2
@app.route("/tramite")
def tramite():
    return render_template("tramite.html")

@app.route("/enviar_tramite", methods=["POST"])
def enviar_tramite():
    return session["id_cliente"]


if __name__=="__main__":
    app.run(debug=True, port=3000)
