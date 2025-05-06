# Ceasar-Cipher
# MyCipher

This project implements a **simple Caesar Cipher** encryption and decryption tool using the command line. It was developed as part of a module assignment for practicing CLI usage, `vi`, `git`, GitHub, and basic programming skills.

## Features

- Takes a shift amount (encryption key) as a command-line argument
- Accepts input from stdin
- Converts all letters to uppercase
- Removes all non-alphabet characters (e.g. digits, spaces, punctuation)
- Outputs encrypted text in blocks of 5 letters, 10 blocks per line

## Usage

### Encrypting

```bash
python3 mycipher.py 3 < plaintext > cryptedtext
