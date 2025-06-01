import os
import math, random, sys, time

sys.path.append("/Users/frank/Projects/VscodeProjects/PythonLearningRoad")

from PythonEncrpytAndDecrypt.Chapter07.PermutationCipher import encryptMessage
from PythonEncrpytAndDecrypt.Chapter08.transpositionDecrypt import decryptMessage


def main():
    inputFilename = "PythonEncrpytAndDecrypt/Chapter10/frankenstein.txt"
    outputFilename = "PythonEncrpytAndDecrypt/Chapter10/frankenstein.encrypted.txt"
    # outputFilename = "PythonEncrpytAndDecrypt/Chapter10/frankenstein.decrypted.txt"
    myKey = 10
    myMode = "encrypt"
    # myMode = "decrypt"

    # if the input file not exists, the program will terminate in advance.
    if not os.path.exists(inputFilename):
        print("The file %s does not exist. Quitting..." % (inputFilename))
        sys.exit()

    # if the output file exists, give the change for user to exit.
    if os.path.exists(outputFilename):
        print(
            "This will overwrite the file %s. (C)ontinue or (Q)uit?" % (outputFilename)
        )
        response = input(">")
        if not response.lower().startswith("c"):
            sys.exit()

    # read from input file
    fileObject = open(inputFilename)
    content = fileObject.read()
    fileObject.close()

    print("%sing..." % (myMode.title()))

    # calculate the encrypt/decrypt time
    startTime = time.time()
    if myMode == "encrypt":
        translated = encryptMessage(myKey, content)
    elif myMode == "decrypt":
        translated = decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print("%sion time: %s seconds" % (myMode.title(), totalTime))

    # write in the output file
    outputFileObj = open(outputFilename, "w")
    outputFileObj.write(translated)
    outputFileObj.close()

    print("Done %sing %s (%s characters)." % (myMode, inputFilename, len(content)))
    print("%sed file is %s." % (myMode.title(), outputFilename))


if __name__ == "__main__":
    main()
