def printer(i):
    text = "Python Is Fun"

    match i:
        case 1:
            print("原文："+text)
        case 2:
            print("小写："+text.lower())
        case 3:
            print("字符数："+str(len(text)))
        case 4:
            print("单词数："+str(len(text.split())))

def main():
    for i in range(1, 5):
        printer(i)

if __name__ == "__main__":
            main()


