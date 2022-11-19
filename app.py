from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MYSQL CONNECTION
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'test'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# SETTINGS
app.secret_key = "my_secret_key"

@app.route("/")
def index():
	return render_template("index.html",)

##########################################################

@app.route("/reclamo")
def reclamo():
	return render_template("reclamo.html")

@app.route("/message", methods=["POST"])
def message():
	if request.method == "POST":
		dni = request.form["dni"]
		nombre = request.form["nombre"]
		apellido = request.form["apellido"]
		ciudad = request.form["ciudad"]
		correo = request.form["correo"]
		telefono = request.form["telefono"]
		direccion = request.form["direccion"]

		departamento = request.form["departamento"]
		tipo_reclamo = request.form["tipo_reclamo"]
		subtipo = request.form["subtipo"]
		mensaje = request.form["mensaje"]

	cursor = mysql.connection.cursor()
	cursor.execute("INSERT INTO reclamos (fecha, dni, nombre, apellido, ciudad, correo, telefono, direccion, departamento, tipo_reclamo, subtipo, mensaje, estado) VALUES (now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, 'por atender')", (dni, nombre, apellido, ciudad, correo, telefono, direccion, departamento, tipo_reclamo, subtipo, mensaje))

	mysql.connection.commit()
	
	return redirect(url_for('index'))

@app.route("/busqueda", methods=["GET","POST"])
def busqueda():
	if request.method == "POST":
		nombre = request.form["nombre"]
		apellido = request.form["apellido"]
		estado = request.form["estado"]
		departamento = request.form["departamento"]

		if nombre and apellido and estado and departamento:
			print("Estan llenos")
			cur = mysql.connection.cursor()
			cur.execute('''
			SELECT id_reclamo, fecha, departamento, mensaje, estado FROM reclamos WHERE nombre LIKE %s AND apellido LIKE %s AND estado LIKE %s AND departamento LIKE %s
			''', (nombre,apellido,estado,departamento))
			data = cur.fetchall()

	else:
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM reclamos")
		data = cur.fetchall()

	return render_template("busqueda.html", reclamos = data)

@app.route("/tramite")
def tramite():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM reclamos")
	data = cur.fetchall()
	return render_template("tramite.html", reclamos = data)

if __name__ == "__main__":
	app.run(port=3000, debug=True)