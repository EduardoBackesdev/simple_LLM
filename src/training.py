from src.tokenizer import tokenizer

class training:
    
    def __init__(self, a: tokenizer):
        self.x = a
        
    
    def training(self, p: str):
        self.x.build_vocab(p)   