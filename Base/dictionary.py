from Base import dictionary1


persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 36,
    "citta": "Roma",
    "cf": "LLCODE123548PX",
    "professione": "Ingegnere"
 }


# print(persona["nome"])
# print(persona.get("cf"))

# # Modifica
# persona["cf"] = "LLCODE123548RT"


# print(persona["cf"])


# key e value
# ciclo per stampare tutti i chiavi
for key in persona.keys():
    print(f"Chiave: {key}")



# ciclo per stampare tutti i valori
print("\n=====================================================\n")
for value in persona.values():
    print(f"Valore: {value}")


print("\n========= Stampa le coppie chiave-valore del dictionary =========\n")
for chiave, valore in persona.items():
    print(f"🔐 {chiave} - 🛄 {valore}")




