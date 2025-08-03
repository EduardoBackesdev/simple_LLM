from src.tokenizer import tokenizer
from src.training import training

def main():
    a = training().training("Ola mundo como voces estão?")
    t = tokenizer()
    t.encode("Ola mundo")    
    
    
if __name__ == "__main__":
    main()