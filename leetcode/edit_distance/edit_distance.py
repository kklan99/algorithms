class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        
        # initialize dp matrix 
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        # Build up dp bottom up
        for i in range(m + 1):
            for j in range(n + 1):
                # if first string is empty then only operation would be
                # to insert every character.
                if i == 0:
                    dp[i][j] = j

                # same if second string is empty.
                elif j == 0:
                    dp[i][j] = i

                # we dont have to do anything if the two characters are the
                # same.
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                # if the last characters are different, then consider whether
                # to insert, replace, or replace.
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

        # return minimum edit distance.
        return dp[m][n]

def test():
    print("Testing algorithm...")
    s = Solution()
    # assert 3 == s.minDistance("saturday", "sunday")
    # assert 0 == s.minDistance("hello", "hello")
    assert 1 == s.minDistance("a", "b")
    print("All tests pass!")

if __name__ == '__main__':
    test()