class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.nodes = [node]
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                self.nodes.append(Node(elem))
                node = node.next

    def __repr__(self):
        node = self.head
        self.nodes = []
        while node is not None:
            self.nodes.append(node.data)
            node = node.next
        self.nodes.append("None")
        return " -> ".join(self.nodes)
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        
    def reverse(self):
        for pos, node in enumerate(self.nodes[::-1]):
            if node == self.head:
                break
            node.next = self.nodes[::-1][pos+1]
        self.head.next = None
        self.nodes = self.nodes[::-1]
        self.head = self.nodes[0]

def main():
    p = LinkedList(["a", "b", "c"]) 
    p.add_last(Node("p"))
    print(p)
    p.reverse()
    print(p)
if __name__ == "__main__":
    main()
