print("TO SIE DZIEJE KIEDY NIE WŁOŻYMY CZEGOŚ DO PUNKTU WEJŚCIOWEGO PROGRAMU!!")


class MojaKlasa:
    def __init__(self, parametr1, parametr2, parametr3):
        self.parametr1 = parametr1
        self.parametr2 = parametr2
        self.parametr3 = parametr3
        self.disco = "https://www.youtube.com/watch?v=F2YpXC1itEE"

    def pokaz_typ_parametrow(self):
        print(f"Parametry Klasy {self.__class__.__name__}: ",
              ', '.join([f"{param}: {type(value).__name__}" for param, value in vars(self).items()]))

    def dzikie_disco(self):
        import webbrowser
        webbrowser.open(self.disco)


if __name__ == '__main__':
    test = MojaKlasa(123, '456', [7, 8, 9])
    test.pokaz_typ_parametrow()
    test.disco = "https://www.youtube.com/watch?v=Q_9VMaX61nI"
    test.dzikie_disco()
