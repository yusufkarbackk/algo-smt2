def input_nilai(variabel):
    return int(input(variabel))


def pembatas():
    print(40 * '=')


def persegi():
    sisi = input_nilai('masukan nilai sisi: ')
    keliling = 4 * sisi
    luas = sisi * sisi
    print(f"keliling persegi = {keliling}, luas persegi = {luas}")
    pembatas()


def persegi_panjang():
    p = input_nilai('masukan nilai panjang: ')
    l = input_nilai('masukan nilai lebar: ')
    keliling = (2 * p) + (2 * l)
    luas = p * l
    print(
        f"keliling persegi panjang = {keliling}, luas persegi panjang = {luas}")
    pembatas()


def jajar_genjang():
    s1 = input_nilai('masukan nilai sisi 1: ')
    s2 = input_nilai('masukan nilai sisi 2: ')
    s3 = input_nilai('masukan nilai siis 3: ')
    s4 = input_nilai('masukan nilai sisi 4: ')
    tinggi = input_nilai('masukan nilai tinggi: ')

    keliling = s1 + s2 + s3 + s4
    luas = s1 * tinggi
    print(f"keliling jajar genjang = {keliling}, luas jajar genjang = {luas}")

    pembatas()


def segitiga():
    s1 = input_nilai('masukan nilai sisi 1: ')
    s2 = input_nilai('masukan nilai sisi 2: ')
    s3 = input_nilai('masukan nilai sisi 3: ')
    tinggi = input_nilai('masukan nilai tinggi: ')

    keliling = s1 + s2 + s3
    luas = s1 * tinggi / 2
    print(f"keliling segitiga = {keliling}, luas segitiga = {luas}")

    pembatas()


def belah_ketupat():
    s1 = input_nilai('masukan nilai sisi 1: ')
    s2 = input_nilai('masukan nilai sisi 2: ')
    s3 = input_nilai('masukan nilai sisi 3: ')
    s4 = input_nilai('masukan nilai sisi 4: ')
    d1 = input_nilai('masukan diagonal 1: ')
    d2 = input_nilai('masukan diagonal 2: ')

    keliling = s1 + s2 + s3 + s4
    luas = d1 * d2 / 2
    print(f"keliling belah_ketupat = {keliling}, luas belah_ketupat = {luas}")

    pembatas()


def layang_layang():
    s1 = input_nilai('masukan nilai sisi 1: ')
    s2 = input_nilai('masukan nilai sisi 2: ')
    s3 = input_nilai('masukan nilai sisi 3: ')
    s4 = input_nilai('masukan nilai sisi 4: ')
    d1 = input_nilai('masukan diagonal 1: ')
    d2 = input_nilai('masukan diagonal 2: ')

    keliling = s1 + s2 + s3 + s4
    luas = d1 * d2 / 2
    print(f"keliling layangan = {keliling}, luas layangan = {luas}")

    pembatas()


def trapesium():
    s1 = input_nilai('masukan nilai sisi 1: ')
    s2 = input_nilai('masukan nilai sisi 2: ')
    s3 = input_nilai('masukan nilai sisi 3: ')
    s4 = input_nilai('masukan nilai sisi 4: ')
    tinggi = input_nilai('masukan nilai tinggi: ')

    keliling = s1 + s2 + s3 + s4
    luas = ((s1 + s2) / 2) * tinggi
    print(f"keliling trapesium = {keliling}, luas trapesium = {luas}")

    pembatas()


def lingkaran():
    jari = input_nilai('masukan nilai jari: ')

    keliling = 2 * 3.14 * jari
    luas = 3.14 * jari * jari
    print(f"keliling lingkaran = {keliling}, luas lingkaran = {luas}")

    pembatas()


persegi()
persegi_panjang()
jajar_genjang()
segitiga()
belah_ketupat()
layang_layang()
trapesium()
lingkaran()
