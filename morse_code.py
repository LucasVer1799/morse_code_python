def encrypt_to_morse(message):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                  'G': '--.', 'H': '....', 'I': '..', 'J': '.--', 'K': '-.-', 'L': '.-..',
                  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', ' ': ' '}

    encrypted = ''
    for char in message.upper():
        encrypted += morse_code[char] + ' '

    return encrypted


def decrypt(message):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                  'G': '--.', 'H': '....', 'I': '..', 'J': '.--', 'K': '-.-', 'L': '.-..',
                  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', ' ': ' '}

    morse_code_reverse = {v: k for k, v in morse_code.items()}

    decrypted = ''
    morse_chars = message.split(' ')
    for morse_char in morse_chars:
        if morse_char in morse_code_reverse:
            decrypted += morse_code_reverse[morse_char]
        elif morse_char == '':
            decrypted += ' '
        else:
            decrypted += 'undefined'

    return decrypted.title()


while True:
    choice = input("Press '1' to encrypt or '2' to decrypt: ")

    if choice == '1':
        name = input('What would you like to encrypt?: ')
        result = encrypt_to_morse(name)
        print(result)
    elif choice == '2':
        name = input('What would you like to decrypt?: ')
        result = decrypt(name)
        print(result)
    stop = input("Type 'Y' if you would like to continue or 'N' if you would like to stop: ")
    if stop == 'N' or 'n':
        break
    else:
        pass
