import numpy as np
import statistics as st      
class buatsendiri():   
    def judul(self): 
        print("Kota                                         : Washington DC")  
   
    def data(self):     
        suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
        lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76]  
        print("Data Suhu Udara 10 hari terakhir              : ",suhu) 
        print("Data Kelembaban 10 hari terakhir              : ",lembab)

class suhu():
    def judul(self):
        print("="*20, "Menghitung Suhu Udara", "="*20)

    def mean(self): 
        suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32]
        hasil = np.mean(suhu)   
        print("Mean Suhu                                   : Rp.", float(hasil))  
    
    def median(self):
        suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32]
        hasil = np.median(suhu)
        print("Median Suhu Udara                           : Rp.", hasil) 
    
    def modus(self): 
        suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
        print("modus Suhu Udara                            : Rp.",st.mode(suhu))
        print("modus Suhu Udara                            : Rp.",st.multimode(suhu)) 
 

    def deviasi(self): 
        suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
        hasil = np.std(suhu) 
        print("Standar Deviasi Suhu Udara                  : ",round(hasil,2)) 

    def kuartil(self): 
        suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
        kuartil1 = np.quantile(suhu, 0.25) 
        kuartil2 = np.quantile(suhu, 0.5)  
        kuartil3 = np.quantile(suhu, 0.75) 
        print("Kuartil 1 Suhu Udara                        : Rp.", kuartil1) 
        print("Kuartil 2 Suhu udara                        : Rp.", kuartil2) 
        print("Kuartil 3 Suhu Udara                        : Rp.", kuartil3)

class Kelembaban():   
    def judul(self):
        print("="*20, "Menghitung Kelembaban", "="*20)  

    def mean(self): 
        lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76]
        hasil = np.mean(lembab)   
        print("Mean Lembab                                 : Rp.", float(hasil))  
    
    def median(self):
        lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76]
        hasil = np.median(lembab)
        print("Median Kelembaban udara                      : Rp.", hasil) 
    
    def modus(self): 
        lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76] 
        print("modus Suhu Udara                            : Rp.",st.mode(lembab))
        print("modus Suhu Udara                            : Rp.",st.multimode(lembab))

    def kuartil(self): 
        lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76] 
        kuartil1 = np.quantile(lembab, 0.25) 
        kuartil2 = np.quantile(lembab, 0.5)  
        kuartil3 = np.quantile(lembab, 0.75) 
        print("Kuartil 1 Harga Beras                        : Rp.", kuartil1) 
        print("Kuartil 2 Harga Beras                        : Rp.", kuartil2) 
        print("Kuartil 3 Harga Beras                        : Rp.", kuartil3)


class kov:  
    def judul(self):
        print("="*20,"Kovarian Suhu Udara Dengan kelembaban", "="*20)  
    def kovr(self):
        suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
        lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76]    
        data1 = np.array([suhu, lembab])          
        print("Kovarian suhu udara dengan kelembaban : \n", np.cov(data1)) 
        print() 
        print("Korelasi suhu udara dengan kelembaban : \n", np.corrcoef(data1)) 

cetak = buatsendiri()
cetak.judul()
cetak.data()

cetak1 = suhu()
cetak1.judul()
cetak1.mean()
cetak1.median()
cetak1.modus()
cetak1.deviasi()
cetak1.kuartil()

cetak2 = Kelembaban()
cetak2.judul()
cetak2.mean()
cetak2.median()
cetak2.modus()
cetak2.kuartil()

cetak3 = kov()
cetak3.judul()
cetak3.kovr()