alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def encrypt(userText, letterShift):
    encyptedWord = ""
    # shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text
    for letter in userText:
        indexInAlpha = alphabet.index(letter)
        shiftedIndex = (indexInAlpha+letterShift)%len(alphabet)
        encyptedWord += alphabet[shiftedIndex]
    return encyptedWord

def decrypt (encryptedText, letterShift):
    decryptedWord = ""
    for letter in encryptedText:
        indexInAlpha = alphabet.index(letter)
        decrpytedIndex = indexInAlpha - letterShift
        decryptedWord += alphabet[decrpytedIndex]
    return decryptedWord

if direction == "encode":
    encoded = encrypt(text, shift)
    print(f"The encoded text is: {encoded}")
else:
    decoded = decrypt(text, shift)
    print(f"The decoded text is: {decoded}")

print(alphabet[28])



def encrpytAndDecrypt(encodeOrDecode, inputText, letterShift):
    result = ""
    # shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text
    for letter in inputText:
        indexInAlpha = alphabet.index(letter)
        if encodeOrDecode == "encode":
            shiftedIndex = (indexInAlpha+letterShift)%len(alphabet)
        else:
            shiftedIndex= indexInAlpha - letterShift
        result += alphabet[shiftedIndex]
    return result