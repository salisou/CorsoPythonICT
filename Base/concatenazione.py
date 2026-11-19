# La concatenazione in Python
nome =  "Dario"
cognome = 'Modenese'
eta = 30
stipendio = 150.050

# Concatenazione di stringhe
print('Ciao, mi chiamo ' + nome + ' ' + cognome + ' e ho ' + str(eta) + ' anni. Il mio stipendio è di ' + str(stipendio) + ' euro.\n')

# la formaattazione con f-string
print(f'Ciao, mi chiamo {nome} {cognome} e ho {eta} anni. Il mio stipendio è di {stipendio} euro.\n')

# L'interpolazione con il metodo format()
print('Ciao, mi chiamo', nome, cognome, 'e ho', str(eta), 'anni. Il mio stipendio è di', stipendio,  'euro.')
