import random
encrypted = input('Please enter a message to decode: ')
decrypted = ''
frequentAlphabet = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b',
                    'v', 'k', 'x', 'q', 'j', 'z']  # based on the english language these are the most frequent letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
quadrigrams = ['that', 'ther', 'with', 'tion', 'here', 'ould', 'aight', 'have', 'hich', 'whic', 'this', 'thin', 'they',
               'atio', 'ever', 'from', 'ough', 'were', 'hing', 'ment']  # based on the english language these are the
# most frequent quadrigrams

newAlphabet = {}
newAlphabet1 = {}

encrypted = ''.join(encrypted.split())  # remove with spaces from phrase
for letters in encrypted:  # here we use a dictionary to find the letter frequency in the cipher
    if letters in newAlphabet:
        newAlphabet[letters] += 1  # if already in dict add 1 to count
    else:
        newAlphabet[letters] = 1  # if not in dict add it to dict with value of 1

newAlphabet = sorted(newAlphabet.items(), key=lambda items: items[1], reverse=True)  # to map it into a new dict with
# the most frequent letters sort it from most frequent to least
for key, values in newAlphabet:  # create the new alphabet dict
    newAlphabet1.setdefault(key, values)

frequentLetters = {}
alphabetKey = list(newAlphabet1.keys())  # separate the keys from dict
alphabetValues = list(newAlphabet1.values())  # separate the values from dict

count = 0


shift = abs(ord(frequentAlphabet[0]) - ord(alphabetKey[0]) + 26)  # for caesar cipher we use the key from frequent
# letters to get the shift value

encrypted = ''.join(encrypted.split())
for i in range(len(encrypted)):  # This loop will decode shifting each letter using the key we got
    if encrypted[i].isdigit() or encrypted[i] == '.':  # skip if there are number of punctuation
        decrypted += encrypted[i]
    else:
        ch = ord(encrypted[i]) + shift  # shift using key making sure it only uses a-z
        if ch > 122:
            ch -= 26
        ch = chr(ch)  # from ascii table switch back to chars
        decrypted += ch

wordList = [decrypted[i:i + 4] for i in range(len(decrypted))]  # to check if the phrase is correct we use the \
# quadrigrams and we check every 4 letters

for t in quadrigrams:
    if t in wordList:
        count += 1  # to make sure it's correct we make sure there is more than one
if count > 1:
    print(decrypted)  # if decrypted print the correct phrase

else:  # message was not decrypted, it will switch the first 2 most common letters
    decrypted = ''
    alphabetKey[0], alphabetKey[1] = alphabetKey[1], alphabetKey[0]  # we change the first and second most frequent
    shift = abs(ord(frequentAlphabet[0]) - ord(alphabetKey[0]) + 26)

    encrypted = ''.join(encrypted.split())
    for i in range(len(encrypted)):  # This loop will decode shifting each letter using the key we got
        if encrypted[i].isdigit() or encrypted[i] == '.':  # skip if there are number of punctuation
            decrypted += encrypted[i]
        else:
            ch = ord(encrypted[i]) + shift  # shift using key making sure it only uses a-z
            if ch > 122:
                ch -= 26
            ch = chr(ch)  # from ascii table switch back to chars
            decrypted += ch

    wordList = [decrypted[i:i + 4] for i in range(len(decrypted))]  # to check if the phrase is correct we use the \
    # quadrigrams and we check every 4 letters

    for t in quadrigrams:
        if t in wordList:
            count += 1  # to make sure it's correct we make sure there is more than one
    if count > 1:
        print(decrypted)  # if decrypted print the correct phrase

    else:  # message was not decrypted with caesar cipher so it will try to solve it by using letter frequency
        # as key
        decrypted = ''
        for items in range(len(alphabetKey)):  # using letter frequency we create a dict to switch each letter
            frequentLetters[alphabetKey[items]] = frequentAlphabet[items]

        for i in range(len(encrypted)):  # loop to change each char at a time
            if encrypted[i].isdigit() or encrypted[i] == '.':  # skip if there are number of punctuation
                decrypted += encrypted[i]
            else:
                ch = frequentLetters[encrypted[i]]
                decrypted += ch
        wordList = [decrypted[i:i + 4] for i in range(len(decrypted))]  # to check if the phrase is correct we use the \
    # quadrigrams and we check every 4 letters
        count = 0
        for t in quadrigrams:
            if t in wordList:
                count += 1  # to make sure it's correct we make sure there is more than one
        if count > 1:
            print(decrypted)  # if decrypted print the correct phrase

        else:  # message was not decrypted using letter frequency so it will use random key to solve
            decrypted = ''
            frequentLetters = {}
            while True:
                shuffledAlphabet = random.sample(alphabet, len(alphabet))  # shuffle the alphabet
                for letters in range(len(shuffledAlphabet)):  # create a dict with the shuffle alphabet
                    frequentLetters[alphabet[letters]] = shuffledAlphabet[letters]

                for i in range(len(encrypted)):  # loop to switch each letter
                    if encrypted[i].isdigit() or encrypted[i] == '.':  # skip if there are number of punctuation
                        decrypted += encrypted[i]
                    else:
                        ch = frequentLetters[encrypted[i]]
                        decrypted += ch
                wordList = [decrypted[i:i + 4] for i in range(len(decrypted))]  # to check if the phrase is correct we 
                # use the quadrigrams and we check every 4 letters
                count = 0
                for t in quadrigrams:
                    if t in wordList:
                        count += 1  # to make sure it's correct we make sure there is more than one
                if count > 1:
                    print(decrypted)  # if decrypted print the correct phrase
                    break
                else:  # keep going until solved :)
                    decrypted = ''
                    shuffledAlphabet = random.sample(alphabet, len(alphabet))
                    continue

