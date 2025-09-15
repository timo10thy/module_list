class List:
    def __init__(self):
        self.container = []

    def append(self, item):
        self.container += [item]

    def remove(self, item):
        if item in self.container:
            new_container = []
            for x in self.container:
                if x != item:
                    new_container += [x]
            self.container = new_container
        else:
            print("item not found")

    def pop(self):
        if len(self.container) == 0:
            print("empty list")
            return None
        last_item = self.container[len(self.container)-1]
        self.container = self.container[:-1]
        return last_item

    def insert(self, index, item):
        new_container = []
        for i in range(len(self.container)):
            if i == index:
                new_container += [item]
            new_container += [self.container[i]]
        if index >= len(self.container):
            new_container += [item]
        self.container = new_container
