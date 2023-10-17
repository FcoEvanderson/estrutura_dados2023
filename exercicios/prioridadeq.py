class PriorityQueue:
    def __init__(self):
        self._qlist = []


class _PriorityEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
