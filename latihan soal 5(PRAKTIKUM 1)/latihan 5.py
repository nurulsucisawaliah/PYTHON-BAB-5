kodeKaryawan = int(input('Masukkan kode karyawan :'))
namaKaryawan = input('Masukkan nama karyawan :')
golongan = input('Masukkan golongan      :')
status = input('Masukkan status        :')
if(status == 'sudah menikah') :
    jumlahAnak = int(input('Masukkan Jumlah Anak :'))
    tunjanganMenikah = 10 / 100
    tunjanganAnak = 5 / 100 * jumlahAnak
    statusMenikah = 'Sudah Menikah'

else:
    jumlahAnak = 0
    tunjanganMenikah = 0
    tunjanganAnak = 0
    statusMenikah = 'Belum Menikah'
    
print('================================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('------------------------------------------------')
print('Nama Karyawan          :' + namaKaryawan + '(Kode Karyawan :' + str(kodeKaryawan) + ')')
print('Golongan               :' + golongan)
print('Status Menikah         :' + statusMenikah)
print('Jumlah Anak            :' + str(jumlahAnak))
print('------------------------------------------------')

if(golongan == 'A'):
    gajiPokok =10000000
    potongan =2.5
    jumlahtunjanganMenikah =10000000 * tunjanganMenikah
    jumlahtunjanganAnak =10000000 * tunjanganAnak
    gajiKotor =10000000 + jumlahtunjanganMenikah + jumlahtunjanganAnak
    jumlahPotongan =2.5 / 100 * gajiKotor
    gajiBersih =gajiKotor - jumlahPotongan

elif(golongan == 'B'):
    gajiPokok =8500000
    potongan =2.0
    jumlahtunjanganMenikah =8500000 * tunjanganMenikah
    jumlahtunjanganAnak =8500000 * tunjanganAnak
    gajiKotor =8500000 + jumlahtunjanganMenikah + jumlahtunjanganAnak
    jumlahPotongan =2. / 100 * gajiKotor
    gajiBersih =gajiKotor - jumlahPotongan

elif(golongan == 'C'):
    gajiPokok =7000000
    potongan =1.5
    jumlahtunjanganMenikah =7000000 * tunjanganMenikah
    jumlahtunjanganAnak =7000000 * tunjanganAnak
    gajiKotor =10000000 + jumlahtunjanganMenikah + jumlahtunjanganAnak
    jumlahPotongan =1.5 / 100 * gajiKotor
    gajiBersih =gajiKotor - jumlahPotongan

elif(golongan == 'D'):
    gajiPokok =5500000
    potongan =1.0
    jumlahtunjanganMenikah =5500000 * tunjanganMenikah
    jumlahtunjanganAnak =5500000 * tunjanganAnak
    gajiKotor =5500000 + jumlahtunjanganMenikah + jumlahtunjanganAnak
    jumlahPotongan =1.0 / 100 * gajiKotor
    gajiBersih =gajiKotor - jumlahPotongan

print('gajiPokok              :Rp' + str(gajiPokok))
print('tunjanganMenikah       :Rp' + str(jumlahtunjanganMenikah))
print('tunjanganAnak          :Rp' + str(jumlahtunjanganAnak))
print('------------------------------------------------')
print('gajiKotor              :Rp' + str(gajiKotor))
print('potongan (' + str(potongan) + '%)        :Rp' + str(jumlahPotongan))
print('------------------------------------------------')
print('gajiBersih             :Rp' + str(gajiBersih))
