def range_find(l1, target):
    left = mid = right = 0

    while left <= len(l1) and l1[left] is not target:
        left = left + 1
        mid = mid + 1
        right = right + 1

    if (left + 1) == len(l1) - 1:
        right = right + 1

        if list1[right] == target:
            return left, right
        return left, mid

    if (left + 2) == len(l1) - 1:
        mid = mid + 1
        right = right + 2
        if list1[mid] == target and list1[right] == target:
            return left, right
        elif list1[mid] == target:
            return left, mid
        else:
            return left, left

    mid = mid + 1
    right = right + 2

    while list1[right] == target and right <= len(l1) - 2:
        mid = mid + 1
        right = right + 1

    if list1[right] == target:
        return left, right
    if list1[mid] == target:
        return left, mid
    if list1[left] == target:
        return left, left


list1 = [13, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8]

print(range_find(list1, 13))
