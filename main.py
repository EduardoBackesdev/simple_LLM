from src.tokenizer import tokenizer
from src.training import training

def main():
    a = tokenizer()
    t = training(a).training("Ola mundo")
    a.decode([1, 1])
  
    
    
if __name__ == "__main__":
    main()