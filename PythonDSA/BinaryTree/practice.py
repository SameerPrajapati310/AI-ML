class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
class TopView:
    def find(self,root,col,row,node):
        if root == None:
            return 
        node.append((col,row,root.val))
        self.find(root.left,col-1,row+1,node)
        self.find(root.right,col+1,row+1,node)
    def topviewFind(self,root):
        node = []
        self.find(root,0,0,node)
        node.sort()
        pre_col = None
        ans = []
        for col,row,val in node:
            if pre_col != col:
                ans.append(val)
                pre_col = col
        return ans


root = TreeNode(2)

root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)

answer = TopView()
print(answer.topviewFind(root))

