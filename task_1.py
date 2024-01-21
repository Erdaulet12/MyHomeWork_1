"""task_1.py"""


def plus_two(number):
    """
    прибавляет к заданному числу +2

    Args:
        number (int): заданное число

    Returns:
        int: результат
    """
    try:
        result = number + 2
        return result
    except TypeError:
        print("Ожидаемый тип данных — число!")


if __name__ == "__main__":
    try:
        number = int(input("Введите число: "))
        print(plus_two(number))
    except ValueError:
        print("Ожидаемый тип данных — число!")
