from math import sqrt

message: str = 'Добро пожаловать в самую лучшую программу для вычисления '\
               'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вывод."""
    if your_number <= 0:
        return

    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {CalculateSquareRoot(your_number)}')


calc(25.5)
