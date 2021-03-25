def find_gt_lt_eq(my_list, num):
    gt = lt = eq = 0
    for item in my_list:
        if item == num:
            eq += 1
        elif item < num:
            lt += 1
        else:
            gt += 1
    return (gt, lt, eq)


my_list = [3, 4, 8, 10, 5, 1, 3, 6]
num = 5
gt, lt, eq = find_gt_lt_eq(my_list, num)

print("For this list:", my_list)
print("Number of items equal to {0:d} = {1:d}".format(num, eq))
print("Number of items less than {0:d} = {1:d}".format(num, lt))
print("Number of items greater than {0:d} = {1:d}".format(num, gt))
