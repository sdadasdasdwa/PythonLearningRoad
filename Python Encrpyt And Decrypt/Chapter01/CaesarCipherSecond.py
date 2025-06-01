# message to encrypt or decrypt
# message = "This is my secret message."
message = 'ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K'

# key
# key = 13

# mode
# mode = "encrypt"
mode = "decrypt"

# symbols which might be encrypted
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# store the encrypt or decrypt result


for key in range(len(symbols)):
    translate = ""
    for symbol in message:
        if symbol in symbols:
            symbolIndex = symbols.find(symbol)
            shift = key if mode == "encrypt" else -key
            symbolIndex = (shift + symbolIndex) % (len(symbols))
            translate += symbols[symbolIndex]
        else:
            translate += symbol

    # print result
    print('Key # %s: %s' % (key, translate))


