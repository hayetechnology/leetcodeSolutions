def search(l1, l2, target):
    for x in range(0, len(l1)):
        for y in range(0, len(l2)):
            if l1[x] + l2[y] == target:
                return x, y
    return None


list1 = [1, 17, 3, 4, 6, 2]
list2 = [5, 8, 21, 5, 18, 12]

target_num = 100

print(search(list1, list2, target_num))
