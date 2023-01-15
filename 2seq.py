user_list = input("Введите элементы через запятую: ")
user_list_2 = user_list.split(',')

one_time_list = []

for i in (user_list_2):
    if user_list_2.count(i) == 1:
        one_time_list.append(i)

print(one_time_list)
