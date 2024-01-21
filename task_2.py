"""task_2.py"""


def get_element(array: list, index: int):
    """
    Пытается получить доступ к индексу элемента

    Args:
        array (list): _description_
        index (int): _description_

    Returns:
        int: _description_
    """
    try:
        return array[index]
    except IndexError:
        return "Индекс выходит за границы массива"


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    index = int(input("Введите индекс: "))
    print(get_element(array, index))
