kodeKaryawan = int(input('Masukkan kode karyawan      :'))
namaKaryawan = input('Masukkan nama karyawan      :')
golongan = input('Masukkan golongan           :')
print('==========================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------')
print('nama Karyawan               :' + namaKaryawan + '(kode Karyawan :' + str(kodeKaryawan) + ')')
print('Golongan                    :' + golongan)
print('-----------------------------------------')

if(golongan == 'A'):
    gajiPokok = 10000000
    potongan = 2.5
    jumlahPotongan = 2.5/ 100 * 10000000
    gajiBersih = 10000000 - jumlahPotongan

elif(golongan == 'B'):
    gajiPokok = 8500000
    potongan = 2.0
    jumlahPotongan = 2./ 100 * 8500000
    gajiBersih = 8500000 - jumlahPotongan

elif(golongan == 'C'):
    gajiPokok = 7000000
    potongan = 1.5
    jumlahPotongan = 1.5/ 100 * 7000000
    gajiBersih = 10000000 - jumlahPotongan

elif(golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahPotongan = 1.0 /100 * 5500000
    GajiBersih = 5500000 - jumlahPotongan

print('gajiPokok                   : Rp' + str(gajiPokok))
print('potongan (' + str(potongan) + '%)             : Rp' + str(jumlahPotongan))
print('-------------------------------------------')
print('gajiBersih                  : Rp' + str(gajiBersih))
