"""Given a binary tree and a target node value, return the"
 path from the root node to the target node.
 
 Input:
        1
       / \
      2   3
     / \
    4   5
       / \
      6   7

target = 7

Output:
[1, 2, 5, 7]]

 """




class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class RTL:
    def find(self, root, target, ans):
        if root is None:
            return False

        if root.val == target:
            ans.append(root.val)
            return True

        ans.append(root.val)

        left = self.find(root.left, target, ans)
        right = self.find(root.right, target, ans)

        if left or right:
            return True

        ans.pop()
        return False

    def rootleaf(self, root):
        ans = []
        self.find(root, 7, ans)
        return ans
    
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)

ans = RTL()
print(ans.rootleaf(root))
print()