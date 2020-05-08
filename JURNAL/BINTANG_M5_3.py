class mhs():
    def __init__(self,urutan,nama,nim,kelas,alamat):
        self.urutan = urutan
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.alamat = alamat
    def cetak(self):
        print("Mahasiswa",self.urutan)
        print('Nama: ',self.nama)
        print('NIM: ',self.nim)
        print('Kelas: ',self.kelas)
        print('Alamat: ',self.alamat)
        print('\n')

no1 = mhs(1,'Dono',12021901010,'SI-20-03','Bandung')
no2 = mhs(2,'Kasino',12021902020,'SI-20-01','Sumedang')
no3 = mhs(3,'Indro',12021905050,'SI-20-04','Ponorogo')

no1.cetak()
no2.cetak()
no3.cetak()