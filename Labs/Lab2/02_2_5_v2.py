def controlla_matricola(matricola: str) -> None:
    if not(not matricola[0:1].isnumeric() and matricola[1:].isnumeric()):
        raise ValueError('Il valore "{}" è sbagliato, necessario come primo carattere una lettera seguito da un numero\nexp : s343243'.format(matricola))

#imput
matricola_1: str = input("Inserisci il primo numero di matricola:\n")
matricola_2: str = input("Inserisci il secondo numero di matricola:\n")

#verifica corettezza imput
controlla_matricola(matricola_1)
controlla_matricola(matricola_2)

#estrazione numero di matricola
n_matricola_1: int = int(matricola_1[1:])
n_matricola_2: int = int(matricola_2[1:])

#print a schermo
if n_matricola_1 > n_matricola_2 :
    print(matricola_1,"\t",matricola_2)
else :
    print(matricola_2,"\t",matricola_1)
