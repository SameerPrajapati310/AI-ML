class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Topview:
    def find(self,root,row,col,node):
        if root == None:
            return 
        node.append((col,row,root.val))
        self.find(root.left,row+1,col-1,node)
        self.find(root.right,row+1,col+1,node)
        
        pass
    def topviewFind(self,root):
        node = []
        self.find(root,0,0,node)
        node.sort()
        ans = []
        pre_col = None
        for col,row,val in node:
            if col != pre_col:
                ans.append(val)
                pre_col = col
        return ans
            


root = TreeNode(2)

root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)

answer = Topview()
print(answer.topviewFind(root))