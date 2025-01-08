import pandas as pd

########################################################################################################################
##                                                     Zadanie 1                                                      ##
########################################################################################################################

# Definiujemy funkcję przyjmującą zestaw danych w DataFrame, nazwe kolumny ceny i nazwe kolumny z przedmiotami
def wybierz_po_najnizszej_cenie(dataframe, nazwa_kolumny_ceny, nazwa_kolumny_przedmiotow):
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
    print(f"Najtańsze {najtanszy_przedmiot} o cenie {minimalna_cena} zł")


# Punkt wejścia programu:
if __name__ == "__main__":
    # ładujemy dane tylko w trakcie wykonywania programu ze skryptu macierzystego
    dane = pd.read_excel("./ceny_gier.xlsx")
    # wypisujemy zwróconą przez funkcję wartość
    wybierz_po_najnizszej_cenie(dane, 'cena', 'gra')