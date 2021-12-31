# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(root: TreeNode, target: int, path:List[str]) -> bool:
            if root.val == target:
                return True
            elif root.left and find(root.left, target, path):
                path+="L"
            elif root.right and find(root.right, target, path):
                path+="R"
            return path
        
        start = []
        dest = []
        
        find(root, startValue, start)
        find(root, destValue, dest)
        i = 0
        size = min(len(start), len(dest))
        
        
        
        while len(start) and len(dest) and start[-1] == dest[-1]:
            start.pop()
            dest.pop()
        
        start = "U" * (len(start) - i ) + "".join(reversed(dest))
        # print(start)
        return start
        