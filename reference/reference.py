def kuadrat():
    print("Kuadrat")
    number = 5
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")

    number = number * number
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")


def penjumlahan():
    print("Penjumlahan")

    number = 5
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")

    number = number + 10
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")


def pengurangan():
    print("Pengurangan")

    number = 20
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")

    number = number - 16
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")


def perkalian():
    print("Perkalian")

    number = 50
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")

    number = number * 2
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")


def pembagian():
    print("Pembagian")

    number = 100
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")

    number = number / 4
    number2 = number
    print(f"number: {number}, alamat: {hex(id(number))}")
    print(f"number2: {number2}, alamat: {hex(id(number2))}")


kuadrat()
print("\n")
penjumlahan()
print("\n")
pengurangan()
print("\n")
perkalian()
print("\n")
pembagian()
