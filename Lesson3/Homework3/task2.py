# Приклади:
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10

given_list = [12, 3, 4, 10, 8]
result_list = []

if len(given_list) > 1:
    given_list.insert(0, given_list[-1])
    given_list.pop()

print(given_list)
