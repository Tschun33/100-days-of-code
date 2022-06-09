alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(encrypt_text, num, choice):
    if choice == "encode":
        new_text = ""
        i = 0
        while i < len(encrypt_text):
            index = alphabet.index(encrypt_text[i])
            new_index = index + num
            while new_index >= 26:
                new_index = new_index - 26
            new_text += alphabet[new_index]
            i += 1
        print(new_text)
    elif choice == "decode":
        new_text = ""
        i = 0
        while i < len(encrypt_text):
            index = alphabet.index(encrypt_text[i])
            new_index = index - num
            while new_index >= 26:
                new_index = new_index - 26
            new_text += alphabet[new_index]
            i += 1
        print(new_text)


encrypt(text, shift, direction)



