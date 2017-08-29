def nextGreaterElement(findNums, nums):
    # mapping of elements in nums to their next greater element, if it exists.
    mapping = {}
    # stack to represent all the previous elements in nums that we have encountered.
    stack = []
    # list of next greater elements
    nexts = []

    for elem in nums:
        # if the stack is not empty and the top element is smaller than the
        # current element, then that means that the current element is the
        # next greater element for the top element.
        while len(stack) > 0 and stack[-1] < elem:
            mapping[stack.pop()] = elem

        # We've already considered elem for all possible next greatest nums,
        # add elem to the stack.
        stack.append(elem)

    for elem in findNums:
        # Check mapping to see if elem has a next greater element. If it does
        # not, then set a -1. 
        nexts.append(mapping.get(elem, -1))

    return nexts

def main():
    print("Testing nextGreaterElement....")
    n1 = [1,3,4,2]
    fn1 = [4,1,2]
    expected1 = [-1,3,-1]
    assert nextGreaterElement(fn1, n1) == expected1
    print("All tests pass!")

if __name__ == '__main__':
    main()