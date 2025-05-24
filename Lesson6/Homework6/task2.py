# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
#
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
#
# Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди повинні заповнюватися нулями
# при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек. Тобто використовуючи
# функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів, годин, хвилин, а те
# що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)
#
# Приклад:
# Copy code
# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

# 60 секунд
# 1 хвилина = 60 секунд
# 1 година = 60 * 60 секунд = 3600
# 1 день = 24 * 60 * 60 секунд = 86 400

user_input = input("Please enter a real number from 0 to 8 640 000:")
MIN_VALUE = 0
MAX_VALUE = 8640000
DAYS_SECONDS = 86400
HOURS_SECONDS = 3600
MINUTES_SECONDS = 60

while True:
    if not user_input.isnumeric():
        user_input = input("Incorrect input. Please enter a real number from 0 to 8 640 000:")
    elif int(user_input) < MIN_VALUE or int(user_input) > MAX_VALUE:
        user_input = input("Incorrect number. Please enter a real number from 0 to 8 640 000:")
    elif user_input.startswith("0") and len(user_input) > 1:
        user_input = input("Incorrect number. Please enter a real number from 0 to 8 640 000:")
    else:
        value = int(user_input)
        days = value // DAYS_SECONDS
        hours = (value - days*DAYS_SECONDS) // HOURS_SECONDS
        minutes = (value - days*DAYS_SECONDS - hours*HOURS_SECONDS) // MINUTES_SECONDS
        seconds = value - days*DAYS_SECONDS - hours*HOURS_SECONDS - minutes*MINUTES_SECONDS
        break

if str(days).endswith("1") and days != 11:
    days_print = "день"
elif not 11 <= days <= 14 and (str(days).endswith("2") or str(days).endswith("3") or str(days).endswith("4")):
    days_print = "дні"
else:
    days_print = "днів"


print(f"{days} {days_print}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
