# keliling & luas segitiga

# atribut = alas, tinggi
# operasi = ()alas x tinggi) / 2
def segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas


def kubus(sisi):
    luas = 6 * sisi ** 2
    volume = sisi * sisi * sisi
    print(f"luas kubus = {luas}, volume kubus = {volume}")


def balok(p, l, t):
    luas = 2*p*l + 2*p*t + 2*l*t
    volume = p*l*l
    print(f"luas balok = {luas}, volume balok = {volume}")


def limas_segi_empat(alas, tinggi):
    luas = segitiga(alas, tinggi) + segitiga(alas, tinggi) + \
        segitiga(alas, tinggi) + segitiga(alas, tinggi) + alas * alas
    volume = (alas * alas) * tinggi / 3
    print(f"luas limas segi empat = {luas}, volume lima segi empat = {int(volume)}")


def tabung(jari, tinggi):
    luas = 3.14 * jari * tinggi
    volume = 3.14 * jari * jari * tinggi
    print(f"luas tabung = {luas}, volume tabung = {volume}")


def kerucut(jari, sisi, tinggi):
    luas = 3.14 * jari * sisi
    volume = 3.14 * jari * jari * tinggi / 3
    print(f"luas kerucut = {luas}, volume kerucut = {volume}")


def bola(jari):
    luas = 4 * 3.14 * jari * jari
    volume = 4 * 4.14 * jari ** 3 / 3
    print(f"luas bola = {luas}, volume bola = {volume}")


def limas_segitiga(alas, tinggi):
    luas = segitiga(alas, tinggi) + segitiga(alas, tinggi) + \
        segitiga(alas, tinggi) + segitiga(alas, tinggi)
    volume = segitiga(alas, tinggi) * tinggi / 6
    print(f"luas limas segitiga = {luas}, volume limas segitiga = {volume}")


def prisma_segitiga(sisi1, sisi2, sisi3, tinggi):
    luas = (sisi1 + sisi2 + sisi3) * tinggi
    volume = segitiga(sisi2, tinggi) * tinggi / 2
    print(f"luas prisma segitiga = {luas}, volume prisma segitiga = {volume}")


sisi_kubus = 5
panjang = 5
lebar = 4
tinggi = 6
jari = 5

kubus(sisi_kubus)
balok(panjang, lebar, tinggi)
limas_segi_empat(panjang, tinggi)
tabung(jari, tinggi)
kerucut(jari, panjang, tinggi)
bola(jari)
limas_segitiga(panjang, tinggi)
prisma_segitiga(panjang, lebar, jari, tinggi)
