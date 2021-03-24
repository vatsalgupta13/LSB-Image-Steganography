from Cryptosteganography import CryptoSteganography
import sys

message = None
with open('sample.mp3', "rb") as f:
    message = f.read()

passkey = "Secret123"
crypto_steganography = CryptoSteganography(passkey)

# Save the encrypted file inside the image
crypto_steganography.hide('test.png', 'output_test.png', message)

pass_key = input("Enter the Password to decrypt the file: ")
if pass_key != passkey:
    print("\nWRONG PASSWORD!\n")
    pass_key = input ("Last chance to enter the correct password: ")
    if pass_key != passkey:
        print("You have exhausted your chances to enter the password")
        sys.exit()
    
# Retrieve the file (the previous crypto_steganography instance could be used but I instantiate a brand new object
# with the same password key just to demonstrate that can it can be used to decrypt)
crypto_steganography = CryptoSteganography(pass_key)
decrypted_bin = crypto_steganography.retrieve('output_test.png')

# Save the data to a new file
with open('decrypted_sample.mp3', 'wb') as f:
      f.write(decrypted_bin)
