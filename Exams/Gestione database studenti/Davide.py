#caricare i dati degli studenti su un dizionario

##non vorrei sparare una cazzata ma csv non credo ci sia come libreria nell'esame
import csv
#import interessante e utile decisamente ma 
# 1 non credo ci sia come libreria installata
# 2 l'output è simile ma non uguale a quello richiesto
"""
Tuo
[{'GPA': '3.5', 'ID': '1', 'cognome_studente': 'Rossi', 'grado': '10A'},
 {'GPA': '3.9', 'ID': '3', 'cognome_studente': 'Verdi', 'grado': '10A'},
 {'GPA': '3.8', 'ID': '5', 'cognome_studente': 'Viola', 'grado': '11B'}]

Richiesto
{'ID': 1, 'cognome_studente': 'Rossi', 'grado': '10A', 'GPA': 3.5}
{'ID': 3, 'cognome_studente': 'Verdi', 'grado': '10A', 'GPA': 3.9}
{'ID': 5, 'cognome_studente': 'Viola', 'grado': '11B', 'GPA': 3.8}
"""
from pprint import pprint

#questa è un po' una cosa mia ma io consiglio sempre di specificare il tipo di variabili
#def organizzazione_dati(file_input : str) -> list[DictReader]:
#questo specifica che file_unput è una stringa e la funzione ritorna una list[DictReader]
def organizzazione_dati(file_input):
    
    #io gli darei un nome più descrittivo
    try:
        input_studenti = open(file_input, "r", encoding="utf-8")
    except IOError:
        #molto bene che hai inserito questo 
        #probabilmente converebbe aggiungere un raise invece di un semplice print
        #diventa difficile capire dove capita il bug
        #raise(IOError)
        print("impossibile aprire il file")
        exit()

    reader = csv.DictReader(input_studenti, delimiter=",")

    lista_studenti = []
    lista_studenti = list(reader)

    input_studenti.close()

    return lista_studenti

def ricerca_ID(lista_studenti, istruzioni_input):
    #Ha un po' poco senso aprire lo stesso file 3 volte, probabilmente ti conveniva creare una funzione per aprire e salvare il file
    #e poi usare queste tre funzioni solo per stampare i dati
    try:
        istruzioni = open(istruzioni_input, "r", encoding="utf-8")
    except IOError:
        print("impossibile aprire il file")
        exit()

    riga1 = istruzioni.readline()
    id_cercati = riga1.rstrip().split(",")

    lista_ID = []
    for id in lista_studenti:
        if id["ID"] in id_cercati:
            lista_ID.append(id)
        
    istruzioni.close()
    return lista_ID

def ricerca_cognome(lista_studenti, istruzioni_input):
    try:
        istruzioni = open(istruzioni_input, "r", encoding="utf-8")
    except IOError:
        print("impossibile aprire il file")
        exit()

    riga1 = istruzioni.readline()
    #qui non è necessario salvare la prima linea puoi fare semplicemente
    #istruzioni.readline()
    #magari se lo fai aggiungi un commento del tipo "salto prima linea"
    riga2 = istruzioni.readline()

    cognomi_cercati = riga2.rstrip().split()

    lista_cognomi = []
    for cognome in lista_studenti:
        if cognome["cognome_studente"] in cognomi_cercati:
            lista_cognomi.append(cognome)

    istruzioni.close()
    return lista_cognomi

def media_GPA(lista_studenti, istruzioni_input):
    #se vuoi ricordati che lista_studenti è una lista probabilmente conviene fare : 
    #def media_GPA(studenti : list[], istruzioni_input):
    #Così non solo devi scrivere di meno ma vscode ti suggerisce comandi per le liste
    try:
        istruzioni = open(istruzioni_input, "r", encoding="utf-8")
    except IOError:
        print("impossibile aprire il file")
        exit()

    riga1 = istruzioni.readline()
    riga2 = istruzioni.readline()
    riga3 = istruzioni.readline()
    #questo è uno dei motivi per cui leggere tre volte lo stesso file ha poco senso
    grado = riga3.rstrip()

    GPA_studenti_classe = []
    numero_studenti = 0
    for classe in lista_studenti:
        #questo è principalmente strano da leggere perchè non fare 
        #for studente in lista_studenti
        if classe["grado"] == grado:
            numero_studenti += 1
            classe["GPA"] = float(classe["GPA"])
            GPA_studenti_classe.append(classe["GPA"])
            #quest lo avrei fatto in una linea 
            #GPA_studenti_classe.append(float(classe["GPA"]))


    somma = sum(GPA_studenti_classe)
    #potevi semplicemente dichiarare somma = 0 e poi in ogni iterazione fare somma += float(classe["GPA"])
    #ti risparmi di creare una lista
    if numero_studenti > 0:
        media = somma/numero_studenti
    else:
        media = 0
        #sconsiglierei questo approccio, perchè se siamo in questo caso allora la classe richiesta non esiste nel database+
        #ha quindi più senso dare un errore più che un numero arbitrario

    grado_media = [media, grado] 

    return grado_media

def main():
    #nota un po' inutile ma era uno studenti.csv non .txt
    lista_studenti = organizzazione_dati("studenti.csv")
    #non è richiesto di stampare la lista degli studenti
    #se lo fai però almeno aggiungi una didascalia
    #print("Lista studenti :")
    pprint(lista_studenti)
    print()

    #non è molto bello da vedere il fatto che apri il file criteria due volte
    #se il nome cambia dovresti criscrivere criteria.txt 3 volte 
    ID_studenti = ricerca_ID(lista_studenti, "criteria.txt")
    print("Studenti trovati per ID:")
    pprint(ID_studenti)
    #questo lo puoi fare in una linea, potrei sbagliarmi ma ha poco senso salvare cose che non riutilizzi
    #pprint(ricerca_ID(lista_studenti, "criteria.txt"))
    print()

    cognomi_studenti = ricerca_cognome(lista_studenti, "criteria.txt")
    print("Studenti trovati per cognome: ")
    pprint(cognomi_studenti)
    print()

    media = media_GPA(lista_studenti, "criteria.txt")
    print(f"Media GPA degli studenti della classe {media[1]}: {media[0]} ")

#qui aggiungeri un
"""
if __name__ == "__main__":
    main()
"""
main()