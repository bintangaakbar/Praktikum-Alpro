x = 0
def hitung(batas1,batas2): 
    for a in range(batas1 + 1,batas2 + 1): 
        if a > 1: 
            for b in range(2,a): 
                if (a % b) == 0: 
                    break
            else:
                global x
                x = x + 1 

batas1 = int(input('Masukan angka batas bawah : '))
batas2 = int(input('Masukan angka batas atas : ')) 
hitung(batas1,batas2) 
print("Jumlah bilangan prima dari",batas1,"sampai dengan",batas2,"adalah ",x)