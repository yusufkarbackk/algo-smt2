def persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    print(f"keliling persegi = {keliling}, luas persegi = {luas}")


def persegi_panjang(p, l):
    keliling = (2 * p) + (2 * l)
    luas = p * l
    print(
        f"keliling persegi panjang = {keliling}, luas persegi panjang = {luas}")


def jajar_genjang(s1, s2, s3, s4, tinggi):
    keliling = s1 + s2 + s3 + s4
    luas = s1 * tinggi
    print(f"keliling jajar genjang = {keliling}, luas jajar genjang = {luas}")


def segitiga(s1, s2, s3, tinggi):
    keliling = s1 + s2 + s3
    luas = s1 * tinggi / 2
    print(f"keliling segitiga = {keliling}, luas segitiga = {luas}")


def belah_ketupat(s1, s2, s3, s4, d1, d2):
    keliling = s1 + s2 + s3 + s4
    luas = d1 * d2 / 2
    print(f"keliling belah_ketupat = {keliling}, luas belah_ketupat = {luas}")


def layang_layang(s1, s2, s3, s4, d1, d2):
    keliling = s1 + s2 + s3 + s4
    luas = d1 * d2 / 2
    print(f"keliling layangan = {keliling}, luas layangan = {luas}")


def trapesium(s1, s2, s3, s4, tinggi):
    keliling = s1 + s2 + s3 + s4
    luas = ((s1 + s2) / 2) * tinggi
    print(f"keliling trapesium = {keliling}, luas trapesium = {luas}")


def lingkaran(jari):
    keliling = 2 * 3.14 * jari
    luas = 3.14 * jari * jari
    print(f"keliling lingkaran = {keliling}, luas lingkaran = {luas}")

s1 = 5
s2 = 7 
s3 = 9
s4 = 3
p = 9
l = 6
jari = 12