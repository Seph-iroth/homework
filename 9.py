class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

def showlinkedlist(head):
    while (head != None):
        print(head.data)
        head = head.next_node

def deleteNode(head, position):
    if position == 0:
        return  head.next_node
    count = 0
    while count < (position-1):
        count += 1
        head = head.next_node
    head.next_node = head.next_node.next_node
    return head

def insertNode(head, element):
    newnode = Node(element)
    node = head
    while node.next_node != Node:
        node = node.next_node
    node.next_node = newnode
    return head

def main():
    newnode = Node("First node")
    nextnode = Node("Second node", newnode)
    nextnode = Node("Third node", nextnode)
    nextnode = Node("Forth node", nextnode)
    n = nextnode
    while n != None:
        print(n.get_data(), end = "")
        if n.get_next() != None:
            print(end="->")
        n = n.get_next()
    print("\n")
    showlinkedlist(nextnode)
    print("\n")
    showlinkedlist(deleteNode(nextnode, 1))
    print('\n')
    showlinkedlist(insertNode(nextnode, "brand new node"))

main()
