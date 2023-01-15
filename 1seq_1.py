user_list = int(input("Введите количество элементов: "))
print_list = []

for i in range(user_list):
    num = int(input(f'Введите {i+1} символ: '))
    print_list.append(num)

print_list.sort()
print(print_list)
