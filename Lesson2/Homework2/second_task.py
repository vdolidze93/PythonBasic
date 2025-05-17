user_input = int(input("Enter a positive number that consists of 5 digits: "))

first_from_back = user_input % 10
second_from_back = user_input % 100 // 10
third_from_back = user_input  // 100 % 10
fourth_from_back = user_input // 1000 % 10
fifth_from_back = user_input // 10000

print(first_from_back)
print(second_from_back)
print(third_from_back)
print(fourth_from_back)
print(fifth_from_back)
