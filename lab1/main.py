from typing import List
from typing import Any


# 1WSZA KLASA


class House:
    doors: int
    color: str
    type: str

    def __init__(self, doors: int, color: str, type:str) -> None:
        self.doors = doors
        self.color = color
        self.type = type

    def change_color(self, new_color: str) -> None:
        if new_color == self.color:
            print('Operation impossible')
            return  # raise ValueError('Operation impossible') -- mozna takze wyrzucic wyjatek

        self.color = new_color

    def __str__(self) -> str:
        return 'Number of doors : {0}, colour: {1}, type: {2}'.format(self.doors, self.color, self.type)

    def __len__(self) -> int:
        return 102


green_house: House = House(doors=20, color='green', type='wooden')

print(green_house.doors)
print(green_house.color)
print(green_house.type)
print(green_house)  # wyswietli nam, ze jest to obiekt klasy house i przestrzen adresową //chyba ze ustawimy metodę str,
                    # i wtedy wyswietli nam sie ustawiony przez nas komunikat, w ktorym mozemy przykladowo
                    # przygotowac tekst,
                    # ktory bedzie przechowywal wartosci wszystkich atrybutow


blue_house: House = House(doors=40, color='blue', type='aluminium')

print(blue_house.doors)
print(blue_house.color)
print(blue_house.type)
print(blue_house)

print(len(blue_house))

# lista jednokierunkowa ( linked list )
# head jest pierwszym elementem, wskaznikiem na 1wszy wezel w liscie
# tail jest wskaznikiem na ostatni wezel w liscie
# wezel(node) zawiera 2 atrubuty, jest w pamieci rozrzucony losowo, ale ma zawsze wskaznik na wezel nastepny --
# data to jakas wartosc wezla
# next to wskaznik na nastepny wezel

# assert - sprawdza czy wyrazenie logiczne jest prawdziwe, np assert 1 == 1 ( wyswietli prawde ), assert 1 == 12 - blad
# assert - assercja pomaga przy sprawdzaniu poprawnosci


def sum1(x: int, y: int) -> int:  # sum1, bcs its default name of function sum in python
    return x + y


assert sum1(2, 6) == 8
# assert sum1(12, 6) == 8

# TO DO : (1) zrobic projekt - zad1(lista kierunkowa) - zad2(kolejka) - zad3(stos)