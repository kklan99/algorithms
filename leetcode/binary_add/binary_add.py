def binary_add(a, b):
    i = len(a) - 1
    j = len(b) - 1

    sum_str = ""
    carry = 0

    while i >= 0 or j >= 0:
        d1 = int(a[i]) if i >= 0 else 0
        d2 = int(b[j]) if j >= 0 else 0
        total = d1 + d2 + carry

        if total >= 2:
            carry = total // 2
            total -= 2

        sum_str = str(total) + sum_str
        i -= 1
        j -= 1

    if carry == 1:
        sum_str = str(1) + sum_str

    return sum_str

def main():
    print("Testing....")
    print("Asserting 111 + 111 == 1110")
    print(binary_add("111","111"))
    assert binary_add("111", "111") == "1110"
    print("True!")
    print("Asserting 100 + 1 == 101")
    print(binary_add("100", "1"))
    assert binary_add("100", "1") == "101"
    print("True!")

if __name__ == '__main__':
    main()
