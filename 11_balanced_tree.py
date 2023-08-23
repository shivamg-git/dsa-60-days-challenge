from tree import BinaryTree

def calc_height(root):
    if root is None:
        return 0
    return 1 + max(calc_height(root.left),calc_height(root.right))

def check_balanced(root):
    if root is None:
        return False
    left    = calc_height(root.left)
    right   = calc_height(root.right)
    if left ==right:
        return True
    else:
        return False
    
binary_tree = BinaryTree()
binary_tree.load_binary_tree_from_list(list(range(1,20)))
print(check_balanced(binary_tree.root_node))
binary_tree.load_binary_tree_from_list(list(range(1,5)))
print(check_balanced(binary_tree.root_node))
binary_tree.load_binary_tree_from_list(list(range(1,4)))
print(check_balanced(binary_tree.root_node))
binary_tree.load_binary_tree_from_list(list(range(1,3)))
print(check_balanced(binary_tree.root_node))
binary_tree.load_binary_tree_from_list(list(range(1,33)))
print(check_balanced(binary_tree.root_node))
binary_tree.load_binary_tree_from_list(list(range(1,32)))
print(check_balanced(binary_tree.root_node))