class Buku:
  def __init__(self, judul, penulis="Tidak Diketahui", tahun_terbit=None):
  
    self.judul = judul
    self.penulis = penulis
    self.tahun_terbit = tahun_terbit
    
  def info(self):
     print(f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}")
      
buku1 = Buku("Pemrograman Berorientasi Objek", "Rian", 2026)
buku2 = Buku("Struktur Data dan Algoritma", "Jeprianto", 2021)
buku3 = Buku("Informatika", tahun_terbit=2020)
      
buku1.info()
buku2.info()
buku3.info()