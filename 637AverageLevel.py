class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque([root])
       
        result = []
        while queue:
            size = len(queue)
            levelSum = 0
            for i in range(size):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(levelSum/size)
        return result
