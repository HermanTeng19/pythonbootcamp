alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_number, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_number *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


from d8_begin_caesarCipherArt import logo
print(logo)
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    shift = shift % 26
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. otherwise type 'no'. \n")
    if restart.lower() == 'no':
        should_end = True
        print("Goodbye")



