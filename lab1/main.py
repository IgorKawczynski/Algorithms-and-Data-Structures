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
<<<<<<< HEAD
                    # i wtedy wyswietli nam sie ustawiony przez nas komunikat, w ktorym mozemy przykladowo
                    # przygotowac tekst,
=======
                    # i wtedy wyswietli nam sie ustawiony przez nas komunikat, w ktorym mozemy przykladowo przygotowac tekst,
>>>>>>> 496da082a4987dec1fa4e8279bc81a40432d23e7
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

<<<<<<< HEAD
# TO DO : (1) zrobic projekt - zad1(lista kierunkowa) - zad2(kolejka) - zad3(stos)
=======
# TO DO : (1) zrobic projekt - zad1(lista kierunkowa) - zad2(kolejka) - zad3(stos)


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: None
        self.tail: None

    def push(self, data2) -> None:
        Node2 = Node(data2)
        Node2.next = self.head
        self.head = Node2


list1 = LinkedList()
list1.head = Node("Albert")
ex1 = Node("Beowulf")
ex2 = Node(124)
list1.head.next = ex1  # polaczenie pierwszego wezla do drugiego
ex1.next = ex2

print(list1.head.data)
print(list1.head.next)
print(list1.head.next.data)
print(list1.head.next.next.data)

list1.push("START")
print(list1.head.data)
print(list1.head.next.data)

>>>>>>> 496da082a4987dec1fa4e8279bc81a40432d23e7
