class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left != None and right != None:
            return root

        if left != None and right == None:
            return left

        if left == None and right != None:
            return right

        return None


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(10)
root.left.left.right = TreeNode(89)
root.left.right.right = TreeNode(3)
root.left.right.left = TreeNode(50)
root.left.right.right.right = TreeNode(5)
root.left.right.right.left = TreeNode(6)


p = root.left.left.right         
q = root.left.right.left        

ans = Solution().lowestCommonAncestor(root, p, q)

print(ans.val)