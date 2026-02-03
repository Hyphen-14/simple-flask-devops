from flask import Flask;
app = Flask(__name__)

@app.route('/') # --> Halaman utama
def home():
    return "<h1>Welcome to the Home Page</h1>"

# Program dibawah memastikan server nya berjalan ketika aplikasi di eksekusi
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
# 0.0.0.0 merupakan Ip address yang bisa diakses dari luar