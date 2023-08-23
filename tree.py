class BinaryNode():
    def __init__(self, value=None, right=None, left=None) -> None:
        self.val    = value
        self.right  = right
        self.left   = left
    
    def printNode(self):
        print(f"Node Value = {self.val}")
        print(f"Node Right = {self.right}")
        print(f"Node Left  = {self.left}")        

class BinaryTree():

    def __init__(self, root_node:BinaryNode = None ) -> None:
        self.root_node = root_node

    def _create_binary_tree_from_list(self, list_:list) -> BinaryNode:
        if len(list_) == 0:
            return None
        
        mid = len(list_)//2
        left_node = self._create_binary_tree_from_list(list_[:mid])
        right_node = self._create_binary_tree_from_list(list_[mid+1:])
        root_node = BinaryNode(value=list_[mid], left=left_node, right=right_node)
        return root_node

    def load_binary_tree_from_list(self, list_:list) -> None:
        self.root_node = self._create_binary_tree_from_list(list_)


    def _print_pre_order_traversal(self, root_node):
        if root_node is None:
            return
        print(root_node.val, end=" ")
        self._print_pre_order_traversal(root_node.left)
        self._print_pre_order_traversal(root_node.right)

    def pre_order_traversal(self):
        self._print_pre_order_traversal(self.root_node)
        print("")


    def _print_post_order_traversal(self, root_node):
        if root_node is None:
            return
        self._print_post_order_traversal(root_node.left)
        self._print_post_order_traversal(root_node.right)
        print(root_node.val, end=" ")

    def post_order_traversal(self):
        self._print_post_order_traversal(self.root_node)
        print("")


    def _print_inorder_order_traversal(self, root_node):
        if root_node is None:
            return
        self._print_inorder_order_traversal(root_node.left)
        print(root_node.val, end=" ")
        self._print_inorder_order_traversal(root_node.right)

    def inorder_order_traversal(self):
        self._print_inorder_order_traversal(self.root_node)
        print("")

# node = BinaryNode(value=20,right=BinaryNode(value=10),left=BinaryNode(value=30))
# node.printNode()

# binary_tree = BinaryTree()
# binary_tree.load_binary_tree_from_list(list(range(1,20)))
# binary_tree.pre_order_traversal()
# binary_tree.post_order_traversal()
# binary_tree.inorder_order_traversal()