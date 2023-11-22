#Data Diri
def Datadiri(nama, alamat, gender, umur, hoby) :
 #nama="Fadhlur Rachman Suwandi"
 #alamat="Desa Karang Asem Barat KP. Lanbau RT02 RW10, Kecamatan Citereup, Kabupaten Bogor."
 #gender="Laki-Laki"
 #umur=20
# hoby= "Bersepeda"
  print("nama:", nama)
  print("alamat:", alamat)
  print("gender:", gender)
  print("umur:", umur)
  print("hoby:", hoby)

Datadiri("Fadhlur rachman", "Desa Karang Asem Barat KP. Lanbau RT02 RW10, Kecamatan Citereup, Kabupaten Bogor.", "Laki-Laki", "20", "Bersepeda")

#Kelulusan Nilai

def kkm(nilai):
 if nilai <= 60:
    print ( "gagal")
 elif 61 <= nilai <= 70 :
    print ("baik")
 elif 71 <= nilai <= 80 :
    print ("sangat baik")
 elif 81 <= nilai <= 100 :
    print ("istimewa")
 else:
    print ("tidak ada")
kkm()

#bilangan ganjil

def ganjil(angka) :
   for i in range(angka) :
      if i % 2 != 0:
         print(i)
ganjil(100)

