class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class VerticalView:
    def find(self,root,col,row,nodes):
        if root == None:
            return 
        nodes.append((col,row,root.val))
        self.find(root.left,col-1,row+1,nodes)
        self.find(root.right,col+1,row+1,nodes)
    def vertical(self,root):
        node = []
        self.find(root,0,0,node)
        node.sort()
        ans = []
        pre_col = None

        for col,row,val in node:
            if pre_col != col:
                ans.append([])
                pre_col = col
            ans[-1].append(val)
        return ans


"""        

        2
    3       4
5        3       6

"""

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)

ans = VerticalView()
answer  = ans.vertical(root)
for it in answer:
    print(it)