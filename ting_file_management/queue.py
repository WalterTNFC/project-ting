from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        # Inicializando a lista
        self.queue = list()

    def __len__(self):
        # Uso do len para determinação do tamanho da lista
        return len(self.queue)

    def enqueue(self, value):
        # Append para adicionar value ao final
        self.queue.append(value)

    def dequeue(self):
        # pop para remover o ultimo item mas nao exluir
        return self.queue.pop(0)

    def search(self, index):
        queue = self.queue
        if index >= 0 and index <= (len(queue) - 1):
            return queue[index]
        raise IndexError
