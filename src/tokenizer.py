class tokenizer:
    
    def __init__(self):
        self.vocab = {}
        self.index = 0
        
    def encode(self, p: str):
        a = p.split()
        c = []
        for i in a:
            if i in self.vocab:
                c.append(self.vocab[i])
            else:
                c.append("<unk>")    
        return c 
    
    def decode():
        pass       
                
    def build_vocab(self, a: str):
        self.tokenization_vocab(a)
        
    def tokenization_vocab(self, p: str):
        a = p.split()
        for i in a:
            if i not in self.vocab:
                self.vocab[i] = self.index
                self.index += 1