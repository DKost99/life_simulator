import utils
from ecosystem import Ecosystem
from organism import Organism
from population import Population

def main():
    # Выводим обязательную ссылку из модуля utils при старте
    print(f"Запуск проекта. Ссылка на репозиторий: {utils.GITHUB_REPOSITORY_URL}")

    # 1. Создаем экосистему
    eco = Ecosystem()

    # 2. Создаем популяцию зайцев
    rabbit_population = Population("Популяция Зайцев")

    # 3. Создаем конкретные организмы
    rabbit1 = Organism("Заяц-1", 20)
    rabbit2 = Organism("Заяц-2", 15)
    fox = Organism("Лиса", 30)

    # 4. Группируем зайцев в популяцию
    rabbit_population.add_member(rabbit1)
    rabbit_population.add_member(rabbit2)

    # 5. Добавляем всех существ в общую экосистему для симуляции
    eco.add_organism(rabbit1)
    eco.add_organism(rabbit2)
    eco.add_organism(fox)

    # 6. Запускаем симуляцию дня
    eco.simulate_day()

    # Проверяем статус популяции после симуляции
    print(f"\nСтатус: В {rabbit_population.species_name} сейчас живых особей: {rabbit_population.get_alive_count()}")

if __name__ == "__main__":
    main()
