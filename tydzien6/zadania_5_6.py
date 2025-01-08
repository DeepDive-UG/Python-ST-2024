import numpy as np
########################################################################################################################
##                                                    Zadanie 5;6                                                     ##
########################################################################################################################

# Definiujemy klasę Kalkulator
class Kalkulator:
    # Definiujemy inicjator klasy
    def __init__(self, NUM_MAT1, NUM_MAT2):
        self.num_mat1 = NUM_MAT1
        self.num_mat2 = NUM_MAT2

    # Definiujemy metody kalkulatora dla odpowiednich typów
    def dodawanie(self):
        return f"Dodawanie: {self.num_mat1} + {self.num_mat2} = {self.num_mat1 + self.num_mat2}\n"

    def odejmowanie(self):
        return f"Odejmowanie: {self.num_mat1} - {self.num_mat2} = {self.num_mat1 - self.num_mat2}\n"

    def mnozenie(self):
        return f"Mnożenie: {self.num_mat1} * {self.num_mat2} = {self.num_mat1 * self.num_mat2}\n"

    def dzielenie(self):
        try:
            if self.num_mat2 != 0:
                return f"Dzielenie: {self.num_mat1} / {self.num_mat2} = {self.num_mat1 / self.num_mat2}\n"
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            return "Dzielnik wynosi zero, nie można wykonać operacji.\n"

    def potegowanie(self):
        return f"{self.num_mat1} ** {self.num_mat2} = {self.num_mat1 ** self.num_mat2}\n"

    # Pierwiastkowanie można wykonać potęgowaniem przez odwrotność stopnia pierwiastka
    def pierwiastkowanie(self):
        try:
            if self.num_mat2 != 0:
                return f"Pierwiastkowanie: {self.num_mat1} ** (1/{self.num_mat2}) = {self.num_mat1 ** (1 / self.num_mat2)}\n"
            else:
                raise ValueError
        except ValueError:
            return "Nie można pierwiastkować w stopniu 0\n"

    def mnozenie_macierzy(self):
        return f"MNOŻENIE MACIERZY\n\n{self.num_mat1}\nMNOŻONA PRZEZ\n{self.num_mat2}\nWYNOSI\n{np.dot(self.num_mat1, self.num_mat2)}\n"

    def dodawanie_macierzy(self):
        return f"DODAWANIE MACIERZY\n\n{self.num_mat1}\nPLUS\n{self.num_mat2}\nWYNOSI\n{self.num_mat1 + self.num_mat2}\n"

    def odejmowanie_macierzy(self):
        return f"ODEJMOWANIE MACIERZY\n\n{self.num_mat1}\nMINUS\n{self.num_mat2}\nWYNOSI\n{self.num_mat1 - self.num_mat2}\n"

    def dzielenie_macierzy(self):
        # Wyłączamy informacje o napotkaniu 0, NumPy automatycznie przypisuje inf do wyników dzielenie przez 0
        np.seterr(divide='ignore')
        return f"DZIELENIE MACIERZY\n\n{self.num_mat1}\nDZIELONA PRZEZ\n{self.num_mat2}\nWYNOSI\n{self.num_mat1 / self.num_mat2}\n"

    def transpozycja_pierwszej_macierzy(self):
        return f"TRANSPOZYCJA MACIERZY\n{self.num_mat1}\nWYNOSI\n{np.transpose(self.num_mat1)}\n"

    def transpozycja_drugiej_macierzy(self):
        return f"TRANSPOZYCJA MACIERZY\n{self.num_mat2}\nWYNOSI\n{np.transpose(self.num_mat2)}\n"


# Punkt wejścia programu:
if __name__ == "__main__":
    a = Kalkulator(5, 3)
    b = Kalkulator(64, 29)
    c = Kalkulator(7, 9)
    d = Kalkulator(8, 0)
    e = Kalkulator(78, 4)
    f = Kalkulator(110, 2)
    A = np.array([[1, 52, 7, 10],
                  [4, 13, 24, 0],
                  [0, 12, 11, 3],
                  [31, 20, 1, 2]])
    B = np.array([[4, 63, 84, 10],
                  [0, 83, 59, 44],
                  [17, 96, 28, 4],
                  [71, 50, 32, 6]])
    g = Kalkulator(A, B)
    print(f"\nDziałania na liczbach")
    print(a.dodawanie(), b.odejmowanie(), c.mnozenie(), d.dzielenie(), e.potegowanie(), f.pierwiastkowanie(), sep='\n')
    print(f"\nDziałania na macierzach")
    print(g.dodawanie_macierzy(), g.odejmowanie_macierzy(), g.mnozenie_macierzy(), g.dzielenie_macierzy(),
          g.transpozycja_pierwszej_macierzy(), g.transpozycja_drugiej_macierzy(), sep='\n')