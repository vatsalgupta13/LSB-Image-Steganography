from Cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography('My secret password key')

# Save the encrypted file inside the image
crypto_steganography.hide('test.png', 'test_output.png', 'Bye')
secret = crypto_steganography.retrieve('test_output.png')
print(secret)
# My secret message
