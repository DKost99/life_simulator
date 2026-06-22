import time
import random

class Organism:
    """
    Класс, представляющий отдельный живой организм (например, Травоядное).
    """
    def __init__(self, name):
        self.name = name
        self.energy = 50  # Начальная энергия организма

    def eat(self, amount):
        """Увеличивает энергию организма при поглощении пищи."""
        self.energy += amount
        print(f"  [{self.name}] Съел пищу. Энергия: {self.energy}")


class Population:
    """
    Класс, представляющий популяцию организмов.
    Управляет жизненным циклом группы существ.
    """
    def __init__(self, species_name, count):
        self.species_name = species_name
        # Создаем список индивидуальных организмов
        self.members = [Organism(f"{species_name}-{i+1}") for i in range(count)]

    def simulate_life(self, ecosystem):
        """
        Логика жизнедеятельности популяции. 
        Популяция ищет и потребляет ресурсы из экосистемы.
        """
        for _ in range(3):  # 3 цикла симуляции
            for organism in self.members:
                # Пытаемся добыть еду из общей экосистемы
                food_found = ecosystem.get_food(10)
                if food_found > 0:
                    organism.eat(food_found)
                else:
                    organism.energy -= 15
                    print(f"  [{organism.name}] Не нашел еды! Энергия упала до: {organism.energy}")
                
                time.sleep(random.uniform(0.2, 0.5))
