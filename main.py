from src.tokenizer import tokenizer
from src.training import training

def main():
    a = training().training("Ola mundo como voces estão?")
    t = tokenizer()
    tokens = t.encode("Ola mundo") 
    t.decode(tokens);   
    
    
if __name__ == "__main__":
    main()