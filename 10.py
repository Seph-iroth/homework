class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

list=[1, 2, 3, 4, 5, 6, 5] #the end is the top



def push(element, list):
    list.append(element)
    return list
def pop(list):
    list.pop(-1)
    return list
def peek(list):
    return list[-1]
def empty(list):
    if len(list) == 0:
        return True
    return False
def clear(list):
    list = []
    return list
def stackpush(element, head):
    element = Node(element)
    element.next = head
def stackpop(head):
    head.next = head.next.next
def stackpeek(head):
    n = head
    return n.data
def stackempty(head):
    if head == None:
        return True
    else:
        return False
def stackclear(head):
    while head.next != None:
        head = None
        head = head.next




# 5 stack array
def stack_push_array(array ,element):
    array[len(array)] = element
    return array
def stack_pop_array(array):
    data  = array[-1]
    del array[-1]
    return data
def stack_peek_array(array):
    return array[-1]
def stack_is_empty_array(array):
    if len(array) == 0:
        return True
    else:
        return False
def stack_clear_linked(element, head):
    element = Node(element)

# 6 stack linked list
def stackpush(element, head):
    element = Node(element)
    element.next = head
def stackpop(head):
    data = head.get_data()
    head = head.next
    return data

def stackpeek(head):
    return head.get_data()
def stackempty(head):
    if head == None:
        return True
    else:
        return False
def stackclear(head):
    head == null

#7 queue
def arraypushQ(list, element): #from the right most "end"
    list.append(element)
    return list
def arraypopQ(list):
    n = list[0]
    list.pop(0)
    return n
def arraypeekQ(list):
    return list[0]
def arrayemptyQ(list):
    if len(list) == 0:
        return True
    else:
        return False
def arrayclearQ(list):
    while len(list) != 0:
        list.pop(0)
    return list

def LLpushQ(head, element):
    element = Node(element)
    while head.next != Node:
        head = head.next
    head.next = element
    return head
def LLpopQ(head):
    data = head.data
    head = head.next
    return data
def LLpeekQ(head):
    return head.data
def LLemptyQ(head):
    if head == None:
        return True
    else:
        return False
def LLclearQ(head):
    head = None
    return head