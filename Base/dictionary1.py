
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


# Calcolare la media dei voti degli studenti
# sum() len() nin() max() get() ..
media = sum(studenti.values()) / len(studenti)

# Numero degli studenti
# print(len(studenti))


minimo_voti = min(studenti.values())
massimo_voti = max(studenti.values())


print(f"La media dei voti è: {media:.3f}")
print(f"Il Valore minimo è: {minimo_voti}")
print(f"Il Valore massimo è: {massimo_voti}")

print("\n===========================================================\n")

print("Studenti sopra la media")

for key, value in studenti.items():
    if value > media:
        print(f"Il nome dello studente sopra la media è: {key}")
    else:
        print(f"Il nome dello studente sotto la media è: {key}")


print("\n===========================================================\n")
studenti_voti = {}

studenti_voti["luana"] = [28, 30, 27]
studenti_voti["brenda"]= [27, 28, 30, 27, 28]
studenti_voti["melania"]= [25, 29, 30, 24, 27, 30, 24]

for studente, voto in studenti_voti.items():
    print(f"Studente: {studente.upper()} ha ottenuo i seguenti voti: {voto}")
