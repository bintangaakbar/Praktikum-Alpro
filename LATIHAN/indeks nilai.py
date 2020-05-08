print("---- CEK KELULUSAN MATA KULIAH KALKULUS ----")

akhir = int(input("Masukkan nilai akhir : "))
kehadiran = int(input("Masukkan Persentase kehadiran :"))

if  kehadiran > 75:
        if 81 <= akhir <= 100:
            print("Selamat anda lulus")
            print("dengan Indeks A")
    
        elif 71 <= akhir <= 81:
            print("Selamat anda lulus")
            print("dengan Indeks B")
    
        elif 61 <= akhir <= 71:
            print("Selamat anda lulus")
            print("dengan Indeks C")

        elif 51 <= akhir <= 61:
            print("Selamat anda lulus")
            print("dengan Indeks D")

        elif 41 <= akhir <= 51:
            print("Selamat anda lulus")
            print("dengan Indeks E") 

        else:
            print("maaf anda tidak lulus")

else:
    print("Maaf anda harus mengulang")