print (">>>>    Check Indeks Nilai     <<<<")

nama = str (input ("masukkan nama mahasiswa :   "))
nilai = int (input ("masukkan nilai mahasiswa   :   "))

if nilai >= 90:
    grade= "A"
elif nilai >= 80:
    grade= "B+"
elif nilai >= 70:
    grade= "B"
elif nilai >= 60:
    grade= "C+"
elif nilai >= 50:
    grade= "C"
elif nilai >= 40:
    grade= "D"
else:
    grade="E"
print ("mahasiswa", nama, "mendapatkan Indeks Nilai  : ", grade)