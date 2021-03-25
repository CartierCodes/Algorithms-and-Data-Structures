def checker(A, B, sum):
    A = sorted(A)
    B = sorted(B)

    for e1 in A:
        for e2 in B:
            temp = e1+e2
            if (temp > sum):
                break
            if (temp == sum):
                return True


A = [5, 2, 4, 6]
B = [1, 7, 3, 8]
sum = 3

print(checker(A, B, sum))
