def yang_lulus(hasil_akhir) :
    yang_lulus =[]
    for yang in hasil_akhir :
        if yang ['nilai'] >  65 :
            yang_lulus.append(yang['nama'])
    
    return yang_lulus

hasil_akhir= [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]

print (yang_lulus(hasil_akhir))

#Nomer 2 

def balik(buah) :
    hasil=[]

    for i in range(len(buah)) :
        hasil.append(buah[len(buah)-1 -i])
    return hasil

print(balik(["pepaya", "mangga", "pisang", "durian", "jambu"]))

#nomer 3

def duplikat(buah2):
    hasil=[]

    for buah in buah2 :
        hasil.append(buah)
        hasil.append(buah)
    return hasil

print(duplikat(["pepaya", "mangga", "pisang", "durian", "jambu"]))

#nomer 4

def konsonan(nama) :
    konsonan= "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    hasil = ""

    for karakter in nama :
        if karakter in konsonan :
            hasil += karakter
    return hasil

print(konsonan("Nurul Fikri"))