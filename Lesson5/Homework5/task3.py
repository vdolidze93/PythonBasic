from string import punctuation

# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

user_input = input("Please enter your text: ")
PUNCTUATION_AND_SPACE = punctuation + " "
new_text = ["#"]

words = user_input.split(" ")

for word in words:
    for symbol in word.capitalize():
        if symbol not in PUNCTUATION_AND_SPACE:
            new_text[0] += symbol

result = str(new_text[0][:140])
print(len(result))
print(result)
