import random

# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
#
# Приклад:
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

random_elements_quantity = random.randint(3, 10)
given_list = []
iteration = 0

while iteration < random_elements_quantity:
    given_list.append(random.randint(1, 9))
    iteration += 1

print(given_list)

new_list = []
new_list_elements = 3
counter = 0

while counter < new_list_elements:
    if len(given_list) == 0 or len(given_list) == 1:
        new_list = given_list.copy()
        break
    match counter:
        case 0:
            new_list.append(given_list[0])
            counter += 1
        case 1:
            new_list.append(given_list[2])
            counter += 1
        case 2:
            new_list.append(given_list[-2])
            counter += 1

print(new_list)
