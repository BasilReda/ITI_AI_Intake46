from LL import Linked_list , Node
from Student import Students
class stack:
    def __init__(self, linked_list:Linked_list, size):
        self.ll=linked_list
        self.size = size

    def push(self,data:Students):
        self.ll.prepend(data)
        return True
    
    def pop(self):
        if self.ll.head is None:
            return False
        else:
            if self.ll.tail == self.ll.head:
                data = self.ll.tail
                self.ll.head = self.ll.tail = None
                return data
            else:
                data = self.ll.tail
                self.ll.tail.prev.next = None
                self.ll.tail = self.ll.tail.prev
                return data
        
    def peek(self):
        if self.ll.tail is None:
            return False
        return self.ll.tail
    
    def is_empty(self):
        if self.ll.head:
            return False
        return True
    
    def is_full(self):
        counter = self.ll.count_nodes()
        if counter == self.size-1:
            return True
        return False
    
    def size(self):
        counter = self.ll.count_nodes()
        return counter+1

if __name__ == "__main__":
    ll = Linked_list()
    s1 = Students(1 , "Alice" , [3.5, 4.0, 2.5, 5.0, 4.5])
    s2 = Students(2 , "Bob" , [4.0, 3.5, 4.5, 3.0, 4.0])
    s3 = Students(3 , "Charlie" , [2.5, 3.0, 3.5, 4.0, 3.5])
    print(f"appending:{ll.append(s1)}")
    print(f"appending:{ll.append(s2)}")
    print(f"prepending:{ll.prepend(s3)}")
    s = stack(ll, 10)
    print(f"push: {s.push(Students(4, "David", [3.0, 3.5, 4.0, 4.5, 5.0]))}")
    print(f"pop: {s.pop()}")
    print(f"is full: {s.is_full()}")
    print(f"is empty: {s.is_empty()}")
    print(f"peek:{s.peek()}")
    a = s.pop()
    print(a.name,a.id, a.grades)
    print(s.pop())
    print(s.pop())
    print(f"is empty: {s.is_empty()}")
    print(f"pop: {s.pop()}")