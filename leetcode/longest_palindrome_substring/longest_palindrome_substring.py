class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        # maximum length and start index
        max_len, start = 1, 0

        # Initialize 2d dp memo
        memo = [[False for j in range(n)] for i in range(n)]
        
        # Each character is considered a palindrome
        for i in range(n):
            memo[i][i] = True

        # Check for adjacent characters. If they are equal they are also
        # palindromic
        for i in range(n-1):
            if s[i] == s[i+1]:
                memo[i][i+1] = True
                max_len = 2
                start = i

        # Check for lengths greater than 2, k being length of substring.
        for k in range(3, n+1):
            # Set starting index
            for i in range(n-k+1):
                # Ending index of substring.
                j = i + k -1

                # If substr between i+1 and j-1 is palindromic, and i == j,
                # substr[i][j] is a palindrome
                if memo[i+1][j-1] and s[i] == s[j]:
                    memo[i][j] = True

                    # Check if current k is greater than max palindrome length.
                    # If it is, then update new longest palindromic substring.
                    if k > max_len:
                        max_len = k
                        start = i

        return s[start: start + max_len]



def main():
    sol = Solution()
    print(sol.longestPalindrome("babad"))
    print(sol.longestPalindrome("cbbc"))
    print(sol.longestPalindrome("asd;lfkj"))

if __name__ == "__main__":
    main()
