from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nilai = request.form.get('nilai')
        tanggal_lahir = request.form.get('tanggal_lahir')

        if nilai and tanggal_lahir:
            try:
                nilai = float(nilai)
                tanggal_lahir = datetime.datetime.strptime(tanggal_lahir, '%Y-%m-%d')
                umur = calculate_age(tanggal_lahir)

                if nilai >= 90:
                    grade = 'A'
                    keterangan = 'Sangat baik'
                elif nilai >= 80:
                    grade = 'B'
                    keterangan = 'Baik'
                elif nilai >= 70:
                    grade = 'C'
                    keterangan = 'Cukup'
                elif nilai >= 60:
                    grade = 'D'
                    keterangan = 'Kurang'
                else:
                    grade = 'E'
                    keterangan = 'Sangat kurang'
                
                return render_template('index.html', grade=grade, keterangan=keterangan, umur=umur)
            except ValueError:
                return render_template('index.html', pesan_error='Masukkan angka dan format tanggal yang valid!')
        else:
            return render_template('index.html', pesan_error='Masukkan angka dan tanggal lahir!')

    return render_template('index.html')

def calculate_age(date_of_birth):
    today = datetime.date.today()
    age = today.year - date_of_birth.year
    if today < datetime.date(today.year, date_of_birth.month, date_of_birth.day):
        age -= 1
    return age

if __name__ == '__main__':
    app.run(debug=True)
