class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_list(self):
        p = self
        string = ""
        while p != None:
            string += str(p.val) + " "
            p = p.next
        print(string)

# utility function to create a linked list from a python list
def linked_list(arr):
    n = len(arr)
    if n == 0:
        return None
    elif n == 1:
        return Node(arr[0])

    head = Node(arr[0])
    p = head
    i = 1

    while i < n:
        node = Node(arr[i])
        p.next = node
        p = node
        i += 1

    return head

# algorithm to reverse a linked list, in place.
def reverse(node):
    if node == None or node.next == None:
        return node

    prev = None
    curr = node
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    node.next = None

    return prev


def test():
    a1 = [1,2,3,4,5]
    n1 = linked_list(a1)
    r1 = reverse(n1)
    r1.print_list()

if __name__ == '__main__':
    test()