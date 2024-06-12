def main():
    with open("books/frankenstein.txt") as text:
        fullText = text.read()

        MakeReport(fullText)
        return


def MakeReport(fullText):
    print("### Start report ###")
    print(f"{CountWords(fullText)} words have been counted")
    charcol = Countchars(fullText)

    for i in range(0, len(charcol)):
        print(f"we looked around and found '{chr(65 + i)}' {charcol[i]} times ")


    print("### End report ###")

    pass

def CountWords(fullText):
    count = 0
    curText = fullText.split()
    for word in curText:
        count += 1
    return count


def Countchars(fullText):
    charCount = [0] * 26

    for letter in fullText:
        if(letter == ' '): continue
        char = ord(letter) - 97
        if(char < 0 or char > 25): continue
        charCount[char] += 1

    return charCount



main()