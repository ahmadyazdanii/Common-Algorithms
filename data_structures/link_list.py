class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def search(self, target):
        if self.value == target:
            return self
        else:
            if self.next:
                return self.next.search(target)
            else:
                return None

    def __repr__(self):
        return f"Node({self.value})"


class LinkList:
    def __init__(self):
        self.root = None
        self.latest = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value)

        if self.latest:
            self.latest.next = new_node
            new_node.previous = self.latest
            self.latest = new_node
        else:
            if self.root == None:
                self.root = new_node
                self.latest = new_node

        self.length += 1

    def search(self, target):
        return self.root.search(target)

    def pop(self):
        latest_node = self.latest
        self.latest = self.latest.previous
        self.latest.next = None

        return latest_node

    def append(self, node: Node, value):
        if self.length == 0:
            raise ValueError("The list does not have the input node")

        new_node = Node(value)

        new_node.previous = node
        new_node.next = node.next
        (node.next).previous = new_node
        node.next = new_node

    def delete(self, node: Node):
        if self.length > 1:
            if node == self.latest:
                self.latest = self.latest.previous
                self.latest.next = None
            elif node == self.root:
                self.root = self.root.next
                self.root.previous = None
            else:
                (node.previous).next = node.next
                (node.next).previous = node.previous
        elif self.length == 1:
            self.root = None
            self.latest = None
        else:
            raise ValueError("List is empty")

        del node

    def __repr__(self):
        items = ""
        next_node = self.root

        while next_node != None:
            if len(items):
                items += ", "

            items += str(next_node.value)

            next_node = next_node.next

        return f"[{items}]"


if __name__ == "__main__":
    list = LinkList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    list.insert(4)
    list.insert(5)

    item = list.search(4)
    print(item)
    print(list.search(10))

    print(list)

    list.delete(item)
    print(list.pop())

    item = list.search(2)
    list.append(item, 12)

    print(list)
