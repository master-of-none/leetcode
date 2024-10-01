from typing import List
import collections

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def dfs_iterative(self, root) -> List[str]:
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            
            if cur.right:
                stack.append(cur.right)
            
            if cur.left:
                stack.append(cur.left)
            
        
        return res

    def dfs_recursive(self, root) -> List[str]:
        res = []
        if not root:
            return []
        res = [root.val]
        res += self.dfs_recursive(root.left)
        res += self.dfs_recursive(root.right)

        return res

    def bfs(self, root) -> List[str]:
        if not root:
            return []
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res

if __name__ == "__main__":
    a = Tree('a')
    b = Tree('b')
    c = Tree('c')
    d = Tree('d')
    e = Tree('e')
    f = Tree('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    res = a.dfs_iterative(a)
    print(res)

    res = a.dfs_recursive(a)
    print(res)

    res = a.bfs(a)
    print(res)
