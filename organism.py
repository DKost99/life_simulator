class Organism:
    """
    Класс, представляющий живой организм в симуляторе.
    """
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        """Проверяет, жив ли организм."""
        return self.health > 0

    def eat(self, food_amount):
        """Логика питания организма, повышающая его здоровье."""
        self.health += food_amount
        print(f" {self.name} поел и восстановил здоровье. Текущее здоровье: {self.health}")
