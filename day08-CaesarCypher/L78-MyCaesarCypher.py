alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def greet_with_name(name, location):
    print(f"Hello {name} form {location}")
    print("Welcome to Caesar Cypher!")
    print("You can encode or decode messages with this.")
    print("Make sure to remember or ask for the shift code!")


def shift_character(char, shift):
    shift_complete = False
    for i in range(0, len(alphabet)):
        if char == alphabet[i] and not shift_complete:
            new_pos = i + shift
            new_pos_in_range = False
            while not new_pos_in_range:
                if new_pos > 25:
                    new_pos_in_range = False
                    new_pos -= 26
                else:
                    new_pos_in_range = True
            char = alphabet[new_pos]
            shift_complete = True
    return char


def encrypt(text, shift):
    input = list(text)
    encrypted_string = []
    for char in input:
        encrypted_string.append(shift_character(char, shift))
    return "".join(encrypted_string)


def unshift_character(char, shift):
    shift_complete = False
    for i in range(0, len(alphabet)):
        if char == alphabet[i] and not shift_complete:
            new_pos = i - shift
            new_pos_in_range = False
            while not new_pos_in_range:
                if new_pos < 0 :
                    new_pos_in_range = False
                    new_pos += 26
                else:
                    new_pos_in_range = True
            char = alphabet[new_pos]
            shift_complete = True
    return char


def decrypt(text, shift):
    input = list(text)
    decrypted_string = []
    for char in input:
        decrypted_string.append(unshift_character(char, shift))
    return "".join(decrypted_string)


greet_with_name(location="Mainz", name="Henrik")  # - Keyword arguments, these ignore the order of input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt")
text = input("Type your message: \n").lower()
shift = int(input("Choose a shift value: "))
if direction == 'encode':
    encrypted_message = encrypt(text, shift)
    print(f"Your encrypted message is {encrypted_message}")
elif direction == 'decode':
    decrypted_message = decrypt(text, shift)
    print(f"Your decrypted message read: {decrypted_message}")
else:
    print("Invalid input, please try again.")


# greet_with_name("Henrik", "Mainz") - this is a positional argument, as the order is important for correct execution
