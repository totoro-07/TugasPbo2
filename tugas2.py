#membuat kelas mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan

    def tampilkan_info(self):
        print("\nNama:", self.__nama)
        print("NIM:", self.__nim)
        print("Jurusan:", self.__jurusan.get_nama_jurusan())

#membuat kelas jurusan
class Jurusan:
    def __init__(self, nama_jurusan):
        self.__nama_jurusan = nama_jurusan
        self.__daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.__daftar_mahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("\nDaftar Mahasiswa", self.__nama_jurusan)
        for mahasiswa in self.__daftar_mahasiswa:
            mahasiswa.tampilkan_info()

    def get_nama_jurusan(self):
        return self.__nama_jurusan

#membuat kelas universitas
class Universitas:
    def __init__(self, nama_universitas):
        self.__nama_universitas = nama_universitas
        self.__daftar_jurusan = []

    def tambah_jurusan(self, jurusan):
        self.__daftar_jurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di", self.__nama_universitas)
        for jurusan in self.__daftar_jurusan:
            print("- Jurusan:", jurusan.get_nama_jurusan())



# Membuat objek Jurusan
jurusan_1 = Jurusan("Informatika")
jurusan_2 = Jurusan("Teknik Sipil")

# Membuat objek Mahasiswa dengan nama dan nim 
mahasiswa1 = Mahasiswa("Ahmad Radesta", "G1A022086", jurusan_1)
jurusan_1.tambah_mahasiswa(mahasiswa1)

mahasiswa2 = Mahasiswa("Fadlan", "G1A022051", jurusan_1)
jurusan_1.tambah_mahasiswa(mahasiswa2)

mahasiswa3 = Mahasiswa("Nando", "G1B022051", jurusan_2)
jurusan_2.tambah_mahasiswa(mahasiswa3)

# Membuat objek Universitas dengan nama "XYZ University" dan menambahkan Jurusan Informatika dan Jurusan teknik sipil ke dalamnya
universitas_xyz = Universitas("XYZ University")
universitas_xyz.tambah_jurusan(jurusan_1)
universitas_xyz.tambah_jurusan(jurusan_2)

# Menampilkan daftar jurusan di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Informatika di Universitas XYZ
jurusan_1.tampilkan_daftar_mahasiswa()
jurusan_2.tampilkan_daftar_mahasiswa()