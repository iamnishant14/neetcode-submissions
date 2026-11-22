class Node:
    def __init__(self,value,nextNode=None):
        self.val = value
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self._head = Node(-1)
        self._tail = self._head
    
    def get(self, index: int) -> int:
        trav = self._head.next
        i = 0
        while trav:
            if i==index:
                return trav.val
            trav=trav.next
            i+=1
        return -1


    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self._head.next
        self._head.next = new_node
        if not new_node.next:
            self._tail = new_node 


    def insertTail(self, val: int) -> None:
        self._tail.next = Node(val)
        self._tail = self._tail.next
        

    def remove(self, index: int) -> bool:
        i=0
        trav = self._head
        while trav and i<index:
            trav=trav.next
            i+=1
        
        if trav and trav.next:
            if trav.next == self._tail:
                self._tail = trav
            trav.next=trav.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        trav = self._head.next
        out = list()
        while trav :
            out.append(trav.val)
            trav=trav.next
        return out
        
