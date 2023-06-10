class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str2tree(s):
    if not s:
        return None

    # Find the root value
    i = 0
    while i < len(s) and (s[i].isdigit() or s[i] == '-'):
        i += 1
    root_val = int(s[:i])
    root = TreeNode(root_val)

    # Check if there are left and right children
    if i < len(s):
        count = 0
        start = i

        # Find the substring that represents the left child
        while i < len(s):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1

            if count == 0:
                break
            i += 1

        root.left = str2tree(s[start + 1:i])

        # Check if there is a right child
        if i + 1 < len(s):
            root.right = str2tree(s[i + 2:len(s) - 1])

    return root


def inorderTraversal(root):
    if not root:
        return []

    result = []
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        result.append(root.val)
        root = root.right

    return result


s = "4(2(3)(1))(6(5))"
tree_root = str2tree(s)
inorder = inorderTraversal(tree_root)
print(inorder)  # Output: [3, 2, 1, 4, 5, 6] 
