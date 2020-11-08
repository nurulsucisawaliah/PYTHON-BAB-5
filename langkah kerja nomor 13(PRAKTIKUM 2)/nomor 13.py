#modifikasi kode program nomor 11
from random import randint
banyak = 0
while True:
    bil = randint(0,10)
    print(bil)
    banyak = banyak + 1
    if bil == 5:
        break
print('banyak perulangan : ' + str(banyak))
