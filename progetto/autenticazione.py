# Autenticazione

# database di utenti
username = "Dario"
password = "Dario@2026"


# chiedeiamo all'utente di inserire le credenziali
user_utente = str(input("Inserisci il tuo username: "))
user_password = str(input("Inserisci la tua password: "))


# confrontare le credenziali inserite con quelle del database
if(user_utente == username and user_password == password ):
    print("Log-in Effettuato correttamente")
    print(f"Benvenuto {username}")
elif(user_utente != username ):
    print("invalid username")
elif(user_password != password):
    print("invalid password")
else:
    print("credenziali non valide")


