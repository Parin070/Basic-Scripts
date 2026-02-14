def encrypt(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ""
    shifted = ""
    for i in range(len(alphabet)-shift):
        shifted += alphabet[shift + i]
    for j in range(shift):
        shifted += alphabet[j]
    for i in range(len(message)):
        location = 0
        if message[i].isupper():
            location = alphabet.upper().index(message[i])
            encrypted_message += shifted.upper()[location]
        elif message[i].islower():
            location = alphabet.index(message[i])
            encrypted_message += shifted[location]
        else:
            encrypted_message += message[i]
    return f"Your encrypted message: {encrypted_message}"


def decrypt(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_message = ""
    shifted = ""
    for i in range(len(alphabet)-shift):
        shifted += alphabet[shift + i]
    for j in range(shift):
        shifted += alphabet[j]
    for i in range(len(message)):
        location = 0
        if message[i].isupper():
            location = shifted.upper().index(message[i])
            decrypted_message += alphabet.upper()[location]
        elif message[i].islower():
            location = shifted.index(message[i])
            decrypted_message += alphabet[location]
        else:
            decrypted_message += message[i]
    return f"Your decrypted message: {decrypted_message}"
    

while True:
    print("1. Encrypt\n2. Decrypt\n3. Exit")
    choice = int(input("Enter choice 1 or 2: "))
    if choice == 1:
        message = input("Enter the message to be encrypted: ")
        shift = int(input("Shift key used to encrypt the message: "))
        print(encrypt(message, shift))
    elif choice == 2:
        message = input("Enter the message to be decrypted: ")
        shift = int(input("Shift key used to decrypt the message: "))
        print(decrypt(message, shift))
    elif choice == 3:
        print("Thank you for using our services.")
        break 
    else: 
        print("Invalid choice.")