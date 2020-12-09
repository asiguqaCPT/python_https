CIPHER = {'a':'z', 'A':'Z','b':'a'} # And so on

def encrypt(plaintext: str):
    return ''.join(CIPHER.get(letter, letter) for letter in plaintext)
