# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

#                        Node
#       left              |               right
#         ----------------+------------------
#         |                                 |
#    x----+-----                       -----+-----
#              |                       |         |
#          x---+---x                ---+---x x---+---x
#                                   |
#                               x---+---x

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def min_tree_depth(node):
    if node is None:
        return 0
    return 1 + min(min_tree_depth(node.left), min_tree_depth(node.right))
