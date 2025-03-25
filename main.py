def get_book_text( filepath ):
    with open(filepath) as fd:
        text = fd.read()
    return text

def main():
    print(get_book_text("./books/frankenstein.txt"))


if __name__ == "__main__":
    main()
