class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Index(object):
    def __init__(self, i):
        self.i = i

def construct(inorder, postorder, inStart, inEnd, index):
    # Base case
    if inStart > inEnd:
        return None

    TreeNode node = TreeNode(postorder[index.i])
    index.i -= 1

    if inStart == inEnd:
        return node

    rootIndex = inorder[inStart:inEnd+1].index(node.val)

    node.right = construct(inorder, postorder, rootIndex + 1, inEnd, index)
    node.left = construct(inorder, postorder, inStart, rootIndex - 1, index)

    return node

def construct_pre_in(inorder, postorder):
    if len(inorder) != len(postorder):
        raise ValueError('Inorder and postorder lengths are not equal!')

    n = len(inorder)
    # Initialize postorder index to be the last element of postorder
    index = Index(n - 1)

    return construct(inorder, postorder, 0, n - 1, index)

def test():
    inorder = [4,8,2,5,1,6,3,7]
    postorder = [8,4,5,2,6,7,3,1]

    