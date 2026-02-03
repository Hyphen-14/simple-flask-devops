from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/') # --> Halaman utama
def home():
    return render_template('game.html')

# Program dibawah memastikan server nya berjalan ketika aplikasi di eksekusi
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 7860, debug = True)
# 0.0.0.0 merupakan Ip address yang bisa diakses dari luar
# huggingface menggunakan port 7860 secara default