from stack import Stack

if __name__ == "__main__":
        pilha = Stack()
        len(pilha)
        pilha.push(5)
        pilha.push(8)
        pilha.push(2.9)
        pilha.push("Mah oi")
        print(pilha.__repr__())
        len(pilha)
        pilha.peek()
        pilha.pop()
        pilha.pop()
        pilha.peek()
