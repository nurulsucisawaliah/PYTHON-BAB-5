from random import randint
angka = randint(0,100)
print('hai...nama saya kembar kembir,saya telah memilih sebuah bilangan bulat secara acak antara 0 sampai dengan 100.ayo tebak!!!')
while angka :
    bil = int(input('tebak angka : '))
    if(bil<angka):
        print('hahaha...tebakan anda terlalu kecil,coba lagi')
    elif(bil>angka):
        print('hmmm...tebakan anda terlalu besar,ayo ditebak lagi')
    else:
        print('yap...bilangan tebakan anda BENAR')
        break

