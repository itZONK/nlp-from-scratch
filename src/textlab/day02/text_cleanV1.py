

from src.textlab.day01.word_count import word_count,top_k



def clean_text(text:str):
    text = text.lower()
    text = text.replace("?","").replace("!","").replace(",","").replace(".","")
    text_list = text.split()

    return text_list

def top_k_words(k:int,text:str):
    counts = word_count(clean_text(text))
    return top_k(counts,k)



def main():
    print("测试1：正常文本")
    print(top_k_words(2, "Python, python! PYTHON. Java?"))

    print("测试2：空字符串")
    print(top_k_words(2, ""))

    print("测试3：多个空格")
    print(top_k_words(2, "Hello   World"))

    print("测试4：连续标点")
    print(top_k_words(2, "Hi!!! Python???"))

    print("测试5：大小写混合")
    print(top_k_words(2, "AI...  Is GREAT!!!"))

    print("测试6：K = 0")
    print(top_k_words(0, "Python Python Java"))

    print("测试7：K 大于单词种类数")
    print(top_k_words(10, "Python Python Java"))
if __name__ == "__main__":
    main()