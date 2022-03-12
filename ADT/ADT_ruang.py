def segitiga(alas, tinggi):

    luas = alas * tinggi / 2
    return luas


def input_nilai(variabel):
    return int(input(variabel))


def pembatas():
    print(40 * '=')


def kubus():
    print('KUBUS')
    sisi = input_nilai('masukan nilai sisi: ')
    luas = 6 * sisi ** 2
    volume = sisi * sisi * sisi
    print(f"luas kubus = {luas}, volume kubus = {volume}")
    pembatas()


def balok():
    print('BALOK')
    p = input_nilai('masukan nilai panjang: ')
    l = input_nilai('masukan nilai lebar: ')
    t = input_nilai('masukan nilai tinggi: ')

    luas = 2*p*l + 2*p*t + 2*l*t
    volume = p*l*l
    print(f"luas balok = {luas}, volume balok = {volume}")
    pembatas()


def limas_segi_empat():
    print('LIMAS SEGI EMPAT')

    alas = input_nilai('masukan alas: ')
    tinggi = input_nilai('masukan tinggi: ')

    luas = segitiga(alas, tinggi) + segitiga(alas, tinggi) + \
        segitiga(alas, tinggi) + segitiga(alas, tinggi) + alas * alas
    volume = (alas * alas) * tinggi / 3
    print(
        f"luas limas segi empat = {luas}, volume lima segi empat = {int(volume)}")

    pembatas()


def tabung():
    print('TABUNG')

    jari = input_nilai('masukan nilai jari: ')
    tinggi = input_nilai('masukan tinggi: ')

    luas = 3.14 * jari * tinggi
    volume = 3.14 * jari * jari * tinggi
    print(f"luas tabung = {luas}, volume tabung = {volume}")

    pembatas()


def kerucut():
    print('KERUCUT')

    jari = input_nilai('masukan nilai jari: ')
    sisi = input_nilai('masukan nilai sisi: ')
    tinggi = input_nilai('masukan nilai tinggi: ')

    luas = 3.14 * jari * sisi
    volume = 3.14 * jari * jari * tinggi / 3
    print(f"luas kerucut = {luas}, volume kerucut = {volume}")

    pembatas()


def bola():
    print('BOLA')

    jari = input_nilai('masukan nilai jari: ')

    luas = 4 * 3.14 * jari * jari
    volume = 4 * 4.14 * jari ** 3 / 3
    print(f"luas bola = {luas}, volume bola = {volume}")

    pembatas()


def limas_segitiga():
    print('LIMAS SEGITIGA')
    alas = input_nilai('masukan alas: ')
    tinggi = input_nilai('masukan tinggi: ')

    luas = segitiga(alas, tinggi) + segitiga(alas, tinggi) + \
        segitiga(alas, tinggi) + segitiga(alas, tinggi)
    volume = segitiga(alas, tinggi) * tinggi / 6
    print(f"luas limas segitiga = {luas}, volume limas segitiga = {volume}")

    pembatas()


def prisma_segitiga():
    print('PRISMA SEGITIGA')

    s1 = input_nilai('masukan nilai sisi 1: ')
    s2 = input_nilai('masukan nilai sisi 2: ')
    s3 = input_nilai('masukan nilai sisi 3: ')
    tinggi = input_nilai('masukan nilai tinggi: ')

    luas = (s1 + s2 + s3) * tinggi
    volume = segitiga(s1, tinggi) * tinggi / 2
    print(f"luas prisma segitiga = {luas}, volume prisma segitiga = {volume}")

    pembatas()


kubus()
balok()
limas_segi_empat()
tabung()
kerucut()
bola()
limas_segitiga()
prisma_segitiga()
