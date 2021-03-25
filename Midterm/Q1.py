def find_max_min(my_list):
    if len(my_list) == 0:
        return (None, None)
    elif len(my_list) == 1:
        return (my_list[0], my_list[0])
    else:
        max = min = my_list[0]
        for num in my_list:
            if num > max:
                max = num
            elif num < min:
                min = num
        return (max, min)


my_list = [1, 4, 2, 3, 5, 8, 7]
max, min = find_max_min(my_list)
print("In this list:", my_list)
print("The max value is:", max)
print("The min value is:", min)