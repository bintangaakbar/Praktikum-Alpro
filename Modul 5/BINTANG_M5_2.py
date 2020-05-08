import os
from time import sleep

class menu():
    def makanan(self):
        print("""\tPesan Ayam Geprek Bentol
                \t1.Nasi Ayam Geprek Bentol
                \t2.Nasi Ayam Geprek Matah
                \t3.Nasi Ayam Geprek Crispy
                \t4.Nasi Ayam Geprek Original
                \t5.Exit""")


def pesan():
    jmlh = int(input("Berapa Banyak pesan ?  "))
    nama = input("Pesanan atas nama  :  ")
    total_hrg = jmlh * harga
    os.system('cls')
    print("-"*10)
    print("Makanan telah dipesan!")
    print("Atas nama   : ", nama)
    print("Total Harga : ", "Rp", total_hrg)
    sleep(2)

cetak = menu()
cetak.makanan()

pil = int(input("Mau Pilih Nomor Berapa ? "))

if pil == 1:
    harga = 20000
    print("-"*15)
    print("\tNasi Ayam Geprek Bentol")
    print("\tHarga  : Rp.20000")
    pesan()
elif pil == 2:
    harga = 15000
    print("-"*15)
    print("\tNasi Ayam Geprek Matah")
    print("\tHarga  : Rp.15000")
    pesan()
elif pil == 3:
    harga = 19000
    print("-"*15)
    print("\tNasi Ayam Geprek Crispy")
    print("\tHarga  : Rp.19000")
    pesan()
elif pil == 4:
    harga = 17000
    print("-"*15)
    print("\tNasi Ayam Geprek Original")
    print("\tHarga  : Rp.17000")
    pesan()
elif pil == 5:
    print("")
    print("\t  >>> Sampai Jumpa lagi <<<")
    sleep(2)
    os.system('cls')
    sleep(1)
    exit
    sleep(1)
else:
    os.system('cls')
    print(">>>  Maaf, Lapangan tidak ada di list kami!   <<<")
    
    
print("#stayHome", "#DiRumahAja")
