def pemisah():        #Fungsi untuk pembatas
    print( )
def cetak():          #Fungsi untuk mencetak judul program
    print(">>> Program Penghitungan Rata-Rata <<<")
cetak()               #mencetak perintah fungsi
def total():
    return (hrn+uts+uas)/3
try:
    pemisah()         #mencetak perintah fungsi
    hrn = int(input("Masukkan Nilai Harian    : "))        #user menginput nilai harian yang ingin dijumlahkan
    uts = int(input("Masukkan Nilai UTS       : "))     #user menginput nilai UTS 
    uas = int(input("Masukkan Nilai UAS       : "))     #user menginput nilai UAS
    total()                                             #menjalankan perintah fungsi
    hasil = total()                                     #membuat variable baru jika hasil sama dengan total
    print("Nilai Rata-Rata                    = ",hasil)#mencetak hasil dari yang telah dijumlahkan difungsi dari nilai yang diinput user
except ValueError:                                      #menjalankan perintah pengecualian
    print('Inputan hanya menerima nilai dalam bentuk angka (integer) !')    #mencetak kalimat pengecualian

#Sumber mengambil dari modul praktikum algoritma pemprograman ke 6