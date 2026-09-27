full_name = input("Введите ФИО через пробел: ")
surname, name, patronymic = full_name.split()
formatted = f"{surname.capitalize()} {name.capitalize()} {patronymic.capitalize()}"
print("Добро пожаловать", formatted)
