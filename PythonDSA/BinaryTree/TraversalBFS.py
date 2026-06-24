class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def bfs(self,root):
        ans = []
        if root == None:
            return ans
        from collections import deque
        q = deque()
        q.append(root)
        ans.append(root.val)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                ans.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
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


answer = TreeNode()
ans = answer.bfs(root)
print(ans)