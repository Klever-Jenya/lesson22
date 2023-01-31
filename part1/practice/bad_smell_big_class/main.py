class Warrior:  # Воин

    def attack(self):
        pass

    def move(self):
        pass

    def defense(self):  # защита
        pass


class Healer:  # Лекарь
    def heal(self):  # лечить
        pass

    def move(self):
        pass

    def defense(self):  # защита
        pass


class Tree:

    def defense(self):  # защита
        pass

    def on_fire(self):
        pass


class Trap:  # Ловушка
    def attack(self):
        pass


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()
