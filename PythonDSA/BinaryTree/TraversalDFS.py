class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFS:
    def find(self, root, ans):
        if root == None:
            return ans

        ans.append(root.val)
        self.find(root.left, ans)
        self.find(root.right, ans)

        return ans

    def dfs_traversal(self, root):
        ans = []
        self.find(root, ans)
        return ans


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(10)
root.left.left.right = TreeNode(89)
root.left.right.right = TreeNode(3)
root.left.right.left = TreeNode(50)
root.left.right.right.right = TreeNode(5)
root.left.right.right.left = TreeNode(6)

answer = DFS()

print(answer.dfs_traversal(root))