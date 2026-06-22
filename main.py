import threading
import utils
from ecosystem import Ecosystem
from organism import Population

if __name__ == "__main__":
    print(f"--- Запуск консольного симулятора жизни ---")
    print(f"Репозиторий проекта: {utils.GITHUB_REPOSITORY_URL}\n")
    
    # 1. Создаем экосистему с начальным запасом еды
    forest_ecosystem = Ecosystem(initial_food=40)

    # 2. Создаем популяцию из 2-х организмов (Травоядных)
    deer_population = Population(species_name="Олень", count=2)

    # 3. Настраиваем потоки: один для жизнедеятельности животных, второй для роста ресурсов
    population_thread = threading.Thread(target=deer_population.simulate_life, args=(forest_ecosystem,))
    nature_thread = threading.Thread(target=forest_ecosystem.regenerate)

    # 4. Запускаем параллельные процессы в экосистеме
    population_thread.start()
    nature_thread.start()

    # 5. Ожидаем завершения симуляции
    population_thread.join()
    nature_thread.join()

    print("\n--- Симуляция экосистемы успешно завершена! ---")
