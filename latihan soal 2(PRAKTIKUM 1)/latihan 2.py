bahasaindonesia =int(input('Nilai Bahasa Indonesia :'))
ipa             =int(input('Nilai ipa              :'))
matematika      =int(input('Nilai Matematika       :'))
if((bahasaindonesia >=0 and bahasaindonesia <=100)) and ((ipa>= 0 and ipa <=100)) and ((matematika >=0 and matematika <=100)):
       if(bahasaindonesia >=60) and (ipa>=60)and (matematika >=70):
              statusKelulusan = 'Lulus'
       else:
              statusKelulusan = 'Tidak Lulus'

       print('statuskelulusan  : ' +statusKelulusan)
else:
       print('maaf input anda tidak valid')

