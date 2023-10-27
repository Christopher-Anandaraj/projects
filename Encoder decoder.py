"""
while True:
    purpose = input("Do you want to encode or decode? ")

    if purpose == "encode" or purpose == "e":
        enc_text = input("Enter text to encode: ")
        print(enc_text)  
        while True:
            try:
                scale = int(input("Enter your scale of encryption: "))
                break
            except ValueError:
                print("Input a number.")
                continue
        


        
    elif purpose == "decode" or purpose == "d":
        dec_text = input("Enter text to decode: ")
        break
    else:
        print("Invalid input. Please enter 'encode' or 'decode'.")
    
    break
"""

import pyperclip

while True:
    purpose = input("Do you want to encode or decode? ")

    if purpose == "encode" or purpose == "e":
        enc_text = input("Enter text to encode: ")

        while True:
            try:
                scale = int(input("Enter your scale of encryption (1-256): "))
                if 1 <= scale <= 256:
                    break  # Break the inner loop if the input is a valid number within the specified range
                else:
                    print("Scale must be between 1 and 256.")
            except ValueError:
                print("Input a valid number.")

        # Encrypt the input text using ASCII index and scale
        encrypted_text = ""
        for char in enc_text:
            encrypted_char = chr((ord(char) + scale) % 256)  # Encrypt using ASCII and wrap around if necessary
            encrypted_text += encrypted_char

        print("Encrypted text:", encrypted_text)
        
        # Copy the encrypted text to clipboard
        pyperclip.copy(encrypted_text)
        print("Encrypted text copied to clipboard.")

    elif purpose == "decode" or purpose == "d":
        dec_text = input("Enter text to decode: ")

        while True:
            try:
                scale = int(input("Enter your scale of decryption (1-256): "))
                if 1 <= scale <= 256:
                    break  # Break the inner loop if the input is a valid number within the specified range
                else:
                    print("Scale must be between 1 and 256.")
            except ValueError:
                print("Input a valid number.")

        
        decrypted_text = ""
        for char in dec_text:
            decrypted_char = chr((ord(char) - scale) % 256)  
            decrypted_text += decrypted_char

        print("Decrypted text:", decrypted_text)

    else:
        print("Invalid input. Please enter 'encode' or 'decode'.")