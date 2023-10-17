class Queue:
    def __init__(self):
        self._qList = []

    def showList(self):
        for i in self._qList:
            print(i, end=" ")

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._qList)

    def enqueue(self, item):
        self._qList.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self._qList.pop(0)
