# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
#
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво
# без урахування знаків пунктуації та розмірності букв.
#
# Функція приймає на вхід рядок, та повертає булеве значення True або False
#
# Приклад:

# Copy code
# def is_palindrome(text):
#     pass
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

from string import punctuation


PUNCTUATION_AND_SPACE = punctuation + " "


def is_palindrome(text):
    given_text = text

    for symbol in PUNCTUATION_AND_SPACE:
        if given_text.find(symbol) != -1:
            given_text = given_text.replace(symbol, '')

    if given_text.lower() == given_text[::-1].lower():
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")