print("=== Использование пакета модулей ===")

from my_package import function1, function2

print(function1())
print(function2())

print("\n=== Альтернативный импорт пакета ===")
import my_package

print(my_package.function1())
print(my_package.function2())

print("\n=== Прямой импорт из подмодулей ===")
from my_package.module1 import helper_function
from my_package.module2 import another_function

print(helper_function())
print(another_function())

print("\n=== Информация о пакете ===")
print("Версия пакета:", my_package.__version__)
print("Автор пакета:", my_package.__author__)