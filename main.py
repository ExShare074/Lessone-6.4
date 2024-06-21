# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не
# изменяя существующий код бойцов или механизм боя.

# Исходные данные:
#
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1: Создайте абстрактный класс для оружия
#
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
# Шаг 2: Реализуйте конкретные типы оружия
#
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод
# attack() своим уникальным способом.
# Шаг 3: Модифицируйте класс Fighter
#
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод changeWeapon(), который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
#
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
#
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко
# добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.

from abc import ABC, abstractmethod
class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def changeWeapon(self, newWeapon):
        self.weapon = newWeapon

    def fight(self, monster):
        self.weapon.attack(monster)

class Monster:
    def __init__(self, weapon):
        self.weapon = weapon

    def fight(self, fighter):
        self.weapon.attack(fighter)

class Weapon:
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self, monster):
        print("Мечь атакует монстра!")

class Bow(Weapon):
    def attack(self, monster):
        print("Лук атакует монстра!")

# Пример использования

fighter = Fighter("Андрей", Sword())
monster = Monster("Злой монстр")

#Бой начинается
print(f"{fighter.name} атакует: {fighter.attack()}")
print(f"{monster.name} контратакует!")

# Смена оружия
fighter.changeWeapon(Bow())
print(f"{fighter.name} сменил оружие на лук и стреляет: {fighter.attack()}")
print(f"{monster.name} падает побежденным!")