import numpy as np
import statistics as st 
# class pemisah():
#     def pemisah1(self):
#         print()     

# class datageneral():   
#     def judul(self): 
#         print("Kota                                          : Surabaya")  
   
#     def data(self):     
#         suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
#         lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76]  
#         print("Data Suhu Udara 10 hari terakhir              : ",suhu) 
#         print("Data Kelembaban 10 hari terakhir              : ",lembab)

# class suhu():
#     def judul(self):
#         print("="*20, "Menghitung Suhu Udara", "="*20)

#     def mean(self): 
#         suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32]
#         hasil = np.mean(suhu)   
#         print("Mean Suhu                                   : ", float(hasil))  
    
#     def median(self):
#         suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32]
#         hasil = np.median(suhu)
#         print("Median Suhu Udara                           : ", hasil) 
    
#     def modus(self): 
#         suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
#         print("modus Suhu Udara                            : ",st.mode(suhu)) 

#     def deviasi(self): 
#         suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
#         hasil = np.std(suhu) 
#         print("Standar Deviasi Suhu Udara                  : ",round(hasil,2))

#     def kuartil(self): 
#         suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
#         kuartil1 = np.quantile(suhu, 0.25) 
#         kuartil2 = np.quantile(suhu, 0.5)  
#         kuartil3 = np.quantile(suhu, 0.75) 
#         print("Kuartil 1 Suhu Udara                        : ", kuartil1) 
#         print("Kuartil 2 Suhu udara                        : ", kuartil2) 
#         print("Kuartil 3 Suhu Udara                        : ", kuartil3)

# class Kelembaban():   
#     def judul(self):
#         print("="*20, "Menghitung Kelembaban", "="*20)  

#     def mean(self): 
#         lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76]
#         hasil = np.mean(lembab)   
#         print("Mean Kelembaban Udara                        : ", float(hasil))  
    
#     def median(self):
#         lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76]
#         hasil = np.median(lembab)
#         print("Median Kelembaban udara                      : ", hasil) 
    
#     def modus(self): 
#         lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76] 
#         print("modus Kelembaban Udara                       : ",st.mode(lembab))
#     def kuartil(self): 
#         lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76] 
#         kuartil1 = np.quantile(lembab, 0.25) 
#         kuartil2 = np.quantile(lembab, 0.5)  
#         kuartil3 = np.quantile(lembab, 0.75) 
#         print("Kuartil 1 Kelembaban Udara                   : ", kuartil1) 
#         print("Kuartil 2 Kelembaban Udara                   : ", kuartil2) 
#         print("Kuartil 3 Kelembanan Udara                   : ", kuartil3)


# class kov:  
#     def judul(self):
#         print("="*20,"Kovarian Suhu Udara Dengan kelembaban", "="*20)  
#     def kovr(self):
#         suhu = [32, 32, 32, 32, 33, 32, 32, 32, 32, 32] 
#         lembab = [94, 76, 76, 77, 76, 75, 79, 79, 78, 76]    
#         data1 = np.array([suhu, lembab])          
#         print("Kovarian suhu udara dengan kelembaban : \n", np.cov(data1)) 
#         print() 
#         print("Korelasi suhu udara dengan kelembaban : \n", np.corrcoef(data1)) 



# pemisah = pemisah()

# cetak = datageneral()
# cetak.judul()
# cetak.data()

# pemisah.pemisah1()

# cetak1 = suhu()
# cetak1.judul()
# cetak1.mean()
# cetak1.median()
# cetak1.modus()
# cetak1.deviasi()
# cetak1.kuartil()

# pemisah.pemisah1()

# cetak2 = Kelembaban()
# cetak2.judul()
# cetak2.mean()
# cetak2.median()
# cetak2.modus()
# cetak2.kuartil()

# pemisah.pemisah1()

# cetak3 = kov()
# cetak3.judul()
# cetak3.kovr()

karyawan = {
    '0001': {
        'Nama       : Ayu Diac'
        'Jabatan    : Supervisor '
        'No HP      : 0819283940'
        'Alamat     : Bojongsoang'
        },
        '0002' : {
        'Nama       : Dito'
        'Jabatan    : Kasir'
        'No HP      : 08192394902'
        'Alamat     : Buah Batu'
        },
        '0003' : {
        'Nama       : Rahmad'
        'Jabatan    : Kasir'
        'No HP      : 08192456615'
        'Alamat     : Batu Nunggal'
        },
        '0004' : {
        'Nama       : Iqbal'
        'Jabatan    : Operator Gudang'
        'No HP      : 08154646763'
        'Alamat     : Sukabirus'
        },
        '0005' : {
        'Nama       : Jacob'
        'Jabatan    : Operator Gudang'
        'No HP      : 081320349543'
        'Alamat     : Sukapura'
        },
        '0006' : {
        'Nama       : Adipati'
        'Jabatan    : Supir'
        'No HP      : 081219204023'
        'Alamat     : Lembang'
        }
        
print (karyawan, end=" ")