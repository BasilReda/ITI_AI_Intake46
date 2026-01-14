from Student import Students

class Node:
    def __init__(self, data):
        self.id = data.Get_id
        self.name = data.Get_name
        self.grades = data.Get_grades
        self.next = None
        self.prev = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data: Students):
        nd = Node(data)
        if self.head==None:
            self.head = nd
            self.tail = nd
        else:
            self.tail.next = nd
            nd.prev = self.tail
            self.tail = nd
    
    def prepend(self,data: Students):
        nd = Node(data)
        if self.head==None:
            self.head = nd
            self.tail = nd
        else:
            nd.next = self.head
            self.head.prev = nd
            self.head = nd
    
    def delete_by_id(self, id):
        curr = self.head
        while curr is not None:
            if curr.id == id:
                if curr == self.head:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None
                elif curr == self.tail:
                    self.tail = curr.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                return True
            curr = curr.next
        return False

    def search_by_name(self, name):
        curr = self.head
        if curr is not None:
            while curr is not None:
                if curr.name == name:
                    return curr
                curr = curr.next
        return False
    
    def search_by_id(self, id):
        curr = self.head
        if curr is not None:
            while curr is not None:
                if curr.id == id:
                    return curr
                curr = curr.next
        return False

    def count_nodes(self):
        curr = self.head
        count = 0
        if curr is not None:
            while curr is not None:
                count += 1
                curr = curr.next
        return count

    def display_forward(self):
        curr = self.head
        display = []
        if curr is not None:
            while curr is not None:
                display.append((curr.id, curr.name, curr.grades))
                curr = curr.next
        return display
    
    def display_backward(self):
        curr = self.tail
        display = []
        if curr is not None:
            while curr is not None:
                display.append((curr.id, curr.name, curr.grades))
                curr = curr.prev
        return display

if __name__ == "__main__":
    ll = Linked_list()
    s1 = Students(1 , "Alice", [3.5, 4.0, 2.5, 5.0, 4.5])
    s2 = Students(2 , "Bob", [4.0, 3.5, 4.5, 3.0, 4.0])
    s3 = Students(3 , "Charlie", [2.5, 3.0, 3.5, 4.0, 3.5])
    print(ll.delete_by_id(1))
    print(ll.search_by_id(1))
    print(ll.search_by_name("Bob"))
    print(ll.append(s1))
    print(ll.append(s2))
    print(ll.prepend(s3))
    print(ll.count_nodes())
    print(ll.display_forward())
    print(ll.display_backward())
    print(ll.delete_by_id(1))
    print(ll.search_by_id(2))
    print(ll.search_by_name("Bob"))
    print(ll.display_forward())
    print(ll.display_backward())