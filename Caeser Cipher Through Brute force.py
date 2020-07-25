# Caesar Cipher Decoder

print('The program was coded by Akshat Upadhyay\n\n\n')


message = 'Tf uhtl pz Hrzoha Bwhkofhf'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) 
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('%s : %s key' % (translated,key))
