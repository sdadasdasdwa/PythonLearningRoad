# to decrypt the permutation cipher, persist that the key is known


import math


def main():
    pass
    myMessage = "H■cb■■irhdeuousBdi■■■prrtyevdgp■nir■■eerit■eatoreechadihf■paken■ge■b■te■dih■aoa.da■tts■tn "
    myKey = 9

    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext + "|")


def decryptMessage(key, message):
    # 1. culculate the column numbers
    numOfColumes = int(math.ceil(len(message) / float(key)))
    # 2. row number
    numOfRows = key
    # 3. Number of shadows
    numOfShadedBoxes = numOfColumes * numOfRows - len(message)
    # 4. plaintext result
    plaintext = [""] * numOfColumes

    column = 0
    row = 0

    # 5. literate encryption string, put it into 8*4 matrix
    for symbol in message:
        plaintext[column] += symbol
        column += 1

        # 6. while literate the last column or in the shaded circumstance
        if (column == numOfColumes) or (
            column == numOfColumes - 1 and row >= numOfRows - numOfShadedBoxes
        ):
            column = 0
            row += 1
    return "".join(plaintext)


if __name__ == "__main__":
    main()
