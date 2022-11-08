"""
binary search basicaly is spliting the set
of data in half until the searched data is found
"""


def binary_search(my_list, element):
    middle = 0
    start = 0
    end = len(my_list)
    steps = 0

    while start <= end:
        # Let's show how many steps it took
        print(f"Step {steps}: {list[start:end + 1]}")

        steps += 1
        middle = (start + end) // 2

        if element == my_list[middle]:
            return middle
        if element < my_list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return - 1


search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2

binary_search(search_list, target)
