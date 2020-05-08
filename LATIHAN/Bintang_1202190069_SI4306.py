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

# print("Data Matriks A : ")
# for i in range(0,len(mtx)):     
#     for j in range(0,len(mtx[0])):        
#         print(mtx[i][j],end=" ")
#     print("\t")

# print(" ")

# print("Data Matriks B : ")
# for i in range(0,len(mtx2)):     
#     for j in range(0,len(mtx2[0])):   
#         print(mtx2[i][j],end=" ")
#     print("\t")

# print(" ")

# print("Data matriks C = Matriks A + Matriks B : ")
# pemisah2()
# for i in range(0,len(mtx)):
#     for j in range(0, len(mtx[0])):
#         print(mtx[i][j] + mtx2[i][j], end=" "),
#     print("\t")


def pertambahan(a,b):
    c = a+b
    return c

per = int(input("Masukan nilai pertama" ))
ked = int(input("masukan nilai kedua" ))
print(pertambahan(per,ked))