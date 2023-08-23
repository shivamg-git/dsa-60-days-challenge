from tree import BinaryTree, BinaryNode

def find_LCA(val_1, val_2, root_node)-> BinaryNode:

    # Assuming both node must be avaialable
    if root_node.val > max(val_1,val_2):
        find_LCA(val_1,val_2, root_node.left)
    elif root_node.val < min(val_1,val_2):
        find_LCA(val_1,val_2, root_node.right)
    else:
        print(root_node)
        print(root_node.val)
        return root_node

binary_tree = BinaryTree()
binary_tree.load_binary_tree_from_list(list(range(1,20)))
binary_tree.pre_order_traversal()

#TODO something is wrong returning None
print(find_LCA(6,9,binary_tree.root_node))
