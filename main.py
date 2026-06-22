import utils
from ecosystem import Ecosystem
from organism import Organism

def main():
    # Выводим обязательную ссылку из модуля utils при старте
    print(f"Запуск проекта. Ссылка на репозиторий: {utils.GITHUB_REPOSITORY_URL}")

    # Создаем экосистему
    eco = Ecosystem()

    # Создаем организмы по примеру из ТЗ
    rabbit = Organism("Заяц", 20)
    fox = Organism("Лиса", 30)

    # Добавляем их в среду обитания
    eco.add_organism(rabbit)
    eco.add_organism(fox)

    # Запускаем симуляцию дня
    eco.simulate_day()

if __name__ == "__main__":
    main()
