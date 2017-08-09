def longest_common_prefix(strs):
    if strs == []:
        return ""

    # Find minimum length string, because the longest prefix will be found in
    # the shortest string.
    min_str = min(strs, key=len)
    prefix = ""
    low, high = 0, len(min_str) - 1

    # Do binary search on min_str, finding the longest common prefix matching
    # all the strings in strs
    while low <= high:
        mid = low + (high - low) // 2
        substr = min_str[0:mid+1]
        if all_contain_prefix(strs, substr, mid):
            prefix = substr
            low = mid + 1
        else:
            high = mid - 1

    return prefix


def all_contain_prefix(strs, prefix, p):
    for s in strs:
        if prefix != s[0:p+1]:
            return False

    return True

def main():
    print("Starting Test....")
    
    strs1 = ["abcdef", "abceqerqe", "abpqoeiu", "abcdefghi"]
    a1 = longest_common_prefix(strs1)
    assert "ab" == a1

    strs2 = ["ca", "a"]
    a2 = longest_common_prefix(strs2)
    assert "" == a2

    print("Tests pass!")

if __name__ == '__main__':
    main()