print("HELLO WORLD!\n\n")


print("ZAD 1")
# # # # # # # # # # # # ZAD 1 # # # # # # # # #


def zad1(pierwsza_litera, nazwisko):
    return pierwsza_litera + "." + nazwisko


print(zad1("I", "Kawczynski"))
print("\n")


print("ZAD 2")
# # # # # # # # # # # # ZAD 2 # # # # # # # # #
imie2 = "janek"
nazwisko2 = "brzeszczeszczykiewicz"


def zad2(imie, nazwisko):
    nazwisko[0].upper()
    return imie[0].upper() + "." + nazwisko.capitalize()


print(zad2(imie2, nazwisko2))
print("\n")


print("ZAD 3")
# # # # # # # # # # # # ZAD 3 # # # # # # # # #


def zad3(rok_x, rok_y, wiek):
    rok = rok_x + rok_y
    rok = int(rok)
    return rok - wiek


print(zad3("20", "21", 20))
print("\n")


print("ZAD 4")
# # # # # # # # # # # # ZAD 4 # # # # # # # # #


def zad4(imie, nazwisko, zad2):
    return zad2(imie, nazwisko)


print(zad4(imie2, nazwisko2, zad2))
print("\n")


print("ZAD 5")
# # # # # # # # # # # # ZAD 5 # # # # # # # # #


def zad5(x, y):
    if(x > 0 and y > 0) & (y != 0):
        return x/y


print(zad5(24, 4))
print(zad5(24, 6))
print(zad5(24, 0))
print(zad5(24, -5))
print("\n")


print("ZAD 6")
# # # # # # # # # # # # ZAD 6 # # # # # # # # #

i = 0
suma = 0

while suma < 100:
    suma = suma + int(input(i))

print(suma)
print("\n")


print("ZAD 7")
# # # # # # # # # # # # ZAD 7 # # # # # # # # #
lista = ['macius', 24, 'angerboda']


def zad7(lista7):
    return tuple(lista7)


print(zad7(lista))
print("\n")


print("ZAD 8")
# # # # # # # # # # # # ZAD 8 # # # # # # # # #
lista8 = []
n = int(input("Enter the size of list : "))
x8 = 0
for i8 in range(n):
    x8 = int(input())
    lista8.append(x8)

print(lista8)
lista8 = tuple(lista8)
print(lista8)
print("\n")


print("ZAD 9")
# # # # # # # # # # # # ZAD 9 # # # # # # # # #


def zad9(x):
    dictionary9 = {'poniedzialek': 1, 'wtorek': 2, 'sroda': 3, 'czwartek': 4, 'piatek': 5, 'sobota': 6, 'niedziela': 7}
    for key, value in dictionary9.items():  # items po to, by określic elementy słownika i operować wartosci i kluczu
        if x == value:
            return key
    return 'musisz podac liczbe z przedziału od 1 do 7'  # w przypadku podania cyfry nie mieszczacej sie w przedziale


print(zad9(1))
print(zad9(2))
print(zad9(6))
print(zad9(9))


print("ZAD 10")
# # # # # # # # # # # # ZAD 10 # # # # # # # # #


def zad10(chain):
    chain = str(chain)
    start = 0
    end = len(chain) - 1  # bo liczba znakow - 1, !! indeksujemy od 0 !!
    while start < end:  # do srodka liczy
        if chain[start] != chain[end]:
            start = start + 1
            end = end - 1
            return 0
        return 1


print(zad10('kotek'))
print(zad10(''))
print(zad10('ala'))
print(zad10('kajak'))
print(zad10('otto'))






