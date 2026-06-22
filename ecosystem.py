from organism import Organism

class Ecosystem:
    """
    Класс, управляющий средой обитания и симуляцией дней для организмов.
    """
    def __init__(self):
        self.organisms = []

    def add_organism(self, organism: Organism):
        """Добавляет новый организм в экосистему."""
        self.organisms.append(organism)

    def simulate_day(self):
        """Запускает симуляцию одного дня для всех существ экосистемы."""
        print("\n--- Симуляция дня в экосистеме ---")
        for org in self.organisms:
            if org.is_alive():
                org.eat(10)
            else:
                print(f" {org.name} мёртв.")
