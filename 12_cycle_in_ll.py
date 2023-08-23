from linked_list import LinkedList

def is_ll_circular(ll:LinkedList) -> bool:
    slow = ll.start_node
    fast = ll.start_node.next

    while slow and fast:
        if slow == fast:
            return True

        slow=slow.next
        if fast.next:
            fast=fast.next.next
        else:
            return False
        
def make_ll_circular(ll:LinkedList) -> None:
    curr=ll.start_node
    for i in range(0,9):
        curr=curr.next
    last=curr
    while last.next:
        last=last.next
    last.next=curr

ll = LinkedList()
ll.load_list(list(range(0,20)))
ll.list_traverse()
print(is_ll_circular(ll))
make_ll_circular(ll)
print(is_ll_circular(ll))

# curr=ll.start_node
# for i in range(0,50):
#     print(curr.val, end=" ")
#     curr=curr.next