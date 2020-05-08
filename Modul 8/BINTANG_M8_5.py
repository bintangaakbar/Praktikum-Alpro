# #sumber modul 8 praktikum
# import matplotlib.pyplot as plt #import modul dari library

# plt.title('Total Nilai Kinerja') #judul dari grafik

# cowo =[10.34, 21.01, 23.68, 25.29, 8.77, 26.88, 15.04, 14.78, 10.27, 15.42, 18.43, 21.58]
# cewe =[24.59, 35.26, 14.83]

# plt.boxplot([cowo, cewe], patch_artist=False ,showmeans=True, meanline=True, labels=["Laki-Laki", "Perempuan"]) #memasukan data 

# plt.show()   #menampilkan grafik





class persegipanjang:
    def luaspersegipanjang(panjang, lebar):
        luas = int(panjang) * int(lebar)
        return luas

    panjang = int(input("Masukkan Nilai Panjang   : "))
    lebar = int(input("Masukkann Nilai Lebar    : "))
    print("Luas Persegi panjang     : ", luaspersegipanjang(panjang, lebar))
