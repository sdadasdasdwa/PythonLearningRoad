import sys

sys.path.append("/Users/frank/Projects/VscodeProjects/PythonLearningRoad")

UPPERLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + " \t\n"


# load English words from dictionary
def loadDictionary():
    dictionaryFile = open("PythonEncrpytAndDecrypt/Chapter11/dictionary.txt")
    englishWords = {}
    for word in dictionaryFile.read().split("\n"):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


ENGLISH_WORDS = loadDictionary()


def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    print("words Match : %s" % wordsMatch)
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    print("letters Match : %s" % lettersMatch)
    return wordsMatch and lettersMatch


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)

    possibleWords = message.split()

    if possibleWords == []:
        return 0.0  # don't have word, return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    print(
        "words match : %d , words length : %d, English words match rate %.2f"
        % (float(matches), len(possibleWords), (float(matches) / len(possibleWords)))
    )
    return float(matches) / len(possibleWords)


# remove symbols which were not belong to LETTERS_AND_SPACE list
def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return "".join(lettersOnly)


if __name__ == "__main__":
    print(isEnglish("Is this sentence english text?"))
