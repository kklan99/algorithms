class Solution(object):
    def generateParentheses(self, n):
        if n == 0 :
            return []
        lst = []
        self.generate(lst, "", n, 0, 0)
        return lst

    def generate(self, lst, s, n, o, c):
        # If number of closed parentheses == n, then add s to the list.
        if c == n:
            lst.append(s)
            return

        # If open paren count is greater than closed paren count, add a closed
        # paren to s and call generate again. If open count is less than n, add
        # another open paren to s.
        if o > c:
            self.generate(lst, s+ ')' , n, o, c+1)
        if o < n:
            self.generate(lst, s + '(', n, o+1, c)

def main():
    sol = Solution()
    print(sol.generateParentheses(3))

if __name__ == '__main__':
    main()