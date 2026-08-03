class Traversal:
    def Preorder(self,node,ans):
        if node == None:
            return
        ans.append(node.val)
        self.Preorder(node.left,ans)
        self.Preorder(node.right,ans)

    def Bfs(self,node):
        if node == None:
            return node
        from collections import deque
        q = deque()
        q.append(node)
        answer = []
        while q:
            size = len(q)
            ans = []
            for _ in range(size):
                n  = q.popleft()
                ans.append(n.val)
                if n.left != None:
                    q.append(n.left)
                if n.right != None:
                    q.append(n.right)
            answer.append(ans)
        return answer
    def zigzag(self,node):
        if node ==None:
            return []
        from collections import deque
        q = deque()
        q.append(node)
        answer = []
        sign = True
        while q:
            size = len(q)
            ans = []
            for _ in range(size):
                idx = q.popleft()
                ans.append(idx.val)
                if idx.left != None:
                    q.append(idx.left)
                if idx.right != None:
                    q.append(idx.right)
            if sign:
                answer.append(ans)
            else:
                ans.reverse()
                answer.append(ans)
            sign = not sign

        return answer
            
                

class Views:
    def left_view(self,node):
        from collections import deque
        q = deque()
        answer = []
        q.append(node)
        while q:
            size = len(q)
            for i in range(size):
                idx = q.popleft()
                if i == 0:
                    answer.append(idx.val)
                if idx.left != None:
                    q.append(idx.left)
                if idx.right != None:
                    q.append(idx.right)
        return answer
    def right_view(self,node):
        from collections import deque
        q = deque()
        answer = []
        q.append(node)

        while q:
            size = len(q)
            for i in range(size):
                idx = q.popleft()
                if i == size - 1:
                    answer.append(idx.val)
                if idx.left != None:
                    q.append(idx.left)
                if idx.right != None:
                    q.append(idx.right)

        return answer
    def find(self,edges,row,col,node):
        if node == None:
            return edges
        edges.append((col,row,node.val))
        if node.left != None:
            self.find(edges,row+1,col-1,node.left)
        if node.right != None:
            self.find(edges,row+1,col+1,node.right)

    def vertical_view(self,node):
        edges = []
        self.find(edges,0,0,node)
        edges.sort()
        ans  = []
        prev_col = None

        for col,row,val in edges:
            if prev_col != col:
                ans.append([])
                prev_col = col
            ans[-1].append(val)
        return ans
    def topview(self,node):
        edges = []
        self.find(edges,0,0,node)
        edges.sort()

        pre_col = None
        ans = []
        for col,row,val in edges:
            if pre_col != col:
                ans.append(val)
                pre_col = col
        return ans

    def bottom_view(self,node):
        edges = []
        self.find(edges,0,0,node)
        edges.sort()
        m = {}
        for col,row,val in edges:
            m[col] = val
        ans = []
        for key in sorted(m):
            ans.append(m[key])
        return ans


