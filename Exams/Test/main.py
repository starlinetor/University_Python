#personaggi caratteristiche --> creo una lista di tabelle 
# Chiave --> caratteristica
# Valore --> valore della corrispettiva caratteristica

import csv


def caratteristiche_personaggi(file_input):
    
    f = open(file_input, "r", encoding="utf-8")
    reader = csv.DictReader(f, delimiter=";")

    for personaggio in reader: 
        print(personaggio)

    f.close()
    return reader

def main():
    personaggi = caratteristiche_personaggi("personaggi.csv")
    print(personaggi)

main()