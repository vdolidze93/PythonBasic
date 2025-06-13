# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range)
# для 100 елементів, за наступними правилом:
#
# Один список з числами кратними 3, інший з кратними числами 5.
#
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
#
# Функція повинна повернути цю множину як результат своєї роботи.

# Copy code
#
# def common_elements():
# 		pass
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# ДЗ необхідно здати наступним чином:

def common_elements():
    first_list = [i for i in range(0, 100) if i % 3 == 0]
    second_list = [i for i in range(0, 100) if i % 5 == 0]

    return set(first_list).intersection(set(second_list))

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")