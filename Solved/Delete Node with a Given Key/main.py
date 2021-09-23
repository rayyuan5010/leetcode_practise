class Node:
    next = None
    data = None

    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data


def delete_node(head, key):
    #TODO: Write - Your - Code
    if head.data == key:
        head = head.next
        rec(None,head.next, key)
    else:
        rec(None,head, key)
    return head


def rec(pre,current, key):
    if current == None:
        return pre
    
    if current.data == key:
        pre.next = current.next
    return rec(current,current.next,key)
            


def print_node(current):
    if current == None:
        return
    print(current.data)
    print_node(current.next)


head2 = delete_node(Node(data=4, next=Node(data=6, next=Node(
    data=54, next=Node(data=20, next=Node(data=1))))), 4)
print_node(head2)