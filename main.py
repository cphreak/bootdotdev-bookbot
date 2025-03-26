from stats import *
import sys

def main():
    mydict = {}
    # print(sys.argv)
    # print(len(sys.argv))
    if (len(sys.argv) <= 1):
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    # print(sys.argv[1])
    mytext = get_book_text(sys.argv[1])
    x = word_count( mytext )
    mydict = token_count( mydict, mytext )
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {x} total words")
    print("--------- Character Count -------")
#    print( mydict )
    mylist = convert2list(mydict)
    for i in mylist:
        print(f"{ i["character"]}: { i["count"]}")


if __name__ == "__main__":
    main()
