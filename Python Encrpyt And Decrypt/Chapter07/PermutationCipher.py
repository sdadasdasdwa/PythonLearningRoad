def main():
    Message = "Common sense is not so common."
    Key = 8

    ciphertext = encryptMessage(Key, Message)
    # print cipher content
    print(ciphertext + "|")


def encryptMessage(key, message):
    # each strings mapping the column
    ciphertext = [''] * key
    
    # literate each colume in plaintext
    for column in range(key):
        currentIndex = column
        
        # go on literating until the currentIndex value overweight than message length
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
    
    return ''.join(ciphertext)
    
if __name__ == "__main__":
    main()
