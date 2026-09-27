text = input("Введите текст: ")
start, end = map(int, input("Введите от какого до какого символа вывести (через пробел): ").split())
print(text[start - 1:end])