"""
Плюсы pickle:
- простота использования
-
Минусы pickle:
- десериализация данных из непроверенных источников небезопасна
"""

import pickle


# Создаем простой класс Employee c одним методом, который определяет
# три атрибута для экземпляров класса; name, department, salary.
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary


# Далее создаем объект класса Employee и записываем в переменную alice и
# используя модуль pickle, записываем созданный объект в файл alice.pickle как последовательность байт
if __name__ == "__main__":
    alice = Employee("Alice", "DevOps", 10000)
    with open('../tmp/alice.pickle', 'wb') as a:
        pickle.dump(alice, a)
# После этого можно запустить файл hw14_other.py, в котором выполняется чтение файла alice.pickle
# и преобразование байтов обратно в объект класса Employee
