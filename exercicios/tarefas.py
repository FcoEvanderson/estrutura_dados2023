from fila_ligada import Queue
from random import randint

fila = Queue()

while True:
    p = randint(0,10)
    if p == 10: break

    task = randint(101,999)
    task = "Task " + str(task)
    fila.enqueueTask(task, p)

fila.toString()