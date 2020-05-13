
# Wypisze tylko liczby nieparzyste - 1 3 5 7 9
def ktoredy(kto, dokad):
    print('Jak '+ kto +' trafi do '+str(dokad))

import lib
import err
mojobiekt =lib.FirstClass()
for x in range(10):
    # Sprawdz, czy x jest parzyste
 #   mojobiekt.pobierz_imie('a')
    lib.FirstClass.pobierz_imie()
    try:
        lib.FirstClass.pobierz_imie()
        tablica = []
        tablica.append(x)

        if x==4 :
            tablica.remove(x)
        tablica.remove(x)
    except : # Raised when accessing a non-existing index of a list
        err.Wyjatki.info("BLAD")

kto =str('aa')
ktoredy(kto, x)
print ('Koniec')
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
