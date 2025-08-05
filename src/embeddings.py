import random

class embeddings:
    def __init__(self, vocab_size, embedding_dim):
        self.matriz = [
            [random.random() for _ in range(embedding_dim)]
            for _ in range(vocab_size)
        ]
    
    def get_embeddings(self, a: list[int]):
        c = []
        for i in a:
            c.append(self.matriz[i])
        return c    
                   
    def update_embeddings(self, a):
        pass