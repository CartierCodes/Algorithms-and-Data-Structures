# Carter Burzlaff - PP Chapter 5

def merge(list1, list2):
    list3 = []
    while len(list1) > 0 or len(list2) > 0:
        if len(list1) > 0 and len(list2) == 0:
            for i in range(len(list1)):
                list3.append(list1.pop(0))
        elif len(list2) > 0 and len(list1) == 0:
            for j in range(len(list2)):
                list3.append(list2.pop(0))
        elif list1[0] <= list2[0]:
            list3.append(list1.pop(0))
        elif list2[0] <= list1[0]:
            list3.append(list2.pop(0))
        
    return list3

testList1 = [1, 3, 5, 7, 8, 10]
testList2 = [2, 4, 5, 6]
print(merge(testList1, testList2))