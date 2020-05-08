def judul():        #fungsi mencetak judul
    print("\tProgram Melihat Lulus atau Tidaknya anda")
def pemisah():
    print()         #fungsi pemisah
judul()             #mencetak perintah judul
pemisah()           #mencetak fungsi dari pemisah
try:
    a=int(input("\tMasukkan Total Nilai Mata Kuliah anda  :   "))       #user menginput nilai matkul
except ValueError:              #jika nilai error maka mencetak ERROR
    print("\tERROR Gan")        
else:
    if a < 40:          #menggunakan percabangan untuk melihat nilai yang user input
        print("\tanda gagal")
    elif 41 <= a <=50:
        print("\tAnda lulus dan boleh mengulang untuk perbaikan")
    else:
        print("\tAnda lulus")
finally:                #jika program error maka akan tetap dieksekusi dengan kalimat penyemangat
    pemisah()
    print("""\tTingkatkan belajar anda!
    \tSemangat!
    \tGanbate!
    """)