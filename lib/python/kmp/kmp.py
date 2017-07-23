# General implementation for Knuth Morris Pratt Pattern Searching algorithm.
# This algorithm is used to find a pattern or substring in an array/string

def kmp(s):
    """
    Given a concatenated string s with unique identifier, return a table
    F such that F[i] is the longest proper prefix of s[0..i] as well as 
    a suffix of s[0..i]
    """
    n = len(s)

    if n == 0:
        return []

    F = [0] * n

    for i in range(1, n):
        # Set k to the length of the longest proper prefix that is also
        # a suffix of s[0..i-1].
        k = F[i - 1]
        # Attempt to shorten the prefix as little as possible such that the
        # prefix and suffix can both be extended by the same character  
        while k > 0 and s[k] != s[i]:
            # The property s[0..k-1] == s[i-k..i-1] holds because s[0..k-1]
            # is the longest proper prefix that is equal to the suffix of 
            # s[0..i-1]. We further break this problem down by looking at the
            # s[0..k-1]. One proper prefix of s[0..k-1] is s[0..k-2]. Because
            # s[0..k-1] == s[i-k..i-1], s[0..k-2] can also act as the proper
            # prefix for s[i].
            k = F[k-1]
        if s[k] == s[i]:
            k += 1

        F[i] = k

    return F

def substr(s, substr, seperator='#'):
    """
    Checks if SUBSTR is a substring of S.
    """
    m = len(substr)
    s = substr + seperator + s
    F = kmp(s)
    return any([i == m for i in F])