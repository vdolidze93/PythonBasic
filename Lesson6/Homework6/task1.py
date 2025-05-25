from string import ascii_letters

# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
#
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
#
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# захист від некоректного вводу, порожнього, якщо навпаки літери

# Приклад:
# Copy code
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA


LETTERS = ascii_letters
DIRECTION_OF_SLICE = "+"

user_input = input("Please enter two letters divided by a hyphen (a-c):")

while True:
    if len(user_input) != 3:
        user_input = input("Incorrect input. Please enter two letters divided by a hyphen (a-c):")
    elif not user_input[0].isalpha() or not user_input[2].isalpha() or not ord(user_input[1]) == 45:
        user_input = input("Incorrect input. Please enter two letters divided by a hyphen (a-c):")
    else:
        first_letter = user_input[0]
        hyphen = user_input[1]
        second_letter = user_input[2]
        # перша літера велика, друга маленька - -
        # обидві великі літери - орд більший у першої - -
        # обидві маленькі літери - орд більший у першої - -
        if first_letter.isupper() and second_letter.islower():
            DIRECTION_OF_SLICE = "-"
        elif (first_letter.isupper() and second_letter.isupper()) and (ord(first_letter) > ord(second_letter)):
            DIRECTION_OF_SLICE = "-"
        elif (first_letter.islower() and second_letter.islower()) and (ord(first_letter) > ord(second_letter)):
            DIRECTION_OF_SLICE = "-"
        break


if DIRECTION_OF_SLICE == "+":
    result_text = LETTERS[LETTERS.find(first_letter):LETTERS.find(second_letter) + 1]
elif DIRECTION_OF_SLICE == "-" and second_letter == LETTERS[0]:
    result_text = LETTERS[LETTERS.find(first_letter)::-1]
else:
    result_text = LETTERS[LETTERS.find(first_letter):LETTERS.find(second_letter) - 1:-1]

print(LETTERS)
print(result_text)
