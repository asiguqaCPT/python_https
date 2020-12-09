DECIPHER = {v: k for k, v in CIPHER.items()}

def decrpyt(ciphertext: str):
    return ''.join(DECIPHER.get(letter, letter) for letter in ciphertext)
