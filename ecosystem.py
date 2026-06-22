import threading
import time

class Ecosystem:
    """
    Класс, представляющий общую среду обитания (Экосистему).
    Управляет ресурсами (Травой/Пищей) с помощью потокобезопасного Lock.
    """
    def __init__(self, initial_food):
        self.food_supply = initial_food
        self.lock = threading.Lock() # Замок для безопасного доступа разных популяций

    def get_food(self, amount):
        """
        Потокобезопасный метод извлечения еды из экосистемы.
        """
        with self.lock:  # Блокируем ресурс на время изменения данных
            if self.food_supply >= amount:
                self.food_supply -= amount
                print(f"[ЭКОСИСТЕМА] Популяция забрала {amount} еды. Осталось в среде: {self.food_supply}")
                return amount
            elif self.food_supply > 0:
                available = self.food_supply
                self.food_supply = 0
                print(f"[ЭКОСИСТЕМА] Забрали последние {available} еды. Среда истощена!")
                return available
            else:
                return 0

    def regenerate(self):
        """
        Метод симулирует рост травы/прирост ресурсов в экосистеме.
        """
        for _ in range(3):
            time.sleep(1)  # Время на рост ресурсов
            with self.lock:
                self.food_supply += 20
                print(f" [ЭКОСИСТЕМА] Ресурсы восстановились! Добавлено 20 еды. Всего: {self.food_supply}")
