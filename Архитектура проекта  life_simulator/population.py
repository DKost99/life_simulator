from organism import Organism

class Population:
    """
    Класс, представляющий группу (популяцию) организмов одного вида.
    """
    def __init__(self, species_name):
        self.species_name = species_name
        self.members = []  # Список организмов этой популяции

    def add_member(self, organism: Organism):
        """Добавляет новый организм в популяцию."""
        self.members.append(organism)

    def get_alive_count(self):
        """Возвращает количество живых участников популяции."""
        alive_members = [m for m in self.members if m.is_alive()]
        return len(alive_members)
