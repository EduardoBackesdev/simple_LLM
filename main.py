from src.tokenizer import tokenizer

def main():
    t = tokenizer()
    t.build_vocab("Ola mundo")
    t.encode("Ola mundo")    
    
    
if __name__ == "__main__":
    main()