import datetime
import queue
import random


class CodaPrioritaria:
    def __init__(self):
        self._lista = [] #voglio che nessuno tocchi questo parametro
        #la lista sarà una lista di tuple di cui il primo valore è la priorità e il secondo è l'oggetto

    def put(self, x):
        """
        Aggiungo un nuovo elemento alla coda
        :param x:
        :return:
        """
        self._lista.append(x)

    def get(self):
        """
        Restituisce l'elemento più piccolo presente nella coda e lo elimina
        :return:
        """
        index, val = min(enumerate(self._lista), key=lambda x: x[1])
        self._lista.pop(index)
        return val[1] #non ci portiamo più dietro la priorità

    def __len__(self):
        return len(self._lista)

#c = CodaPrioritaria()

c = queue.PriorityQueue() #uso la classe implementata da Python e uso i suoi metodi

c.put((3, "ciao"))
c.put((1, "hello"))
c.put((2, "test"))

print(c.get()[1]) #stampa in ordine di priorità
print(c.get()[1])
print(c.get()[1])

#controllo quanto tempo impiega il mio metodo #questo ci mette taaaaaaanto di più
c1 = CodaPrioritaria()
tic = datetime.datetime.now()
for i in range(10000):
    c1.put((random.randint(0, 100), random.randint(0, 100)))
for i in range(len(c1)):
    c1.get()
toc = datetime.datetime.now()
print(f"La tua implementazione di coda prioritaria ci ha messo {toc-tic} secondi")

#controllo quanto tempo impiega il metodo di default
c2 = queue.PriorityQueue()
tic = datetime.datetime.now()
for i in range(10000):
    c2.put((random.randint(0, 100), random.randint(0, 100)))
for i in range(c.qsize()):
    c2.get()
toc = datetime.datetime.now()
print(f"L'implementazione di default della coda prioritaria ci ha messo {toc - tic} secondi")
