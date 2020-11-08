print('Hai...nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
tebak=int(input('Tebakan Anda : '))
poinsalah=0
while True:
    if(tebak<10):
        print('Hehehe.....Bilangan tebakan anda terlalu kecil')
        tebak=int(input('Tebakan Anda : '))
        poinsalah+=2

    elif(tebak>10):
        print('wah.....Bilangan tebakan anda terlalu besar')
        tebak=int(input('Tebakan Anda : '))
        poinsalah+=2

    elif(tebak==10):
        print('cieee...Bilangan tebakan anda benar')
        score=100-poinsalah
        print('Score anda : ' + str(score))
        break
