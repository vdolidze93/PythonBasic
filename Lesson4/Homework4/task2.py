# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

given_list = []
result = 0

for i in range(0, len(given_list), 2):
    if len(given_list) == 0:
        break
    result += given_list[i]

if len(given_list) != 0:
    result *= given_list[-1]

print(result)
