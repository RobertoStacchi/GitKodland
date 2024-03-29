import random
import time

print("Questo è un generatore di password.")

caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_scelta = int(input("Inserisci il numero di caratteri della password: "))
password = ""
for i in range(password_scelta):
    password += random.choice(caratteri)

print("La password generata è: ", password)

print("Vuoi continuare la generazione di password? Avrai solamente una generazione in più. y/n")

if input() == "y":
    caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password_scelta = int(input("Vabbene, inserisci il numero di caratteri della password: "))
    password = ""
    for i in range(password_scelta):
        password += random.choice(caratteri)
    print("La tua nuova password generata è: ", password)

if input() == "n":
    pass

