# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Singly Linked List

# %%
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def deleteNode(self, node):
        head = self.head
        if node.next:
            node.value = node.next.value
            node.next = node.next.next
        else:
            while head.next:
                curr = head
                head = head.next
            node = None
            curr.next = node
    
    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            
    def reverse_list(self, head):
        prev = None
        curr = head 
        while curr:
            tmp = curr.next 
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev

    def traversal(self, head):
        while head:
            print(head.value)
            head = head.next

    def removeNthFromEnd(self, head, n: int):
        def helper(head):
            if head is None:
                return 0
            else:
                cnt = helper(head.next) + 1
                if cnt > n:
                    head.next.value = head.value                
                return cnt
        helper(head)
        self.head =  head.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append('None')
        return " -> ".join(map(str, nodes))

if __name__ == "__main__":
    # %%
    llist = LinkedList()
    llist.head = Node(1) 


    # %%
    second = Node(2) 
    third = Node(3)
    fourth = Node(4)
    llist.head.next = second
    second.next = third


    # %%
    print(llist)

    # %% [markdown]
    # ##Remove Nth From the End

    # %%
    llist.removeNthFromEnd(llist.head, n=1)


    # %%
    print(llist)

    # %% [markdown]
    # ## Delete Node

    # %%
    llist.deleteNode(second)
    print(llist)

    # %% [markdown]
    # ## Append Node

    # %%
    llist.append(fourth)
    print(llist)


    # %%
    llist.deleteNode(fourth)
    print(llist)


    # %%
    fifth = Node(5)


    # %%
    llist.append(fifth)


    # %%
    print(llist)

    # %% [markdown]
    # ## Reverse List

    # %%
    llist.reverse_list(llist.head)


    # %%
    print(llist)


    # %%



