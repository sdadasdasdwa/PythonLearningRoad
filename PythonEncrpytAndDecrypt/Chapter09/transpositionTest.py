import math, random, sys
sys.path.append('/Users/frank/Projects/VscodeProjects/PythonLearningRoad')
from PythonEncrpytAndDecrypt.Chapter07.PermutationCipher import encryptMessage
from PythonEncrpytAndDecrypt.Chapter08.transpositionDecrypt import decryptMessage


def main():
    random.seed(42)

    # 1. test 20 times
    for i in range(20):

        # 2. generate random message
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 20)
        # 3. transform from String to list
        message = list(message)
        random.shuffle(message)
        message = "".join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        for key in range(1, int(len(message) / 2)):
            encrypted = encryptMessage(key, message)
            decrypted = decryptMessage(key, encrypted)

            # 4. verify whether is corrent
            if decrypted != message:
                print("Mismatch with key %s and message %s." % (key, message))
                print("Decrypted as: " + decrypted)
                sys.exit()

    print("Transposition cipher test passed.")


if __name__ == "__main__":
    main()
