lowercase_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                      'n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                      'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in lowercase_alphabet:
            position = lowercase_alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += lowercase_alphabet[new_position]
        elif char in uppercase_alphabet:
            position = uppercase_alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += uppercase_alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's the text after encryption: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in lowercase_alphabet:
            position = lowercase_alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += lowercase_alphabet[new_position]
        elif char in uppercase_alphabet:
            position = uppercase_alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += uppercase_alphabet[new_position]
        else:
            plain_text += char
    print(f"Here's the text after decryption: {plain_text}")
        
wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    text = input("Type your message:\n")
    shift = int(input("Enter shift Key:\n"))
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    go_again = input("Type 'yes' to continue, type 'no' to exit.\n")
    if go_again == 'no':
        wanna_end = True
        print("Have a nice day!.. bye")
