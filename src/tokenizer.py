class tokenizer:
    
    def __init__(self):
        self.vocab = {}
        self.vocab_invert = {}
        self.index = 0
        
    def encode(self, p: str):
        a = p.lower().split()
        c = []
        for i in a:
            if i in self.vocab:
                c.append(self.vocab[i])
            else:
                c.append("<unk>")    
        return c 
    
    def decode(self, a: list[int]):
        c = []
        for i in a:
            if i in self.vocab_invert:
                c.append(self.vocab_invert[i])        
                
    def build_vocab(self, a: str):
        self.tokenization_vocab(a)
        
    def tokenization_vocab(self, p: str):
        a = p.lower().split()
        for i in a:
            if i not in self.vocab:
                self.vocab[i] = self.index
                self.vocab_invert[self.index] = i
                self.index += 1
                
                