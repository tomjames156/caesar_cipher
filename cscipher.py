letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
plain_text = input("=> ")
cipher_text = ''

print("\nConverting to Cipher ...")
print("..")
print(".")


def encrypt():
    for char in plain_text:
        if char.isalpha():
            new_char = letters[(letters.index(char.upper()) + 3) % 26]
            if char.isupper():
                cipher_text += new_char.upper()
            else:
                cipher_text += new_char.lower()
        else:
            cipher_text += char


print("\n")
print(cipher_text)