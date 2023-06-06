#Создайте функцию генератор чисел Фибоначчи

def fibonacci_Generator():
    a = 0
    b = 1
    for i in range(10):
        yield b
        a, b = b, a + b




obj = fibonacci_Generator()

for i in range(10):
    print(next(obj))
