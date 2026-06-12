def encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            encrypted += char

    return encrypted


def decrypt(text, shift):
    decrypted = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            else:
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            decrypted += char

    return decrypted


print("===================================")
print("   CAESAR CIPHER ENCRYPTION TOOL")
print("===================================")

plaintext = input("\nEnter Text: ")

while True:
    try:
        shift = int(input("Enter Shift Key (1-25): "))

        if 1 <= shift <= 25:
            break

        print("Shift key must be between 1 and 25.")

    except ValueError:
        print("Please enter a valid number.")


encrypted_text = encrypt(plaintext, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\n========== RESULTS ==========")
print("Original Text :", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

print("\n========== STATUS ==========")

if plaintext == decrypted_text:
    print("✅ Encryption and Decryption Successful")
else:
    print("❌ Validation Failed")
