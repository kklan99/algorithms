def binary_search_iterative(arr, val, left, right):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == val:
            return mid

        elif arr[mid] < val:
            left = mid + 1

        else:
            right = mid - 1

    return -1

def binary_search(arr, val, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == val:
        return mid

    elif arr[mid] < val:
        return binary_search(arr, val, mid + 1, right)

    else:
        return binary_search(arr, val, left, mid - 1)

def test():
    a1 = [1, 3, 5, 7, 9, 10]
    l1 = len(a1)
    assert 0 == binary_search_iterative(a1, 1, 0, l1 - 1)
    assert 0 == binary_search(a1, 1, 0, l1 - 1)

    assert 4 == binary_search_iterative(a1, 9, 0, l1 - 1)
    assert 4 == binary_search(a1, 9, 0, l1 - 1)

    print("All tests pass!")

if __name__ == '__main__':
    test()