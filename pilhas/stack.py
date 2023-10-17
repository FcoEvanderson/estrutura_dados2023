from node import Node

# Recursos mínimos que uma pilha deve ter:
# Inserir dado, remover dado e observar o topo da pilha


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def isEmpty(self): return self._size == None

    def push(self, element):
        # insere elementos
        node = Node(element)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        # remove elementos
        if not self.isEmpty():
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node
        raise IndexError("The Stack is empty!")

    def peek(self):
        # retorna o topo sem remover
        if not self.isEmpty():
            node = self.top.data
            return node
        raise IndexError("The Stack is empty!")

    def __len__(self): return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self): return self.__repr__()
