def encryption(phrase, key):  # This function will encrypt the message. It passes 2 parameters the message to be encrypted and a the key.
    key = key.lower()
    key = ord(key) - 96  # For easier manipulation they given key is converted into a int.
    encryptedPhrase = ''  # This will hold the end result.
    phrase = phrase.lower()  # To make sure program won't crash make the whole string lower case.
    
    for ch in phrase:  # This for loop will iterate through the string to change the each individual chars.
        if ch.isdigit() or ch == '.' or ch == ',' or ch == ' ' or ch ==';':  # It wont chance numbers, spaces, comas and punctuation
            encryptedPhrase += ch 
            continue
        else:
            ch = ord(ch) + key  # Revert to original char using key.
            if ch > 122:
                ch -= 26
            ch = chr(ch)  # Conver int back into char to be added into string.
            encryptedPhrase += ch

    return encryptedPhrase  # Return the encrypted prhase  


phrase = input('Please enter the message you want to encrypt: ')

key = input('Please enter a key: ')


print('This is your encrypted message: ')
print(encryption(phrase, key))
