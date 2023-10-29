import pyperclip

while True:
    purpose = input("Do you want to encrypt or decrypt? ")

    if purpose == "encrypted" or purpose == "e":
        enc_text = input("Enter text to encrypt: ")

        while True:
            try:
                shift = int(input("Enter your shift value (1-25): "))
                if 1 <= shift <= 25:
                    break  
                else:
                    print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Input a valid number.")

        
        encrypted_text = ""
        for char in enc_text:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
                encrypted_text += shifted_char
            else:
                encrypted_text += char

        print("Encrypted text:", encrypted_text)

       
        pyperclip.copy(encrypted_text)
        print("Encrypted text copied to clipboard.\n")

    elif purpose == "decrypt" or purpose == "d":
        dec_text = input("Enter text to decrypt: ")

        while True:
            try:
                shift = int(input("Enter your shift value (1-25): "))
                if 1 <= shift <= 25:
                    break  
                else:
                    print("Shift value must be between 1 and 25.")
            except ValueError:
                print("Input a valid number.")

        
        decrypted_text = ""
        for char in dec_text:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
                decrypted_text += shifted_char
            else:
                decrypted_text += char

        print("Decrypted text:", decrypted_text, "\n")

    elif purpose == "kill":
        break
    else:
        print("Invalid input. Please enter 'encrypt' or 'decrypt'.\n")
    elif purpose == "kill":
        break
    else:
        print("Invalid input. Please enter 'encrypt' or 'decrypt'.\n")
