import datetime
from datetime import date
from datetime import date as d

print("=== Импорт всего модуля datetime ===")
birthday = datetime.date(2017, 6, 1)
print(birthday)

x = datetime.datetime.now()
print("Текущий год:", x.year)
print("Текущая дата:", x.year, x.month, x.day)
print("Текущее время:", x.hour, "часов", x.minute, "минут", x.second, "секунд")

print("\n=== Импорт конкретной функции ===")
birthday = date(2017, 6, 1)
print(birthday)

print("\n=== Импорт с переименованием ===")
birthday = d(2017, 6, 1)
print(birthday)

print("\n=== Работа с различными параметрами ===")
current_time = datetime.datetime.now()
print("Год:", current_time.year)
print("Месяц:", current_time.month)
print("День:", current_time.day)
print("Час:", current_time.hour)
print("Минута:", current_time.minute)
print("Секунда:", current_time.second)

print("\n=== Использование пользовательского модуля ===")
import my_module

print(my_module.greet("Алексей"))
print("Площадь круга радиусом 5:", my_module.calculate_area(5))
print("Число 10 четное?", my_module.is_even(10))
print("Факториал 5:", my_module.factorial(5))
print("Версия модуля:", my_module.version)
print("Автор:", my_module.author)

print("\n=== Альтернативный импорт ===")
from my_module import greet, calculate_area

print(greet("Мария"))
print("Площадь круга радиусом 3:", calculate_area(3))

print("\n=== Импорт с переименованием ===")
from my_module import greet as hello, calculate_area as area

print(hello("Петр"))
print("Площадь круга радиусом 7:", area(7))