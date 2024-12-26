import numpy as np

def zad1(debug = False):
    x = np.random.uniform(-10,10+1e-5, (3,2))
    y = np.random.uniform(-10,10+1e-5, (2,3))
    if debug:
        print(f"ZADANIE 1\n{x = }\n{y = }\n{x.shape = }\n{y.shape = }\n")
    return x, y

mac_zad_1_1, mac_zad_1_2 = zad1(debug=True)

def zad2(macierz1, macierz2, debug=False):
    if debug:
        print(f"\nZADANIE 2\n{macierz1@macierz2 = }\n")
    return macierz1@macierz2

z2 = zad2(mac_zad_1_1, mac_zad_1_2, debug = True)

def zad3(m1, m2, debug = False):
    m1trans = m1.transpose()
    m2trans = m2.T
    if debug:
        print("\nZADANIE 3\n")
        print(f"{m1.shape = } -> {m1trans.shape = }")
        print(f"{m2.shape = } -> {m2trans.shape = }")
    return m1trans, m2trans

z3m1, z3m2 = zad3(mac_zad_1_1, mac_zad_1_2, debug=True)

z4 = zad2(z3m1, z3m2, debug=False)
print(f"\nZADANIE 4\n{z4 = }\n{z4.shape = }\n")

def zad5(macierz, debug = False):
    if debug:
        print("\nZADANIE 5\n")
    for idx, element in enumerate(macierz):
        if debug:
            print(f"Rząd {idx}: {element}")

zad5(z4, debug=True)

def zad6(macierz, debug=False):
    if debug:
        print("\nZADANIE 6\n")
    for idx, element in enumerate(macierz.T):
        if debug:
            print(f"Kolumna {idx}: {element}")

zad6(z4, debug=True)

def zad7_i_8(macierz1, macierz2, debug=False):
    if debug:
        print("\nZADANIE 7 i 8\n")
    try:
        dodawanie = macierz1+macierz2
        odejmowanie = macierz1-macierz2
    except ValueError:
        if debug:
            print(f"Macierze mają różne rozmiary! {macierz1.shape = } =/= {macierz2.shape = }")
            print(f"Macierz 1 zostanie przetransponowana!\n{macierz1.shape = } -> {macierz1.T.shape = }")
        dodawanie = macierz1.T+macierz2
        odejmowanie = macierz1.T-macierz2
        if debug:
            print(f"{dodawanie = }\n{odejmowanie = }")
    return dodawanie, odejmowanie

dod, odej = zad7_i_8(mac_zad_1_1, mac_zad_1_2, debug=True)

### ZADANIE 9 JEST Z GWIAZDKĄ, SPRÓBUJCIE JE WYKONAĆ SAMI A WYNIKI OMÓWIMY NA KOLEJNYCH ZAJĘCIACH