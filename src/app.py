from dotenv import load_dotenv
import os
import mysql.connector
from flask import Flask, render_template
from config import config

#crear la instancia flask
app = Flask(__name__)

# Definir una ruta para la página de inicio
@app.route('/')
def inicio():
    #return "Bienvenido a mi página web de inicio de sesión"
    return render_template('index.html')

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run() #aqui tambien se puede cambiar el puerto, pero lo dejare por defecto..
    #luego preguntarle a nepu el porque ahora puedo modificar el servidor en tiempo real, esta en depuracion...

#cargar las variables de entorno que deseo proteger
load_dotenv()

#creando la coneccion a mi base de datos
baseDeDatos = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_DATABASE")
)

