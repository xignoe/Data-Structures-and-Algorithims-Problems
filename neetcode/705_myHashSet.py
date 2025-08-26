class ListNode:
    def __init__(self, key, next):
        self.key = key
        self.next = next


class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0, None) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        current = self.set[index]

        while current.next:
            if current.next.key == key:
                return
            current = current.next
        current.next = ListNode(key, None)

    def remove(self, key: int) -> None: 
        current = self.set[key % len(self.set)]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        current = self.set[key % len(self.set)]
        while current.next:
            if current.next.key == key:
                return True
            current = current.next
        return False    
    
    