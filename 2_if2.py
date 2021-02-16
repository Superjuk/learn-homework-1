"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def compare(str1 = '', str2 = ''):
    if type(str1) != str or type(str2) != str:
        return 0

    if str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3
    else:
        return -1

def main():
    print(compare(1, 'test'))
    print(compare('test1', 2.5))
    print(compare('same', 'same'))
    print(compare('longer', 'short'))
    print(compare('pypy', 'learn'))
    print(compare('learn', 'pypy'))
    print(compare('cpython', 'python3'))
    print(compare())


if __name__ == "__main__":
    main()
