class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find(self,inorder,target):
        idx = 0
        for i in range(len(inorder)):
            if inorder[i] == target:
                return i
        return -1
    def construct(self,preorder,inorder,idx,start,end):
        if start >  end:
            return None
        element = preorder[idx[0]]
        i = self.find(inorder, element)
        idx[0] += 1
        root = TreeNode(element)
        root.left = self.construct(preorder,inorder,idx,start,i-1)
        root.right = self.construct(preorder,inorder,idx,i+1,end)
        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder) - 1
        idx = [0] 
        return self.construct(preorder,inorder,idx,0,n)