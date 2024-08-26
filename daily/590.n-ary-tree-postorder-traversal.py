# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def traversal(root):
            if root == None:
                return
            
            
            for child in root.children:
                traversal(child)

            res.append(root.val)
        traversal(root)
        return res
# @leet end
