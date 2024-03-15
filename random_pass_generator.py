
import random

#python stringlere liste gibi davranır.
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunluk = int(input("Lütfen parola uzunluğu girin:"))

parola = ""

karakter = random.choice(karakterler)

print(karakter)
for i in range(parola_uzunluk):
  
