c = 0                                                                        #dimulai dari nol
def batas():                                                                 #Membuat Fungsi untuk dihitung
    for i in range(1,a + 1):                                                 #untuk memulai dari angka 1
        if i > 1:                                                            #Jika i lebih dari 1
            for x in range(2,i):                                             #jika i lebih dari 1 maka masuk ke x
                if(i % x) == 0:                                              #jika i dan x sama dengan 0 maka break
                    break                                                    #jika hasil tidak sama maka dibreak
            else:                                                            #Jika tidak maka count akan menambah 1
                global c                                                     #Mendeklarasikan variable diluar fungsi
                c += 1                                                       #hitungan ditambah dengan 1

a = int(input("Masukan angka batas : "))                                     #user menginput batas
batas()                                                                      #meminta hasil yang dikerjakan difungsi batas
print("Bilangan prima mulai dari 1 sampai", a, "ada sebanyak : ", c)         #mencetak hasil