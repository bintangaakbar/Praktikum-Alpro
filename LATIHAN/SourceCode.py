nilai = 10

if nilai == 75:
    print ("nilai anda adalah", nilai)

if nilai is 60:
    print ("nilai anda adalah", nilai)

if nilai is not 60:
    print("nilai anda bukan", nilai)

print (50*"-")

if 80 <= nilai <= 100:
    print("maka nilai anda A")
elif 70 <= nilai <= 80:
    print ("maka nilai anda B")
elif 60 <= nilai <=70:
    print("maka nilai anda C")
elif 50 <= nilai <= 60:
    print ("maka nilai anda D lakukan perbaikan")
else:
    print("maaaf anda tidak lulus matkul ini")

print(50*"`")
print("operator logika untuk list dan string")
print(" ")

gorengan = ("bakwan", "cireng", "molen", "tahu")
beli = "cireng"

if beli in gorengan:
    print('Mamang bilang, ya saya jual', beli, " ")

else: 
    print ("saya tidak jual", beli,)




################################################

    print (">>> \* ANGKA GANJIL *\ <<<")
print("\t -------------")

angka = int(input("masukkan angka anda ="))

if angka % 2 == 1:
    print ("angka", angka, "adalah angka ganjil")

angka2 = int(input("inputkan angka anda"))

if angka2 % 2 == 0:
    print("angka", angka2, "adalah angka genap")


    ####################################
    print (">>> \* SPEED LIMIT *\ <<<")
print("\t ================")

speed = int(input ("massukan speed anda"))

if speed > 70:
    print("License Suspended")
else:
    print("OK.")




    ########################################
print ("---- CEK BILANGAN ----")

bilangan =int(input ("Masukkan Bilangan :"))
x = 47
if bilangan < x:
    print(bilangan, "Kurang dari", x)

elif bilangan > x:
    print(bilangan, "lebih dari", x)

else:
    print(bilangan, "sama dengan", x)