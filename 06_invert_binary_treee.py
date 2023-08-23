"""
Invert a binary tree given root node return root node

"""
from tree import BinaryTree

def invert_binary_tree(root_node:BinaryTree) -> BinaryTree:
    if root_node is None:
        return
    invert_binary_tree(root_node.left)
    invert_binary_tree(root_node.right)
    root_node.left,root_node.right = root_node.right, root_node.left
    return root_node


binary_tree = BinaryTree()
binary_tree.load_binary_tree_from_list(list(range(1,8)))
binary_tree.inorder_order_traversal()
binary_tree.root_node = invert_binary_tree(binary_tree.root_node)
binary_tree.inorder_order_traversal()
