class Kubus:        #membuat class untuk menghitung kubus
    def __init__(self,s): #inisiasi sendiri
        self.sisi = s

    def volume(self):       #fungsi untuk menghitung luas volume
        volume = self.sisi**3 
        print("\tVolume Kubus:",volume,"cm^3") 

    def permukaan(self):  #fungsi untuk menghitung luas permukaan
        permukaan = 6*(self.sisi**2) 
        print("\tLuas Kubus:",permukaan,"cm^2") 

    def keliling(self): #fungsi untuk menghitung luas keliling
        keliling = self.sisi * 12 
        print("\tKeliling Kubus:",keliling,"cm") 

def pemisah():  #fungsi untuk pemisah
    print()

def main(): #membuat fungsi untuk dicetak
    print("\tKubus 1") 
    kubus1=Kubus(5) #menginput nilai dari luas kubus
    kubus1.volume() #menghitung dari fungsi volume
    kubus1.permukaan() #menghitung dari fungsi luas permukaan
    kubus1.keliling()#menghitung dari fungsi luas keliling

    pemisah()

    print("\tKubus 2") 
    kubus2=Kubus(10) #menginput nilai dari luas kubus
    kubus2.volume() #menghitung dari fungsi volume
    kubus2.permukaan() #menghitung dari fungsi luas permukaan
    kubus2.keliling() #menghitung dari fungsi luas keliling

main() #menyetak dari fungsi main







# import numpy as np
# def pemisah():
#     print("="*16)

# def pemisah2():
#     print("="*40)

# mtx = [
#     [7, 6, 9, 3],
#     [5, 7, 4, 2],
#     [7, 9, 2, 2],
# ]

# mtx2 = [
#     [3, 6, 8, 6],
#     [7, 3, 9, 1],
#     [8, 5, 9, 4],
# ]

# list1 = np.array(mtx)
# list2 = np.array(mtx2)

# print(list1)
# pemisah()
# print(list2)
# pemisah()

# print("Data matriks C = Matriks A + Matriks B : ")
# pemisah2()
# for i in range(0,len(mtx)):
#     for j in range(0, len(mtx[0])):
#         print(mtx[i][j] + mtx2[i][j], end=" "),
#     print("\t")