def decryption(phrase, key):  # This function will decrypt the message. It passes 2 parameters the encrypted phrase and a the key.
    key = key.lower()
    key = ord(key) - 96  # For easier manipulation they given key is converted into a int.
    decryptedPhrase = ''  # This will hold the end result.
    phrase = phrase.lower()  # To make sure program won't crash make the whole string lower case.
   
    for ch in phrase:  # This for loop will iterate through the string to change the each individual chars.
        if ch.isdigit() or ch == '.' or ch == ',' or ch == ' ' or ch == ';':  # It wont chance numbers, spaces, comas and punctuation
            decryptedPhrase += ch 
            continue
        else:
            ch = ord(ch) - key  # Revert to original char using key.
            if ch < 97:
                ch += 26
            ch = chr(ch)  # Conver int back into char to be added into string.
            decryptedPhrase += ch

    return decryptedPhrase  # Return the decrypted prhase


phrase = input('Please enter the message you want to decrypt: ')

key = input('Please enter your key: ')


print('This is your decrypted message: ')
print(decryption(phrase, key))
