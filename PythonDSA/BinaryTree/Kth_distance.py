"""
Given a binary tree, a target node, and an integer K, 
return all nodes that are at distance K from the target node.

         4
        /
       2
      / \
     5   10
      \  / \
      89 50 3
            / \
           6   5
k = 2
node 5:

Distance 0 : 5
Distance 1 : 89, 2
Distance 2 : 4, 10

Output:
[4, 10]

"""

class TreeNode:
    def __init__(self,val=0,left=None,right = None):
        self.val = val
        self.right = right
        self.left = left
from collections import deque
class Solution:
    def find_parent(self,root,parent):
        q = deque([root])
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                    parent[node.left] = node
                if node.right != None:
                    q.append(node.right)
                    parent[node.right] = node

        
    def find(self,root,k,target):
        ans = []
        parent = {}
        self.find_parent(root,parent)
        visited = {}
        q = deque([target])
        visited[target] = True
        count = 0
        while q:
            size = len(q)
            if count == k:
                break 
            count += 1
            for _ in range(size):
                node = q.popleft()
                if node.left != None and node.left not in visited:
                    q.append(node.left)
                    visited[node.left] = True
                if node.right != None and node.right not in visited:
                    q.append(node.right)
                    visited[node.right] = True
                if node in parent and parent[node] not in visited:
                    q.append(parent[node])
                    visited[parent[node]] = True
        while q:
            node = q.popleft()
            ans.append(node.val)
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

k = 2
target = root.left.left

ans = Solution()
print(ans.find(root,k,target))