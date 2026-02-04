import os
from flask import Flask
from flask import render_template

base_dir = os.path.dirname(os.path.dirname(__file__))
app = Flask(__name__)

@app.route('/') # --> Halaman utama
def home():
    file_path = os.path.join(base_dir, 'game.html')
    if not os.path.exists(file_path):
        return f"<h1>Error: File game.html tidak ditemukan di {file_path}!</h1><p>Cek tab Files apakah sudah terupload?</p>"
    
    return render_template('game.html')

# Program dibawah memastikan server nya berjalan ketika aplikasi di eksekusi
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 7860)
# 0.0.0.0 merupakan Ip address yang bisa diakses dari luar
# huggingface menggunakan port 7860 secara default