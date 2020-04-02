class Fixedqueue:
    def __init__(self):
        self.items = []
        self.front = -1
        self.tail = -1

    def is_empty(self):
        return self.items == []
    def read(self):
        self.front = len(self.items) - 1
        if self.front != -1:
            return self.items[self.front]
        return None
    def insert(self, item):
        self.front == len(self.items) - 1
        if (self.tail + 1) == self.front:
            return "error"
        if 


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
