class Fenwick:
    """
    Fenwick tree implementation aka Binary Indexed Tree in python. Given an
    array with a set range, calculate the prefix sum n (sum of elements from
    index 0 to n) in log(n) time. Also, update the prefix sum in log(n) time.
    It is important to know that the indexes in BIT for arr[i] is i + 1. This
    is because BIT[i+1] represents the sum for the first i elements.

    Implementation inspired from 
    http://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
    """
    def __init__(self, arr, n):
        """
        Constructs and returns a Binary Indexed tree for a given array of 
        size n.
        """
        self.BITree = [0] * (n+1)
        self.size = n

        for i in range(n):
            self.update(i, arr[i])

    def get_sum(self, i):
        """
        Returns the sum of arr[0..index] in log time. When you calculate the
        sum you go DOWN the binary indexed tree.
        """
        s = 0

        # index in BITree is 1 more than index in arr[]
        i += 1

        # Traverse to leaves of BITree[i]:
        while i > 0:
            s += self.BITree[i]

            # Move index to parent node (next set bit in binary representation)
            i -= i & (-i)

        return s

    def update(self, i, v):
        """
        Updates a node in BITree at index i by adding value v to all ancestors
        in tree. Propogates UP the binary tree.
        """
        # index in BTree is 1 more than index in arr[]
        i += 1

        # Traverse to ancestors of BITree[i]
        while i <= self.size:
            self.BITree[i] += v

            # Update index to next set bit in binary representation
            i += i & (-i)

def main():
    print("Testing Fenwick Tree...")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Testing with array: " + str(arr))
    fenwick = Fenwick(arr, len(arr))
    print("Sum of elements in arr[0..5]: " + str(fenwick.get_sum(5)))
    print("Updating arr[3] by 6...")
    fenwick.update(3, 6)
    print("Sum of elements in arr[0..5]: " + str(fenwick.get_sum(5)))
    print("Tests complete!")

if __name__ == '__main__':
    main()
