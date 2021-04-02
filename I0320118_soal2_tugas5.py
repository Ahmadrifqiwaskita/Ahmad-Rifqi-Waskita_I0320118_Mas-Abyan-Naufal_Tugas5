#program grading nilai

nama = input('Masukkan nama: ')
nilai = float(input('Masukkan nilai: '))

template = '"Halo,'+str(nama) + str('!') + ' Nilai anda setelah di konversi adalah '

if nilai >= 85 and nilai <= 100:
    print (template + 'A"')
if nilai >= 80 and nilai <= 84:
    print(template + 'A-"')
if nilai >= 75 and nilai <= 79:
    print(template + 'B+"')
if nilai >= 70 and nilai <= 74:
    print(template + 'B"')
if nilai >= 65 and nilai <= 69:
    print(template + 'C+"')
if nilai >= 60 and nilai <= 64:
    print(template + 'C"')
if nilai >= 0 and nilai <= 59:
    print(template + 'E"')
else:
    pass





