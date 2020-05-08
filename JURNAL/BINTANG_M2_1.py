print(">>> PENGHITUNG NILAI AKHIR")

nama = str(input("Masukkan Nama    :  "))
nim = int(input("Masukkan NIM    :  "))
kuis= int(input("Masukkan Nilai Kuis   :  "))
uts= int(input("Masukkan nilai UTS   :   "))
uas= int(input("Masukkan Nilai UAS   :   "))
prk= int(input("Masukkan Nilai Praktikum  :  "))
total = (kuis + uts + uas + prk )/4

print ("+++++* Nilai Kelulusan *+++++")
print("NAMA         :  ",nama)
print ("NIM           :  ",nim)
print ("Nilai Akhir :  ",total)
if total > 80:
    print ("Indeks     : A")
    print ("LULUS")
elif 70 < total <= 80:
    print("Indeks     : AB")
    print ("LULUS")
elif 65 < total <= 70:
    print("Indeks     : B")
    print ("LULUS")
elif 60 < total <= 65:
    print("Indeks     : BC")
    print ("LULUS")
elif 50 < total <= 60:
    print("Indeks     : C")
    print ("LULUS")
elif 40 < total <= 50:
    print("Indeks     : D")
    print ("LULUS")
else:
    print("tidak lulus")