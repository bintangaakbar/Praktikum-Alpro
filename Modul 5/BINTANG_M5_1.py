import os

class menu():
    def Pilihan(self):
        print("""\tKalkulator Python 3
                \t1.Penjumlahan
                \t2.Pengurangan
                \t3.Perkalian
                \t4.Pembagian""")

cetak = menu()
cetak.Pilihan()
print()
pil = int(input("\tMau Pilih Nomor Berapa ? "))

angka1 = int(input("Berapa Nilai pertama : "))
angka2 = int(input("Berapa Nilai kedua : "))

def Penjumlahan(angka1, angka2):
    hasil = angka1 + angka2
    print("Hasil Penjumlahan adalah : ",hasil)
    return Penjumlahan

def Pengurangan(angka1, angka2):
    hasil = angka1 - angka2
    print("Hasil Pengurangan adalah : ",hasil)
    return Pengurangan

def Perkalian(angka1, angka2):
    hasil = angka1 * angka2
    print("Hasil Perkalian Adalah : ",hasil)
    return Perkalian

def Pembagian(angka1, angka2):
    hasil = angka1 / angka2
    print("Hasil Pembagian Adalah : ",hasil)
    return Pembagian


if pil == 1:
    Penjumlahan(angka1, angka2)
elif pil == 2:
    Pengurangan(angka1, angka2)
elif pil == 3:
    Perkalian(angka1, angka2)
elif pil == 4:
    Pembagian(angka1, angka2)
else:
    print("Maaf Menu belum tersedia di kalkulator kami")
    os.system("cls")
    exit()