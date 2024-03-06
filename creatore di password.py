import random


caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_scelta = int(input("Inserisci il numero di caratteri della password: "))
password = ""
for i in range(password_scelta):
    password += random.choice(caratteri)

print("La password generata è: ", password)