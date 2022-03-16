class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self,head=None):
        self.head = head
        
    def insert(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print("none")    

ll = Linked_List()
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.print_list()