from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

#  Koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flaskmysql"   # pastikan sesuai di phpMyAdmin kamu
)

#  Route utama — untuk menampilkan halaman HTML
@app.route('/')
def index():
    return render_template('index.html')

#  Route REST API — untuk diambil lewat jQuery
@app.route('/users')
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
