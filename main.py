import threading
import time
import random

# 1. Создаем Склад, где лежат товары
class Warehouse:
    def __init__(self):
        self.storage = []           # Тут хранятся товары
        self.lock = threading.Lock() # Замок, чтобы потоки не толкались

    def add_product(self, product):
        with self.lock: # Закрываем дверь на замок, пока кладем товар
            self.storage.append(product)
            print(f"[ЗАВОД] Сделал: {product}. На складе: {len(self.storage)}")

    def remove_product(self):
        with self.lock: # Закрываем дверь на замок, пока забираем товар
            if len(self.storage) > 0:
                product = self.storage.pop(0)
                print(f"[МАГАЗИН] Продал: {product}. Осталось: {len(self.storage)}")
                return product
            else:
                print("[МАГАЗИН] Товара нет, ждем завод...")
                return None

# 2. Что делает Завод (работает сам по себе)
def factory_worker(warehouse):
    products = ["Смартфон", "Ноутбук", "Наушники"]
    for _ in range(5): # Сделает 5 товаров
        product = random.choice(products)
        warehouse.add_product(product)
        time.sleep(1) # Отдыхает 1 секунду

# 3. What делает Магазин (работает сам по себе)
def shop_worker(warehouse):
    for _ in range(5): # Попробует продать 5 раз
        warehouse.remove_product()
        time.sleep(1.5) # Ждет покупателя 1.5 секунды

# 4. Главный запуск игры
if __name__ == "__main__":
    shared_warehouse = Warehouse() # Создаем один склад для всех

    # Включаем параллельные потоки (Завод и Магазин работают одновременно)
    potok_zavoda = threading.Thread(target=factory_worker, args=(shared_warehouse,))
    potok_magazina = threading.Thread(target=shop_worker, args=(shared_warehouse,))

    # Запускаем их!
    potok_zavoda.start()
    potok_magazina.start()

    # Ждем, пока они закончат
    potok_zavoda.join()
    potok_magazina.join()

    print("Симуляция окончена!")
