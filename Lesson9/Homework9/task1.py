# На вхід функції popular_words передаються два аргументи. Текст та список слів, популярність яких необхідно визначити.
#
# При вирішенні цього завдання зверніть увагу на такі моменти
#
# Слова необхідно шукати у всіх регістрах. Тобто. якщо необхідно знайти слово "one", значить
# для нього будуть підходити слова "one", "One", "oNe", "ONE" і т.д.
# Шукані слова завжди вказані в нижньому регістрі
# Якщо слово не знайдено жодного разу, його необхідно повернути у словнику зі значенням 0 (нуль)
# Вхідні параметри: Текст і масив слів, що шукаються.
#
# Вихідні параметри: Словник, у якому ключами є шукані слова та значеннями, скільки разів кожнє
# слово зустрічаються у орігінальному тексті.
#
# Приклад:
#
# Copy code
# def popular_words (text, words):
#     pass
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
#                      ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')


def popular_words (text, words):
    founds_counter_dict = {}
    words_list = text.lower().split(' ')

    for word in words:
        if word not in words_list:
            founds_counter_dict.update({word: 0})
        else:
           founds_counter_dict.update({word: words_list.count(word)})

    return founds_counter_dict

assert popular_words("When I was One I had just begun When I was Two I was nearly new ",
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
