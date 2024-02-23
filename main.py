meme_dict = {
    "PARA": "Preoccupari per qualcosa, paranoiarsi",
    "BOICOTTARE": "Ostacolare in qualsiasi modo",
    "ASTRUSO": "Un qualcosa di impossibile",
    "DECADENTISTA": "Una persona che vede un oggetto quasias in mille modi e funzioni diversi",
    "PYTHON": "Linguaggio di programmazione, il cui nome deriva da un gruppo comico chiamato Monty Python",
    "ITERARE": "Sinonimo ri ripetere",
    "BUG": "Un difetto di un programma che causa un risultato non come si aspettava"
}

while True:
    print("Ciao, questo è un mini dizionario. In quale parola sei in assenza di conoscenza?", meme_dict.keys())
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

    if parola in meme_dict.keys():
        print("Il significato della parola è:", meme_dict[parola])
    else:
        print("Parola non trovata")

    continua = input("Vuoi cercare un'altra parola? (s/n): ")
    if continua.lower() != 's':
        print("Grazie per non aver rimpiazzato Garzanti con me!")
        break
