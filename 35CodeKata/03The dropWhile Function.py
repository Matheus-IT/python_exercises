def isEven(num):
    return num % 2 == 0


def dropWhile(arr, func):
    i = 0
    len_arr = len(arr)
    while i < len_arr and func(arr[i]):
        i += 1
    return arr[i:]


arr = [2, 4, 6, 8, 1, 2, 5, 4, 3, 2]

assert dropWhile(arr, isEven) == [1, 2, 5, 4, 3, 2]  # True
