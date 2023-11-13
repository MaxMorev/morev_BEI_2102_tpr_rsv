import asyncio
from clickhouse_driver import Client
import multiprocessing
# import threading
# import random
# import time
#
# class Warrior:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.lock = threading.Lock()
#
#     def attack(self, enemy):
#         damage = 20
#         with self.lock:
#             if enemy.health > 0:
#                 enemy.health -= damage
#                 if enemy.health < 0:
#                     enemy.health = 0
#                 print(f"{self.name} атакует {enemy.name}. {enemy.name} осталось здоровья: {enemy.health}")
#                 time.sleep(random.uniform(0.5, 1))
#                 if enemy.health == 0:
#                     print(f"{self.name} одержал победу!")
#
# def battle(warrior1, warrior2):
#     while warrior1.health > 0 and warrior2.health > 0:
#         attacker = random.choice([warrior1, warrior2])
#         enemy = warrior2 if attacker == warrior1 else warrior1
#         attacker.attack(enemy)
#
# if __name__ == "__main__":
#     warrior1 = Warrior("Воин 1")
#     warrior2 = Warrior("Воин 2")
#
#     battle_thread = threading.Thread(target=battle, args=(warrior1, warrior2))
#     battle_thread.start()
#     battle_thread.join()





# async def execute_clickhouse_query(query, query_number, delay=0):
#     await asyncio.sleep(delay)  # Имитация задержки
#     client = Client(host='g2.plzvpn.ru',
#                     user='default',
#                     password='1',
#                     port=9000,  # Remove quotes around port number
#                     database='test',
#                     settings={'use_numpy': True})
#     result = client.execute(query)
#     print(f"Запрос {query_number} завершён с задержкой {delay} секунд.")
#     return result
#
# async def main():
#     query1 = "SELECT * FROM Tabl8"
#     query2 = "SELECT * FROM Tabl8"
#
#     # Запускаем оба запроса асинхронно
#     task1 = asyncio.create_task(execute_clickhouse_query(query1, 1, delay=2))
#     task2 = asyncio.create_task(execute_clickhouse_query(query2, 2))
#
#     # Ожидаем завершения обоих запросов
#     await asyncio.gather(task1, task2)  # Use asyncio.gather to wait for both tasks
#
#     return task1.result(), task2.result()
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     results1, results2 = loop.run_until_complete(main())
#     print("Результат запроса 1:", results1)
#     print("Результат запроса 2:", results2)


def execute_query(query):
    client = Client(host='g2.plzvpn.ru',
                    user = 'default',
                    password = '1',
                    port='9000',
                    database = 'test',
                    settings={'use_numpy':True})
    result = client.execute(query)
    for row in result:
        print(row)

if __name__ == '__main__':
    queries = [
        'SELECT * from Tabl8',
        'SELECT * from Goroda LIMIT 4',
    ]

    pool = multiprocessing.Pool(processes=len(queries))

    pool.map(execute_query,queries)

    pool.close()
    pool.join()

