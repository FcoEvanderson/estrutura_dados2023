from exercicios.fila_sequencial import Queue

values = Queue()
for i in range(16):
    if i % 3 == 0:
        values.enqueue(i)

print(values.showList())


