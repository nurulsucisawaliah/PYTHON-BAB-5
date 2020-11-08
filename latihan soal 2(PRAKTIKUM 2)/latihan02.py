#modifikasi kode program nomor 1
jumlah = 0
for bil in range (0,100):
    bilanganGanjil = bil + 1
    if bilanganGanjil %2 == 1:
        jumlah = jumlah + 1
        print(bilanganGanjil)
print('Banyaknya bilangan ganjil : ' + str(jumlah))
