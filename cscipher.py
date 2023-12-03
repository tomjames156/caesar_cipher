letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
] # all english letters

def encrypt(plain_text=''):
    # encrypts plain text to cipher text using the Caesar cipher
    cipher_text = ''
    if plain_text == '': # if no text passed as a parameter 
        plain_text = input("Enter some plain text to be converted\n=> ") # prompts user for the plain text

    for char in plain_text:
        if char.isalpha():
            new_char = letters[(letters.index(char.upper()) + 3) % 26] # get the letter to be substituted for the letter in the plain text
            if char.isupper(): # add to cipher in uppercase
                cipher_text += new_char.upper()
            else: # add to cipher in lowercase
                cipher_text += new_char.lower()
        else:
            # add non alphabetic characters without any subtitution
            cipher_text += char

    return cipher_text

cipher = encrypt("Hey there i'm some plain text")
print(f"\n{cipher}")

def decrypt(cipher=''):
    """Retrieves the plain text from a Caesar cipher text"""

    plain_text = ''
    if cipher == '': # if no cipher text passed as a parameter
        cipher = input("Enter the cipher text you want to decrypt\n=> ") #prompts user for the cipher text
    
    for char in cipher:
        if char.isalpha():
            new_char = letters[(letters.index(char.upper()) - 3) % 26] # get the the letter in the plain text that was substituted
            if char.isupper(): # add to plain text in uppercase
                plain_text += new_char.upper()
            else: # add to plain text in lowercase
                plain_text += new_char.lower()
        else:
            # add non alphabetic characters without any subtitution
            plain_text += char
    
    return(plain_text)

plain = decrypt(cipher)
print(f"\n{plain}")