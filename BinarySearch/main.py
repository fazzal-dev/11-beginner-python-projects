

def binary_search(list, target):

    mid = 0
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        list.sort()
        print("Step", steps, ":", str(list[start:end+1]))

        steps += 1
        mid = (start + end) // 2
        if target == list[mid]:
            return mid
        if target < list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_search(my_list, 9)
