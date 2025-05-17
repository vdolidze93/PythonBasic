user_input = int(input("Enter a number that consists of 4 digits: "))

first_number = user_input // 1000
second_number = (user_input - first_number * 1000) // 100
third_number = (user_input - first_number * 1000 - second_number * 100) // 10
fourth_number = user_input - first_number * 1000 - second_number * 100 - third_number * 10

print(first_number)
print(second_number)
print(third_number)
print(fourth_number)
#___________________

user_input_option2 = int(input("Enter a number that consists of 4 digits: "))

first_number2 = user_input_option2 // 1000
second_number2 = user_input_option2 % 1000 // 100
third_number2 = user_input_option2 % 1000 % 100 // 10
fourth_number2 = user_input_option2 % 10

print(first_number2)
print(second_number2)
print(third_number2)
print(fourth_number2)
