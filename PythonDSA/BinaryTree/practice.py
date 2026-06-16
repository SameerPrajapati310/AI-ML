class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BottomView:
    def find(self,root,col,row,node):
        if root == None:
            return 
        node.append((col,row,root.val))
        self.find(root.left,col-1,row+1,node)
        self.find(root.right,col+1,row+1,node)
    def bottom(self,root):
        node = []
        self.find(root,0,0,node)
        node.sort()
        mp = {}
        for col,row,val in node:
            mp[col] = val
        ans = []
        sorted(mp)
        for key,index in mp.items():
            ans.append(index)
        return ans


"""        
        2
    3       4
5        3     6

"""

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(6)

ans = BottomView()
print(ans.bottom(root))