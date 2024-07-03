def main():
    book_path = "books/frankenstein.txt"
    text = getBookText(book_path)
    num_words = countWords(text)
    num_characters = countCharacters(text)
    print(f"-- Begin report of {book_path} --")
    print(f"{num_words} words were found in the document \n")
    for element, count in num_characters.items():
        if element.isalpha():
            print("The", element, "character was found", count,"times.")
    print("--- End of Report ---")

def getBookText(path):
    with open(path) as f:
        return f.read()
    
def countWords(book):
    words = book.split()
    return len(words)

def countCharacters(text):
    countDict = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,
    }
    for element in text:
        smallText = element.lower()
        if smallText in countDict:
            countDict[smallText] += 1
        else:
            countDict[smallText] = 1
    return countDict

#def sortText(dict):
#    return dict["num"]

main()
