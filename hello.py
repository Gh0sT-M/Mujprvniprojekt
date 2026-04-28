import os

user = "Gh0sT-M"
print(f"--- System Ready, {user} ---")
print("Tvoje prvni Python mise byla uspesna.")

#Vypsani souboru v teto slozce
files = os.listdir('.')
print(f"Aktualni soubory v projektu: {files}")