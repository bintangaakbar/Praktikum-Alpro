kilasUmurAnak={     
    0:[21,15], 
    1:[17,14], 
    2:[30,21,5], 
    3:[25,23,21,19], 
    4:[17], 
    5:[6,3], 
    6:[1,12] 
}
#list umur anak
suspectUmurAtas=int(input("Suspect anak berumur (batas atas)\t: "))         #user menginput batas atas
suspectUmurBawah=int(input("Suspect anak berumur (batas bawah)\t: "))       #user menginput batas bawah
suspectUrutan=int(input("Suspect anak lahiran ke - "))-1                    #user menginput anak lahiran keberapa yg ingin dipilih
print()
def miripPolisi(keluarga):  #fungsi baru 
    global suspectUrutan,suspectUmurBawah,suspectUmurAtas,kilasUmurAnak     #memanggil inputan kedalam fungsi dengan global
    try: 
        if kilasUmurAnak[keluarga][suspectUrutan]<suspectUmurAtas and kilasUmurAnak[keluarga][suspectUrutan]>suspectUmurBawah: 
            print("di keluarga ke - ",int(keluarga+1),"anak lahiran ke - ",int(suspectUrutan+1),"berumur : ",kilasUmurAnak[keluarga][suspectUrutan])  #jika inputan sesuai list maka akan mencetak kalimat disamping
        else:
            print("di keluarga ke - ",int(keluarga+1),"anak lahiran ke - ",int(suspectUrutan+1),"tidak memenuhi kriteria tersangka")    #jika inputan ada dilist tapi tidak sesuai maka akan mencetak kalimat disamping
    except: 
        print("[list index out of range] Pemilihan data keluarga untuk calon tersangka salah. Jumlah anak dalam keluarga ke - ",int(keluarga+1),"tidak sesuai.")  #jika inputan tidak ada dilist maka akan mencetak ini
    
for keluarga in range(len(kilasUmurAnak)): # untuk fungsi keluarga dijangkauan list umur anak
    miripPolisi(keluarga)   #mencetak fungsi miripPolisi