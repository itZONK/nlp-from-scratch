from src.textlab.day03.file_reader import read_text
from src.textlab.day02.text_cleanV1 import top_k_words,clean_text,word_count

def main():
    text1 = "Hi!!! PYTHON?"
    result1 = clean_text(text1)
    assert result1 == ["hi", "python"]
    assert result1 == ["hi", ""]

if __name__ == "__main__":
    main()