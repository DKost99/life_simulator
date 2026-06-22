import threading
import time
import random

class Warehouse:
    """
    Класс, представляющий общий ресурс (Склад) для хранения товаров.
    Использует threading.Lock для безопасной работы в многопоточной среде.
    """
    def __init__(self):
        self.storage = []       

# Список для хранения товаров
    
        self.lock = threading.Lock()  
    
# Замок для синхронизации потоков

    def add_product(self, product):
        """Добавляет товар на склад."""
        with self.lock:
            self.storage.append(product)
            print(f"[ЗАВОД] Сделал: {product}. На складе: {len(self.storage)}")

    def remove_product(self):
        """Забирает товар со склада для продажи."""
        with self.lock:
            if len(self.storage) > 0:
                product = self.storage.pop(0)
                print(f"[МАГАЗИН] Продал: {product}. Осталось: {len(self.storage)}")
                return product
            else:
                print("[МАГАЗИН] Товара нет, ждем завод...")
                return None

def factory_worker(warehouse):
    """Функция потока-производителя (Завод)."""
    products = ["Смартфон", "Ноутбук", "Наушники"]
    for _ in range(5):
        product = random.choice(products)
        warehouse.add_product(product)
        time.sleep(1)

def shop_worker(warehouse):
    """Функция-потребитель (Магазин)."""
    for _ in range(5):
        warehouse.remove_product()
        time.sleep(1.5)

if __name__ == "__main__":
    
# Инициализация общего ресурса
    
    shared_warehouse = Warehouse()

# Создание параллельных потоков

    potok_zavoda = threading.Thread(target=factory_worker, args=(shared_warehouse,))
    potok_magazina = threading.Thread(target=shop_worker, args=(shared_warehouse,))

# Запуск потоков

    potok_zavoda.start()
    potok_magazina.start()

# Ожидание завершения работы потоков

    potok_zavoda.join()
    potok_magazina.join()

    print("Симуляция окончена!")
