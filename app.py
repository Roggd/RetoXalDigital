from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL
import requests
from requests.models import Response

app = Flask(__name__)
# conección con mysql 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'vuelosMex'
mysql = MySQL(app)

#Inicio
@app.route('/')
def index():
    return render_template('index.html')

#Parte 2: SQL
@app.route('/sql')
def sql():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT nombre_aeropuerto, COUNT(v.id_movimiento) AS total FROM aeropuertos a, vuelos v WHERE a.id_aeropuerto = v.id_aeropuerto GROUP BY nombre_aeropuerto ORDER BY total DESC LIMIT 1;')
    r1 = cursor.fetchall()
    cursor.execute('SELECT nombre_aerolinea, COUNT(v.id_movimiento) AS total FROM aerolineas a, vuelos v WHERE a.id_aerolinea = v.id_aerolinea GROUP BY nombre_aerolinea ORDER BY total DESC LIMIT 1;')
    r2 = cursor.fetchall()
    cursor.execute('SELECT dia, COUNT(dia) total FROM vuelos GROUP BY dia ORDER BY total DESC LIMIT 1;')
    r3 = cursor.fetchall()
    cursor.execute('SELECT nombre_aerolinea, COUNT(v.id_movimiento) as tot, dia AS total FROM aerolineas a, vuelos v WHERE a.id_aerolinea = v.id_aerolinea GROUP BY nombre_aerolinea, dia ORDER BY dia;')
    r4 = cursor.fetchall()
    return render_template('sql.html', resp1 = r1, resp2 = r2, resp3 = r3, resp4 = r4)

#Parte 1: Programación
@app.route('/json')
def json():

    return render_template('json.html')

if __name__ == '__main__':
 app.run(port=3000, debug=True)
