text = input("Введите текст: ")
word = input("Введите слово для поиска: ")
count = text.count(word)
first_index = text.find(word)
print("Количество встреченных слов:", count)
if first_index != -1:
    print("Индекс первого встреченного слова:", first_index)
else:
    print("Слово в тексте не найдено")
print("Строка без слова:", text.replace(word, ""))