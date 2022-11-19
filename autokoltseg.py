# File: autokoltseg.py
# Author: Béres Délia
# Copyright: 2022, Béres Délia
# Group: Szoft 1/I/E
# Date: 2022-11-19
# Github: https://github.com/deliaberes
# Licenc: GNU GPL
 

print("Béres Délia")
print("2022.11.19")
print("SZOFT 1/I/E")
print(" ")
print("Kedves Ügyfelünk! \nHa kíváncsi mennyibe is került autójával egy adott hónapban pontosan egy kilóméter megtétele az összes költségével együtt! \nKérem adja meg az alábbi adatokat:")
print(" ")
a = int(input("Gépjárműadó (havi adat): "))
b = int(input("Kötelezőbiztosítás (havi adat): "))
g = int(input("Garázs bérletidíj (havi adat): "))
j = int(input("Javítási költségek (havi adat): "))
b = int(input("Benzinköltség (havi adat): "))
k = int(input("Megtett kilóméter (havi adat): "))
print(" ")


e = (a+b+g+j+b)/k
print("Eredmény:", e, "Ft/Km")











