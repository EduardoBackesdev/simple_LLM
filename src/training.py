from src.tokenizer import tokenizer

class training:
    
    def training(self, p: str):
        tokenizer().build_vocab(p)   