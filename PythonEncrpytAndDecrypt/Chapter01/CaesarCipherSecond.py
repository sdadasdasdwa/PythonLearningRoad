# message to encrypt or decrypt
# message = "This is my secret message."
message = 'Tvi6ki6kz!k6sq5s7kzs66ousn'

# key
key = 13

# mode
# mode = "encrypt"
mode = "decrypt"

# symbols which might be encrypted
symbols = "abcdefghjklmnopqrstuvwxyz1234567890 !?."

# store the encrypt or decrypt result
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
print(translate)
