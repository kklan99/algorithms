def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if not s or int(s) == 0:
        return 0
    memo = [0] * (len(s) + 1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2, len(s) + 1):
        if int(s[i-1]) > 0:
            memo[i] = memo[i-1]
        if int(s[i-2]) > 0 and int(s[i-2:i]) <= 26:
            memo[i] += memo[i-2]
     
    return memo[len(s)]

def main():
    print("Testing...")
    assert numDecodings("123") == 3
    assert numDecodings("01") == 1
    assert numDecodings("4444") == 1
    print("All tests pass!")

if __name__ == '__main__':
    main()