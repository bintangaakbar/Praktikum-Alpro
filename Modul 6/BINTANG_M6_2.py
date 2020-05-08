l=[]       #untuk menambahkan list sesuai inputan user
try:
    jmlh= int(input("Masukkan Jumlah Sayur yang ingin diinput : "))     #user menginput jumlah sayur
    for x in range (jmlh):  #untuk x di jangkauan jumlah inputan user
        l.append(input("Masukkan sayur ke -"+str(x)+": "))   #berapa banyak sayur yg ingin di input oleh user 
    berapa = int(input('Anda ingin menampilkan sayur urutan ke- berapa? : '))    # memberi pilihan pada user mana sayur yg ingin ditampilkan
    print('Sayur pada urutan ke- '+str(berapa)+' adalah '+str(l[berapa]))       #
except IndexError:  #jika dilist tidak ada sayur yg dimaksud maka program mencetak kalimat dibawah
    print('Sayur tidak tersedia pada urutan tersebut')