from Student import Students
class queue:
    def __init__(self,size):
        self.size = size
        self.items = []
    
    def enqueue(self, data: Students) -> bool:
        if len(self.items) < self.size:
            self.items.append(data)
            return True
        return False
    
    def dequeue(self) -> Students|bool:
        if self.items:
            data = self.items.pop(0)
            return data
        return False

    def front(self) -> Students|bool:
        if self.items:
            return self.items[0]
        return False
    
    def is_empty(self) -> bool:
        if self.items:
            return False
        return True
    
    def is_full(self) -> bool:
        if len(self.items) == self.size:
            return True
        return False
    
    def get_size(self) -> int|bool:
        return len(self.items)

if __name__ == "__main__": 
    s1 = Students(1, "ahmed", [3.5, 4.0, 2.5, 5.0, 4.5])
    s2 = Students(2, "basil", [4.0, 3.5, 4.5, 3.0, 4.0]) 
    s3 = Students(3, "joe", [2.5, 3.0, 3.5, 4.0, 3.5])
    q = queue(2)
    print(f"is empty: {q.is_empty()}")
    print(f"is full: {q.is_full()}")
    print(f"dequeue: {q.dequeue()}")
    print(q.get_size())
    print(f"front: {q.front()}")
    print(f"enqueue s1: {q.enqueue(s1)}")
    print(f"enqueue s2: {q.enqueue(s2)}")
    print(f"enqueue s3: {q.enqueue(s3)}")
    print(f"is empty: {q.is_empty()}")
    print(f"is full: {q.is_full()}")
    print(f"dequeue: {q.dequeue()}")
    print(f"get size: {q.get_size()}")
    print(f"front: {q.front()}")
    print(f"dequeue: {q.dequeue()}")
    print(f"dequeue: {q.dequeue()}")
    print(f"dequeue: {q.dequeue()}")