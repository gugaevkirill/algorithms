# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        root - 1 - 8 - . - . - . - p
        root - 1 - 8 - . - q

        >>> root = TreeNode(1)
        >>> Solution().lowestCommonAncestor(root, root, root) is root
        True
        
        >>> a = TreeNode(1)
        >>> b = TreeNode(2)
        >>> root = TreeNode(0)
        >>> root.left = a
        >>> root.right = b
        >>> Solution().lowestCommonAncestor(root, a, b) is root
        True
        """
        
        # DFS: find ways to p & q
        way_p = self.find_way(root, p)
        way_q = self.find_way(root, q)
        
        # find the deepest common node
        i = 0
        while i < len(way_p) and i < len(way_q) and way_p[i] is way_q[i]:
            i += 1
        
        return way_p[i - 1]
    
    def find_way(self, root, node):
        """
        :rtype: List[TreeNode]
        """
        if root == node:
            return [root]
        
        for child in (root.left, root.right):
            if child is None:
                continue
            
            way = self.find_way(child, node)
            if way is not None:
                return [root] + way
        
        return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
