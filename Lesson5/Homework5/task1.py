from keyword import kwlist
from string import punctuation

# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.


KEYWORDS = kwlist
PUNCTUATION_AND_SPACE = punctuation + " "

user_input = input("Please enter the name for a variable: ")
result = True


if (user_input[0] != '_') and (user_input[0].isalpha() != True):
    result = False


if len(user_input) > 1 and user_input[1] == "_":
    result = False


if user_input != user_input.lower():
    result = False


for symbol in PUNCTUATION_AND_SPACE.replace("_", ""):
    if user_input.find(symbol) != -1:
        result = False


for keyword in KEYWORDS:
    if user_input == keyword:
        result = False

print(result)
