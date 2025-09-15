class Lists:
    def __init__(self):
        self.container = []

    def append(self, item):
        self.container += [item]

    def remove(self, item):
        new_container = []
        found = False
        for x in self.container:
            if x == item and not found:
                found = True
                continue
            new_container += [x]
        if not found:
            print("item not found")
        self.container = new_container

    def pop(self):
        if len(self.container) == 0:
            print("empty list")
            return None
        last_item = self.container[-1]
        self.container = self.container[:-1]
        return last_item

    def insert(self, index, item):
        before = self.container[:index]
        after = self.container[index:]
        self.container = before + [item] + after
