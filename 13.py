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


newnode = Node("First node")
nextnode = Node("Second node", newnode)
nextnode = Node("Third node", nextnode)
nextnode = Node("Forth node", nextnode)


array = []
#right most is the top
def read_array_stack(list):
    if len(list) == 0:
        return None
    else:
        return list[-1]
def insert_array_stack(list, item, listsize):
    if len(list) == listsize:
        print("error")
    else:
        list[-1] += item
def remove_array_stack(list, listsize):
    if len(list) == listsize:
        return None
    else:
        return list[-1]
def search_array_stack(list,item):
    for i in list:
        if i == item:
            return True
    return False
def insert_array_stack_resizable(list,item):
    print()
def ooinsert(head, item):
    n = Node(item, head)
    head = n

class Fixedstack:
    def __init__(self):
        self.array = []
        self.top = -1
    def is_full(self):
        return self.top == len(self.array)-1
    def is_empty(self):
        return self.array == []
    def read(self):
        self.top = len(self.array) - 1
        if self.top != -1:
            return self.array[-1]
        else:
            return None
    def insert(self, data):
        self.top = len(self.array) - 1
        if not self.is_full():
            self.top = len(self.array)-1
            self.top = self.top + 1
            self.array[self.top] = data
        else:
            return None
    def remove(self):
        if not self.array.isempty():
            n = self.array[-1]
            self.array = self.array[:-1]
            return n
        else:
            return None
    def serach(self, item):
        for i in self.array:
            if i == item:
                return True
        return False











class Resizablestack:
    def __init__(self):
        self.array = []
        self.top = -1
    def is_empty(self):
        return self.array == []
    def is_full(self):
        return self.top == len(self.array) - 1
    def read(self):
        self.top = len(self.array) - 1
        if self.top != -1:
            return self.array[-1]
        else:
            return None
    def insert(self, data):
        self.top = len(self.array) - 1
        if not self.is_full():
            self.top = len(self.array) - 1
            self.array[self.top] = data
        else:
            return None
    def remove(self):
        if not self.is_empty():
            self.top = len(self.array) - 1
            self.top = self.top - 1
            return self.array[self.top+1]
        return None
    def serach(self, item):
        for i in self.array:
            if i == item:
                return True
        return False




