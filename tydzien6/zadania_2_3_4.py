import pandas as pd
########################################################################################################################
##                                                    Zadanie 2;3;4                                                   ##
########################################################################################################################

# Definiujemy klasę Człowiek
class Czlowiek:
    # Zadanie 2 - tworzymy inicjator klasy
    def __init__(self, imie, nazwizko, wiek, wzrost, waga):
        self.imie = imie
        self.nazwisko = nazwizko
        self.wiek = wiek
        self.wzrost = wzrost
        self.waga = waga

    ## Zadanie 4 - metoda "idź do sklepu"
    def idz_do_sklepu(self):
        print(f"{self.imie} idzie do sklepu.")

    ## Zadanie 4 - metoda "kup po najniższej cenie"
    def kup_po_najnizszej_cenie(self, dataframe, nazwa_kolumny_ceny, nazwa_kolumny_przedmiotow):
        # Znajdujemy minimalną wartość w kolumnie cena
        minimalna_cena = min(dataframe[nazwa_kolumny_ceny])
        # definiujemy pustą zmienną do przechowywania tytułu gry
        najtanszy_przedmiot = None
        # Dla każdego indeksu w przedziale od 0 do długości zestawu danych
        for indeks in range(len(dataframe)):
            # Jeśli cena w danej lokalizacji indeks jest równa minimalnej cenie
            if dataframe[nazwa_kolumny_ceny][indeks] == minimalna_cena:
                # Zapisz tytuł przedmiotu o najniższej cenie
                najtanszy_przedmiot = dataframe[nazwa_kolumny_przedmiotow][indeks]
        # wyświetl odpowiednie dane
        print(f"{self.imie} kupuje {najtanszy_przedmiot} za {minimalna_cena} zł")


# Punkt wejścia programu:
if __name__ == '__main__':
    # ładujemy dane tylko w trakcie wykonywania programu ze skryptu macierzystego
    dane = pd.read_excel("./ceny_gier.xlsx")

    ## Zadanie 3 - definicja obiektów i print ich parametrów
    # definiujemy obiekty Seba i Jula
    seba = Czlowiek("Seba", "Nietuzinkowski", 23, 180, 75)
    jula = Czlowiek("Jula", "Wiedźma", 20, 172, 67)

    # wypisywanie słowników parametrów obiektów za pomocą wbudowanej funkcji vars(obiekt)
    print(f"Obiekt Seba: {vars(seba)}")
    print(f"Obiekt Jula: {vars(jula)}")

    ## Zadanie 4 - metody idź do sklepu i kup po najniższej cenie, przykład na obiekcie Jula
    jula.idz_do_sklepu()
    jula.kup_po_najnizszej_cenie(dane, 'cena', 'gra')