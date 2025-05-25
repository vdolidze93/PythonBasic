# Ваше завдання — написати програму, яка перемножує всі цифри,
# введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.

# Користувач вводить число з клавіатури.
# Приклади:
# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729,
# Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

user_input = input("Please enter a real number:")


while True:
    if not user_input.isnumeric():
        user_input = input("Incorrect input. Please enter a real number:")
    elif user_input.startswith("0") and len(user_input) > 1:
        user_input = input("Incorrect number. Please enter a real number:")
    else:
        break

result = 1
iteration = 0

while int(user_input) > 9 or iteration == 0:
    for number in user_input:
        result *= int(number)
    iteration += 1
    user_input = str(result)
    if result > 9:
        result = 1

print(result)
