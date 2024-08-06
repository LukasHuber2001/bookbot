def main():
    path = "books/frankenstein.txt"
    fileContents = readFile(path)

    print("--- Begin report of books/frankenstein.txt ---")
    print(str(countWords(fileContents))+" words were found in this book\n")
    countChar(fileContents)
    print("--- End report ---")

def readFile(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def countWords(text):
    wordArray = text.split()
    return len(wordArray)

def countChar(text):
    charList = []
    charArray = list(text.lower())
    charDict = {}
    charCounter = 0
    for char in charArray:
        if char not in charDict:
            charDict[char] = 1
        else:
            charDict[char] += 1
    for char in charDict:
        
        if char.isalpha():
            specificDict = {}
            specificDict["char"] = char
            specificDict["occurance"] = charDict[char]
            charCounter += specificDict["occurance"]
            charList.append(specificDict)
            charList.sort(reverse=True, key=orderBy)
    print(str(charCounter)+" Characters were found in this book\n")
    for i in range(len(charList)):
        print(f"The {charList[i]['char']} character was found {charList[i]['occurance']} times")      
    pass

def orderBy(dist):
    return dist["occurance"]

print(main())