import copy

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.get_level_order())

    def get_level_order(self):
        from collections import deque
        ret = [self.val]
        q = deque()
        q.append(self)
        while q:
            s = len(q)
            for _ in range(s):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    ret.append(curr.left.val)
                # else:
                #    ret.append('null')
                if curr.right:
                    q.append(curr.right)
                    ret.append(curr.right.val)
                # else:
                #    ret.append('null')
        return ret


class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        nums = [x for x in range(1, n + 1)]
        return self.helper(1, n + 1)

    def helper(self, start, end):
        if end - start == 1:
            return [TreeNode(start)]
        ret = []
        for num in range(start, end):
            right_trees = self.helper(num + 1, end)
            left_trees = self.helper(1, num)
            if right_trees and left_trees:
                for r in right_trees:
                    for l in left_trees:
                        root = TreeNode(num)
                        root.left = l
                        root.right = r
                        ret.append(root)
            elif right_trees:
                for r in right_trees:
                    root = TreeNode(num)
                    root.right = r
                    ret.append(root)
            else:
                for l in left_trees:
                    root = TreeNode(num)
                    root.left = l
                    ret.append(root)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))
