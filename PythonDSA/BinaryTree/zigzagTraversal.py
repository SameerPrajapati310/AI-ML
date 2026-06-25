from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        answer = []
        if root == None:
            return answer
        q = deque([root])
        sign = True
        while q:
            ans = []
            for _ in range(len(q)):
                node = q.popleft()
                ans.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            if not sign:
                ans.reverse()
            answer.append(ans)
            sign = not sign
        return answer

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(10)
root.left.left.right = TreeNode(89)
root.left.right.right = TreeNode(3)
root.left.right.left = TreeNode(50)
root.left.right.right.right = TreeNode(5)
root.left.right.right.left = TreeNode(6)

