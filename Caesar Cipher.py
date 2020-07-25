# Caesar Cipher 

''' The basic principle applied is to shift the letters of the message by
    the specific key provided by the user to encrypt and also to decrypt it .  '''

print('The program was coded by Akshat Upadhyay\n\n')
MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you want to encrypt or decrypt the message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTransMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    trans = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            trans += chr(num)
        else:
            trans += symbol
    return trans

mode = getMode()
message = getMessage()
key = getKey()

print('Translated text is:')
print(getTransMessage(mode, message, key))
