sisi = [19, 21, 33, 17, 23, 51, 47, 41, 31, 11, 13] #variable dari sisi yang ingin dijumlahkan
print("Berikut sisi-nya sesuai data soal : ", sisi) #Mencetak isi dari variable sisi
hasil = map(lambda args : 6 * (args**2),sisi)  #menggunakan fungsi secara anonymous

print("Hasil luas permukaan kubus masing-masing sisi yaitu : ", (list(hasil))) #mencetak hasil dari variable isi yang telah dijumlahkan difungsi lambda





# data =[[1,2,3],[4,5.6],[7,8,9]]

# for baris in range(0,3):
#     for kolom in range(0,3):
#         print("Data ke ["+str(baris)+"]"+"["+str(kolom)+"] = ", data[baris][kolom])


# data = [[1,2,3],[4,5,6],[7,8,9]]

# for baris in range (0,3):
#     for kolom in range (0,3):
#         print("Data ke ["+str(baris)+"]"+"["+str(kolom)+"]=",data[baris][kolom])