import time


def diplayIntro():
    print("There you will choose method between encryption and decryption")
    print()


def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("which cave you want to choose? (1 or 2)")
        cave = input()
    return cave


def checkCave(number, text):
    print("you have made your choice")
    time.sleep(2)
    result = ""
    if number == "1":
        print("this mode is encrypt")
        shift = input("please input encrypt shift number: ")
        result = caesar_cipher(text, int(shift), "encrypt")
        print("encrypt result : {}".format(result))
    elif number == "2":
        print("this mode is decrypt")
        shift = input("please input decrypt shift number: ")
        result = caesar_cipher(text, int(shift), "decrypt")
        print("decrypt result : {}".format(result))


def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result


if __name__ == "__main__":

    original = "The Secret Password is Rosebud"
    decryptStr = (
        "UMMSVMAA: CvKwuuwv xibqmvkm qv xtivvqvo i zmdmvom bpib qa ewzbp epqtm."
    )
    encryptAgain = "yes"
    while encryptAgain == "yes" or encryptAgain == "y":
        diplayIntro()
        numberChosen = chooseCave()
        checkCave(numberChosen, decryptStr)
        encryptAgain = input("Do you want to play again?")
