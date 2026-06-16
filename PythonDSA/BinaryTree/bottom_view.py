class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class BottomView:
    def find(self, root, row, col, nodes):
        if root is None:
            return
        nodes.append((col, row, root.val))

        self.find(root.left, row + 1, col - 1, nodes)
        self.find(root.right, row + 1, col + 1, nodes)
    def bottomViewFind(self, root):
        nodes = []
        self.find(root, 0, 0, nodes)
        nodes.sort()
        mp = {}
        for col, row, val in nodes:
            mp[col] = val   
        ans = []

        for col in sorted(mp):
            ans.append(mp[col])

        return ans
    
root = TreeNode(2)

root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)

answer = BottomView()
print(answer.bottomViewFind(root))