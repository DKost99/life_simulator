import utils
from ecosystem import Ecosystem
from organism import Organism
from population import Population

def main():
    print(f"Запуск проекта. Ссылка на репозиторий: {utils.GITHUB_REPOSITORY_URL}")

    eco = Ecosystem()
    rabbit_population = Population("Популяция Зайцев")

    rabbit1 = Organism("Заяц-1", 20)
    rabbit2 = Organism("Заяц-2", 15)
    fox = Organism("Лиса", 30)

    rabbit_population.add_member(rabbit1)
    rabbit_population.add_member(rabbit2)

    eco.add_organism(rabbit1)
    eco.add_organism(rabbit2)
    eco.add_organism(fox)

    eco.simulate_day()

    print(f"\nСтатус: В {rabbit_population.species_name} сейчас живых особей: {rabbit_population.get_alive_count()}")

if __name__ == "__main__":
    main()
