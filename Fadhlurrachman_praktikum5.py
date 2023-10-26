motor = ["jupiter z","motor","115","biru","dua"]
motor.append("17000000")
motor.append("bebek")
motor.insert(2,"yamaha")
print(motor)
#tugas 2
luas = input ("PILIH OPERASI : \n1.menghitung luas persegi \n 2.hitung luas lingkaran \n 3.hitung luas segitiga \n pilihan:")
match luas:
    case"1" : 
        sisi = int ("masukan nilai sisi: ")
        luas = sisi*sisi
        print(luas)
    case "2" :
        jari_jari = int(input("masukkan nilai jari-jari: "))
        luas = 3.14*jari_jari*jari_jari
        print(luas)
    case "3":
        alas = int(input("masukkan nilai alas : "))
        tinggi = int(input("masukkan nilai tinggi : "))
    case _:
        
        print("eweuh")

