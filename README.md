# PRODIGY_CS_01
This repository contains a Python program that implements the Caesar Cipher algorithm for both encryption and decryption of text. Users can input a message and specify a shift value to perform the encryption or decryption process.
# Caesar Cipher Implementation in Python

This repository contains a Python program that implements the Caesar Cipher algorithm, a simple encryption technique that shifts the characters in a message by a specified number of positions in the alphabet.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down or up the alphabet. This program allows users to both encrypt and decrypt messages by providing the desired shift value.

## Features
- **Encrypt a message:** Convert plaintext into ciphertext using a specified shift.
- **Decrypt a message:** Convert ciphertext back into plaintext using the same shift.
- **Customizable shift value:** Users can specify any integer as the shift value.

## Prerequisites
To run this program, you will need:
- Python 3.x installed on your system.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/nitixsh/caesar-cipher-python.git
    ```
2. Navigate to the project directory:
    ```bash
    cd caesar-cipher-python
    ```

## Usage
1. Run the Python script:
    ```bash
    python caesar_cipher.py
    ```
2. Enter the text you want to encrypt or decrypt.
3. Input the shift value when prompted.

The program will output the encrypted or decrypted text based on your input.

## Examples
### Encrypting a Message
```plaintext
Enter the message: hello
Enter the shift value: 3
Encrypted message: khoor

### Decrypting a Message
```plaintext
Enter the message: khoor
Enter the shift value: 3
Decrypted message: hello
