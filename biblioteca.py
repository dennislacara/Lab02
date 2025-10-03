import csv

class Book:
    def __init__(self, t, a, ap, n):
        self.titolo = t
        self.autore = a
        self.annoPubblicazione = ap
        self.n_pagine = n

def carica_da_file(file_path):
    """Carica i libri dal file"""
    try:
        f = open(file_path,"r")
    except FileNotFoundError:
        return None
    sezioni = {1 : [], 2 : [], 3 : [], 4 : [], 5 : []}

    for riga in csv.reader(f):
        if len(riga) == 5: # escludo la prima riga
            sezioni[int(riga[4])].append(Book(riga[0], riga[1], riga[2], riga[3]))
    return sezioni

    # TODO


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    for key in biblioteca.keys():
        for book in biblioteca[key]:
            if titolo == book.titolo:
                return None
    biblioteca[sezione].append(Book(titolo, autore, anno, pagine))
    f = open(file_path, 'a')
    f.write(f'{titolo}, {autore}, {anno}, {pagine}, {sezione}\n')
    f.close()
    return True

    # TODO

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    for key in biblioteca.keys():
        for book in biblioteca[key]:
            if titolo == book.titolo:
                sezione = key
                return f"{book.titolo}, {book.autore}, {book.annoPubblicazione}, {book.n_pagine}, {sezione}"
    return None
    # TODO


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    if sezione in biblioteca.keys():
        libri_sezione = []
        for book in biblioteca[sezione]:
            libri_sezione.append(book.titolo)
        ordinati = sorted(libri_sezione)
        return ordinati
    else:
        return None
    # TODO


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path) # assegno alla variabile biblioteca: sezioni (r.19)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro '{titolo}' aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
