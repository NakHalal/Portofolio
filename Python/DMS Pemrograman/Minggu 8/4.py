my_list = [int(i) for i in input().split()]

my_list.sort()
median = my_list[len(my_list) // 2]
if len(my_list) % 2 == 0:
    median = (median + my_list[(len(my_list) // 2) - 1]) / 2
print(median)
