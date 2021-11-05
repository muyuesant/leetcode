https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        queue = []
        root.val = 1
        queue.append(root)
        while queue:
            size = len(queue)
            maxWidth = max( maxWidth, (queue[size-1].val - queue[0].val + 1) )
            # print("size",size,"queue[0]",queue[0].val,"queue[size-1]",queue[size-1].val,"maxWidth",maxWidth)
            for i in range(size):
                curr = queue.pop(0)
                if curr.left is not None:
                    curr.left.val = curr.val*2
                    queue.append(curr.left)
           
                if curr.right is not None:
                    curr.right.val = curr.val*2+1
                    queue.append(curr.right)
        return maxWidth