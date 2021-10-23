alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt")
text = input("Type your message: \n").lower()
shift = int(input("Choose a shift value: "))


def caesar(plain_text, shift_amount, cypher_direction):
    cypher_text = ""
    shift_amount = shift_amount % 26
    if cypher_direction == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cypher_text += new_letter
        else:
            cypher_text += char
    print(f"The {cypher_direction}d string is {cypher_text}.")


caesar(text, shift, direction)
