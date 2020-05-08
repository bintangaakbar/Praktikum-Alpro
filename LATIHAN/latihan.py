print = str(input("masukkan nama anda"))
print =int (input("masukkan nim anda"))
nilai1 = int(input ("masukkan nilai minggu ke 1 : "))
nilai2 =int(input ("masukkan nilai minggu ke 2  : "))
nilai3 =int(input ("masukkan nilai minggu ke 3  :"))

ttl(nilai1 + nilai2 + nilai3)/3

if ttl > 80:
    print("selamat anda mendapatkan nilai A, nilai anda", ttl)
elif ttl < 80:
    print("selamat anda mendapatkan nilai B, nilai anda", ttl)
else:
    print("maaf anda harus mengulang")
