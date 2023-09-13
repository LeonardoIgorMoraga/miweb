from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from dotenv import load_dotenv
import os

resultado = None

# Cargar las variables de entorno desde .env
load_dotenv()

# Crear una instancia de la aplicación Flask
app = Flask(__name__)
# app.secret_key = os.getenv("SECRET_KEY")

# Conectar a la base de datos
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

# Ruta para la página de inicio de sesión
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # verificamos usuario y contraseña
        cursor = db.cursor()
        cursor.execute("SELECT email FROM usuario WHERE username = %s AND password = %s", (username, password))
        resultado = cursor.fetchone()
        cursor.close() #buena practica

        if resultado:
            return "Bienvenid@, tu correo es " + resultado[0]
        else:
            return "Datos incorrectos..."
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
