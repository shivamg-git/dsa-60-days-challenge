class Node():
    def __init__(self, val=None, next_node=None ) -> None:
        self.val  = val
        self.next = next_node

class LinkedList():
    
    def __init__(self,start_node=None) -> None:
        self.start_node = start_node

    def add_node(self, curr_node:Node , val) -> Node:
        curr_node.next = Node(val=val)
        return curr_node.next

    def load_list(self, list_) -> None:
        if len(list_) > 0:
            self.start_node = Node(val=list_[0])
            curr = self.start_node
            for l in list_[1:]:
                curr.next = Node(val=l)
                curr=curr.next

    def list_traverse(self):
        curr=self.start_node
        while curr:
            print(curr.val, end=" ")
            curr=curr.next
        print("")

# ll = LinkedList()
# ll.load_list([0,1,2,3,4,5,6,7])
# ll.list_traverse()