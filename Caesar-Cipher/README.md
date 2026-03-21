#  Caesar Cipher – Encrypt & Decrypt

A simple Python implementation of the **Caesar Cipher**, one of the oldest and most well-known encryption techniques. Supports both encryption and decryption of messages with a custom shift key.

---

##  What is a Caesar Cipher?

A Caesar Cipher works by shifting each letter in the message by a fixed number of positions in the alphabet. For example, with a shift of 3:

```
A → D    B → E    Z → C
```

It's a substitution cipher — not secure by modern standards, but a great introduction to classical cryptography.

---

##  Features

- Encrypt any plaintext message using a custom shift key
- Decrypt any ciphertext back to the original message
- Preserves letter case (uppercase stays uppercase)
- Non-alphabetic characters (spaces, numbers, punctuation) are passed through unchanged
- Simple interactive CLI menu

---

##  Requirements

- Python 3.x
- No external libraries required

---

##  Usage

Run the script using:

```bash
python cipher.py
```

You'll be presented with a menu:

```
1. Encrypt
2. Decrypt
3. Exit
```

### Encrypting a message

```
Enter choice 1 or 2: 1
Enter the message to be encrypted: Hello World
Shift key used to encrypt the message: 3
Your encrypted message: Khoor Zruog
```

### Decrypting a message

```
Enter choice 1 or 2: 2
Enter the message to be decrypted: Khoor Zruog
Shift key used to decrypt the message: 3
Your decrypted message: Hello World
```

---

##  Notes

- The shift key must be a positive integer between `1` and `25`.
- Using a shift of `0` or `26` will return the original message unchanged.
- **The same shift key used to encrypt must be used to decrypt.**
- This cipher is not cryptographically secure and should not be used for sensitive data.

---

##  Planned Improvements

- [ ] Add **frequency analysis** to automatically detect the shift key
- [ ] Support for **brute-force decryption** (try all 25 possible shifts)
- [ ] Input validation and error handling for invalid shift values
- [ ] File encryption support (read from / write to `.txt` files)