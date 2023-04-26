# https://youtu.be/V_T5NuccwRA
# find an element using BINARY search

print("Enter space seperated Numbers")
num_list = list(map(int, input().split()))

print("Enter a number which you want to find in list")
num = int(input())

def binary_search(num_list, num):
    n = len(num_list)

    num_list.sort() # sort the list first
    print(num_list, "new sorted array")

    l = 0   # Left Index
    r = n-1   # Right Index
    while l < r:
        mid = (l + r) // 2    # find mid value (floor)
        print(num_list[l:r+1], mid, num_list[mid])
        if num_list[mid] < num: # left sub array from mid
            l = mid + 1
        elif num_list[mid] > num:   # right sub array from mid
            r = mid - 1
        else:
            position = mid + 1
            return "Element found at {}".format(position) # mid element matches with num  

    return "Element Not found"

position = binary_search(num_list, num)

print(position)