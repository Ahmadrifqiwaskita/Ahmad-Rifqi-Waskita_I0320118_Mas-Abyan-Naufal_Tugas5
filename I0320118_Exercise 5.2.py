#penggunaan if untuk dua kasus
#input bilangan\

bilangan = int(input('Masukkan bilangan bulat: '))

if bilangan % 2 == 0:
    print('%d adalah bilangan genap' % bilangan)
else:
    print('%d adalah bilangan ganjil' % bilangan)

print()        