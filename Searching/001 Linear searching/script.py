# Find an element in an array

print("Enter space seperated Numbers")
num_list = list(map(int, input().split()))

print("Enter a number which you want to find in list")
num = int(input())

def get_position_of_element(num_list, num):
    n = len(num_list)
    for i in range(n):
        if num_list[i] == num:
            return "Element found at {}".format(i + 1)
    return "Element Not Found"

print()
position = get_position_of_element(num_list, num)

print(position)