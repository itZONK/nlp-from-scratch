from src.textlab.day02.text_cleanV1 import top_k_words
import os

def read_text(path:str):
    with open(path,"r",encoding="utf-8") as file:
        text = file.read()
    return text

def main():
    print("工作目录：", os.getcwd())

    path1 = "data/day03/sample.txt"
    text = read_text(path1)

    print(top_k_words(5,text))




if __name__ == "__main__":
    main()