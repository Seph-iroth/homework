class FixedStack:
    def __init__(self):
        self.items = []
        self.top = -1
    def is_full(self):
        return self.items.top == len(self.items)-1
    def is_empty(self):
        return self.items == []
    def read(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def insert(self, data):
        self.items.top = len(self.items) - 1
        if not self.items.is_full():
            self.items.top = self.items.top + 1
            self.items[self.items.top] = data
        else:
            return None
    def remove(self):
        self.items.top = len(self.items) - 1
        if not self.is_empty():
            self.items.top = self.items.top -1
            n = self.items.top
            self.items = self.items[:n]
            return self.items[n]
        else:
            return None
    def serach(self,item):
        for i in self.items:
            if i == item:
                return True
        else:
            return False

class ResizeableStack:
    def __init__(self):
        self.items = []
        self.top = -1

    def is_full(self):
        return self.items.top == len(self.items) - 1

    def is_empty(self):
        return self.items == []

    def read(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def insert(self, data):
        self.items.top = len(self.items) - 1
        if self.items.is_full():
            newlist = [len(self.items)*2]
            for i in range(0 , len(self.items)-1 ):
                newlist[i] = self.items[i]
            self.items = newlist
        self.items.top = self.items.top + 1
        self.items[self.items.top] = data

    def remove(self):
        self.items.top = len(self.items) - 1
        if not self.is_empty():
            self.items.top = self.items.top - 1
            n = self.items.top
            self.items = self.items[:n]
            return self.items[n]
        else:
            return None

    def serach(self, item):
        for i in self.items:
            if i == item:
                return True
        else:
            return False


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
#fixed size
class OOFixedStack(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = None
    def read(self):
        return self.data
    def insert(self,item):
        n  = Node(item, self)
        self.data = n

    def remove(self):
        n = self.data
        if self != None:
            self.next.next = self.next
        return n

    def search(self,item):
        n = self
        while n != None:
            if self.data == item:
                return True
            n = n.next
        return False
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

#same
class OOResizedStack(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = None
    def read(self):
        return self.data
    def insert(self,item):
        n  = Node(item, self)
        self.data = n

    def remove(self):
        n = self.data
        if self != None:
            self.next.next = self.next
        return n

    def search(self,item):
        n = self
        while n != None:
            if self.data == item:
                return True
            n = n.next
        return False
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next