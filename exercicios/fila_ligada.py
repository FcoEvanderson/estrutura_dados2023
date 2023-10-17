class _QueueNode():
    def __init__(self, item):
        self.item = item
        self.next = None


class _QueuePriorityNode():
    def __init__(self, item, pitem):
        self.item = item
        self.priority = pitem
        self.next = None


class Queue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    def isEmpty(self):
        return self._qhead is None

    def __len__(self):
        return self._count

    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._count += 1

    def dequeue(self):
        if not self.isEmpty():
            node = self._qhead
            if self._qhead is self._qtail:
                self._qtail = None
            self._qhead = self._qhead.next
            self._count -= 1
            return node.item

    def clear(self):
        temp = self._qhead
        while temp is not None:
            self._qhead = temp.next
            temp = temp.next
        self._qtail = None
        self._count = 0

    def toString(self):
        temp = self._qhead
        while temp is not None:
            print(f"{temp.item} ({temp.priority})", end="; ")
            temp = temp.next

    def enqueueTask(self, tarefa, prioridade):
        node = _QueuePriorityNode(tarefa, prioridade)
        if not self.isEmpty():
            if node.priority < self._qhead.priority:
                node.next = self._qhead
                self._qhead = node
            elif node.priority >= self._qtail.priority:
                self._qtail.next = node
                self._qtail = node
            else:
                temp = self._qhead
                prev = None
                while node.priority >= temp.priority:
                    prev = temp
                    temp = temp.next
                node.next = prev.next
                prev.next = node
        else:
            self._qhead = node
            self._qtail = node

        self._count += 1
