# program penyapa pengunjung hotel

nama = input('Masukkan nama: ')
jenis_kelamin = input('Masukkan jenis kelamin (pria/wanita): ')
template = '"Selamat datang' + ','
template2 = str(nama) + str('!"')

if jenis_kelamin == 'pria':
    print(template + 'Tuan ' + template2)
else:
    print(template + 'Nyonya ' + template2)