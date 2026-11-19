# Il ciclo for in python

"""
    Esempio: voliamo stampare 10 vote ciao Dario

    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
    print("ciao Dario")
"""

#  esempio con il ciclo for

# for variabile in range(10):
#     print("ciao Dario",  variabile + 1)


# Lista in pytho
studenti = ["Dario", "Luca", "Marco", "Giulia", "Sara", "Francesca", "Alessandro"]
voti= [30, 8, 15, 17, 5, 10, 20]

# ciclo per glio studenti
# for studente, voto in zip(studenti, voti):
#     print("Ciao sono => ", studente, "e sono il numero ", studenti.index(studente), "della lista e l'ultimo voto che ho avuto e'", voto)


# for voto in voti:
#     print("Il voto è => ", voto)


varr = []

# # Append ci permette di aggiungere un elemento alla lista
# nuovo_studente = int(input("Inserisci il nome del nuovo studente: "))
# varr.append(nuovo_studente)

print("La lista degli studenti aggiornata è => ", varr)


# insert: Inserisce un elemento in una posizione specifica della lista
nuovo_varr = str(input("Inserisci il nome del nuovo studente da inserire in prima posizione: "))
studenti.insert(0, nuovo_varr)


for studente in studenti:
    print("Ciao sono => ", studente, "e sono il numero ", studenti.index(studente), "della lista")

"""
    Metodi utili per le liste in python:
    append()	Aggiunge un elemento alla fine
    insert()	Inserisce un elemento in una posizione
    extend()	Aggiunge più elementi
    remove()	Rimuove un elemento specifico
    pop()	Rimuove e restituisce un elemento
    clear()	Svuota la lista
    sort()	Ordina gli elementi
    reverse()	Inverte l'ordine
    count()	Conta le occorrenze
    index()	Trova la posizione di un elemento
    copy()	Crea una copia superficiale
"""
