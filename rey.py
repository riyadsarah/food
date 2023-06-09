# Input nilai ujian
nilai = float(input("Masukkan nilai ujian: "))

# Memeriksa kondisi nilai
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

# Menampilkan hasil
print("Grade: ", grade)
print("Keterangan: ", keterangan)
