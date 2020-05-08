import numpy as np      #import modul numpy sebagai np
class buatsendiri():    #membuat class
    def judul(self):    #fungsi untuk judul
        print("="*20, " Menghitung harga beras ", "="*20)   #mencetak isi dari fungsi judul
   
    def data(self):     #membuat fungsi data
        beras = [14000, 12500, 13000, 10000, 11000, 11000, 9750]    #variable harga beras
        harian = [500, 400, 300, 340, 557, 200, 900]    #variable kunjungan harian
        print("Data Harga Beras                             : ",beras) #mencetak data dari variable beras
        print("Data Kunjungan Harian                        : ",harian) #mencetak data dari variable kunjungan harian
   
    def mean(self): #membuat fungsi mean
        beras = [14000, 12500, 13000, 10000, 11000, 11000, 9750] #variable harga beras
        hasil = sum(beras)/len(beras)   #hasil sama dengan penjumlahan dari beras 
        print("Mean Harga Beras                             : Rp.", float(hasil))   #mencetak variable hasil

    def median(self):   #membuat fungsi median
        beras = [14000, 12500, 13000, 10000, 11000, 11000, 9750] #variable harga beras
        if len(beras) % 2 == 0: #membuat fungsi if dan else untuk mencari hasil
            ok = int(len(beras) / 2)    #ok sama dengan beras dibagi 2
            hasil = (beras[ok - 1] + beras[ok] / 2) #membuat variable hasil dari ok
        else:   #jika kondisi tidak sesuai sama pernyataan diatas
            ok = int((len(beras) + 1 ) / 2) #ok sama dengan beras + 1 dibagi 2
            hasil = beras[ok - 1] #membuat variavle hasil dari ok
    
        print("Median Harga Beras                           : Rp.", hasil)  #mencetak hasil dari median
    
    def modus(self):
        beras = [14000,12500,13000,10000,11000,11000,9750] 
        modusx = max(set(beras), key=beras.count)   
        a = beras.count(modusx)
        b = []      
        c = b[::a]  
        modus = "Modus data adalah "
        moduss = []
        if len(c) == 1: 
            modus += str(c[0])
        else:
            for i in c:
                moduss.append(str(i))
            modus += " & ".join(moduss)
        print("modus Harga Beras                            : Rp.",modusx)

    def deviasi(self): #membuat fungsi dari deviasi
        beras = [14000,12500,13000,10000,11000,11000,9750] #variable harga beras
        Deviasi = np.std(beras) #membuat variable deviasi sama dengan beras dengan modul
        print("Standar Deviasi Harga beras                  : ",round(Deviasi,2)) #mencetak hasil dari deviasi

    def kuartil(self): #membuat fungsi dari kuartil
        beras = [14000,12500,13000,10000,11000,11000,9750] #variable harga beras
        kuartil1 = np.quantile(beras, 0.25) #membuat variable kuartil pertama
        kuartil2 = np.quantile(beras, 0.5)  #membuat variable kuartil kedua
        kuartil3 = np.quantile(beras, 0.75) #membuat variable kuartil ketiga
        print("Kuartil 1 Harga Beras                        : Rp.", kuartil1) #mencetak hasil kuartil pertama
        print("Kuartil 2 Harga Beras                        : Rp.", kuartil2) #mencetak hasil kuartil kedua
        print("Kuartil 3 Harga Beras                        : Rp.", kuartil3) #mencetak hasil kuartil ketiga
    
    def kovr(self):
        beras = [14000,12500,13000,10000,11000,11000,9750]  #variable harga beras
        harian = [500, 400, 300, 340, 557, 200, 900]    #variable kunjungan harian
        data1 = np.array([beras, harian])          #membuat variable baru data1 sama dengan beras dan harian
        print("Kovarian Harga Beras dengan Jumlah Kunjungan : \n", np.cov(data1)) #mencetak hasil kovarian dengan modul
        print() #membuat pembatas antara kovarian dan korelasi
        print("Korelasi Harga Beras dengan Jumlah Kunjungan : \n", np.corrcoef(data1)) #mencetak hasil dari korelasi dengan modul


cetak = buatsendiri()       #membuat variable baru class sama dengan cetak
cetak.judul()               #Mencetak fungsi judul dari class
cetak.data()                #Mencetak fungsi data dari class 
cetak.mean()                #Mencetak fungsi mean dari class
cetak.median()              #Mencetak fungsi median dari class
cetak.modus()               #Mencetak fungsi modus dari class
cetak.deviasi()             #Mencetak fungsi deviasi dari class
cetak.kuartil()             #Mencetak fungsi kuartil dari class
cetak.kovr()                #Mencetak fungsi kovarian dan korelasi dari class