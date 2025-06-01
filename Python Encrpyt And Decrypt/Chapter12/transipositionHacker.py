import math, random, sys, time

import pyperclip

sys.path.append("/Users/frank/Projects/VscodeProjects/PythonLearningRoad")

from PythonEncrpytAndDecrypt.Chapter07.PermutationCipher import encryptMessage
from PythonEncrpytAndDecrypt.Chapter08.transpositionDecrypt import decryptMessage
from PythonEncrpytAndDecrypt.Chapter11.detectEnglish import isEnglish


def main():
    # encryption text
    message = " halfuheakjfh aksfhduealksdf "

    hackMessage = hackTransposition(message)

    if hackMessage == None:
        print("Failed to hack transposition")
    else:
        print("Copying hacked message to clipboard")
        print(hackMessage)
        pyperclip.copy(hackMessage)


def hackTransposition(message):
    print("Hacking.......")

    for key in range(1, len(message)):
        print("Trying key #%s..." % key)

        decryptedText = decryptMessage(key, message)

        if isEnglish(decryptedText):
            print()
            print("Possible encryption hack: ")
            print("Key %s: %s" % (key, decryptedText[:100]))
            print()
            print("Enter D if done, anything else to continue hacking:")

            response = input(">")
            if response.strip().upper().startswith("D"):
                return decryptedText

    return None


if __name__ == "__main__":
    main()
