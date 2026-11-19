studenti = {
    "mario" : 36,
    "luca" : 30,
    "simona" : 28,
    "andrea" : 10,
    "melania" : 29,
    "catalina" : 27,
    "giovanni" : 31,
    "giseppe" : 26,
    "mattia": 32,
    "francesca" : 24
}


nomi = list(studenti.keys())
voti = list(studenti.values())


i = 0

while i < len(nomi):
    nome = nomi[i]
    voto = studenti[nome]
    print(f"Studente {nome} - voto {voto}")
    i += 1
    # i = i + 1

