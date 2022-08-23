# This program is relating to sorting list problem


def list_sort(l1):
    for i in range(len(l1)):
        for j in range(len(l1)-1):
            if l1[j] > l1[j+1]:
                tempo = l1[j+1]
                l1[j+1] = l1[j]
                l1[j] = tempo
    return l1
l1 = [2, 4, 1, 5]
l2 = [9, 2, 5, 1, 10, 19, 3]
print("In the name of Allah. \n")
print(list_sort(l1))
print(list_sort(l2))
l3 = l1 + l2
print(list_sort(l3))