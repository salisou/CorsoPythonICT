# input e output dell'utente in python

print("Benvenuto nel programma di input e output in python\n")

# num1 = float(input("Inserisci il primo numero: "))
# num2 = float(input("Inserisci il secondo numero: "))

# somma = num1 + num2
# sottrazione = num1 - num2
# moltiplicazione = num1 * num2
# divisione = num1 / num2
# resto = num1 % num2
# divisione_intera = num1 // num2


# print(f"\nLa somma di {num1} e {num2} è: {somma}\n")
# print(f"\nLa sottrazione di {num1} e {num2} è: {sottrazione}\n")
# print(f"\nLa moltiplicazione di {num1} e {num2} è: {moltiplicazione}\n")
# print(f"\nLa divisione di {num1} e {num2} è: {divisione}\n")
# print(f"\nIl resto di {num1} e {num2} è: {resto}\n")
# print(f"\nLa divisione intera di {num1} e {num2} è: {divisione_intera}\n")


# Operatori di confronto <, >, <=, >=, ==, !=
eta = int(input("Inserisci la tua età: "))

maggiore=18
if(eta>= 18):
    print(f"Sei maggiorenne")
else:
    print(f"non hai raggiunto la maggiore età, ti mancano ancora {maggiore - eta} anni")


if(eta>= 18):
    print(f"Sei maggiorenne")
elif(eta<18):
    print(f"non hai raggiunto la maggiore età, ti mancano ancora {maggiore - eta} anni")
else:
    print(f"età non valida")


if(eta>= 18):
    if(eta>= 18):
        print(f"Sei maggiorenne")
    else:
        print(f"non hai raggiunto la maggiore età, ti mancano ancora {maggiore - eta} anni")
else:
    print(f"età non valida")
