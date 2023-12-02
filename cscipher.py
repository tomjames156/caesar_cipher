letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

def encrypt(plain_text=''):
    cipher_text = ''
    if plain_text == '':
        plain_text = input("Enter some plain text to be converted\n=> ")

    print("Converting to Cipher ...")

    for char in plain_text:
        if char.isalpha():
            new_char = letters[(letters.index(char.upper()) + 3) % 26]
            if char.isupper():
                cipher_text += new_char.upper()
            else:
                cipher_text += new_char.lower()
        else:
            cipher_text += char

    return cipher_text

cipher = encrypt("Hey there i'm some plain text")
print(f"\n{cipher}")