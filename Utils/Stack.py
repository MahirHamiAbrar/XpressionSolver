from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.next = None
        self.value = value


class Stack:
    def __init__(self) -> None:
        self.head = Node("head")
        self._len = 0
    
    def __repr__(self) -> str:
        text = "["
        
        if self.head.next:
            node = self.head.next
            l = self._len
            
            while l > 1:
                text += f"{str(node.value)}, "
                node = node.next
                l -= 1
            text += f"{str(node.value)}"
        
        text += "]"
        return text
    
    def prettyText(self) -> str:
        text = "[EMPTY]"
        
        if self.head.next:
            text = "[BOTTOM] ["
            node = self.head.next
            l = self._len
            
            while l > 1:
                text += f"{str(node.value)} <- "
                node = node.next
                l -= 1
            text += f"{str(node.value)}] [TOP]"
        
        return text
    
    def print(self) -> None:
        print(self.prettyText())
    
    def size(self) -> int:
        return self._len
    
    def isEmpty(self) -> bool:
        return (self._len == 0)
    
    def isNotEmpty(self) -> bool:
        return (self._len > 0)
    
    def push(self, value: Any) -> None:
        # create a new node
        node = Node(value)
        # point new node's next-pointer to where the head was pointing until now
        node.next = self.head.next
        # change the pointer of the 'head' to current node
        self.head.next = node
        # increment length
        self._len += 1
    
    def pushValues(self, values: list | tuple) -> None:
        for v in values:
            self.push(v)
    
    def top(self) -> Any:
        return None if self.head.next is None else self.head.next.value
    
    def pop(self) -> Any:
        assert self._len != 0 or self.head.next is None, "Cannot pop() from an empty Stack!"
        # decrement the length
        self._len -= 1
        # get the current Node's value
        value = self.head.next.value
        # change the pointer to the next next Node
        self.head.next = self.head.next.next
        # return the value
        return value
    
    def clear(self) -> None:
        self.head.next = None
        self._len = 0


if __name__ == '__main__':
    stack = Stack()
    print(stack)
    stack.push(1)
    stack.push(2)
    stack.push("text item")
    stack.push(12.38)
    stack.print()   # print with top & bottom indicator
    print(stack)    # print only the values
    
    for i in range(0, 4):
        stack.pop()
        print(f"i = {i}; Stack = {stack}")


