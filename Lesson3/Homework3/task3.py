# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

given_list = [1, 2, 3, 4, 5, 6, 7]

first_part_list = []
second_part_list = []
result_list = []

if (len(given_list) % 2) == 0 and (len(given_list) > 0):
    first_part_list = given_list[:len(given_list)//2]
    second_part_list = given_list[len(given_list)//2:]
    result_list.append(first_part_list)
    result_list.append(second_part_list)
elif (len(given_list) % 2 != 0) and (len(given_list) > 0):
    first_part_list = given_list[:len(given_list)//2 + 1]
    second_part_list = given_list[len(first_part_list):]
    result_list.append(first_part_list)
    result_list.append(second_part_list)
else:
    result_list.append(given_list)
    result_list.append([])

print(given_list)
print(result_list)
