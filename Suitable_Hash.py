import hashlib


def pow(string, end):
    string = list(string)
    for thisOne in writeAllStates(string):
        print(hasher(thisOne))
        if hasher(thisOne)[len(end)*-1:] == end:
            return thisOne


def writeAllStates(listOfCharecter):
    remaining_text = listOfCharecter[:]  # copy the array
    # we start with an empty string so we can easily append to it
    options = ['']
    while remaining_text:
        # get the first letter and removes it from the list in one go
        next_letter = remaining_text.pop(0)

    # and add one option with lowercase and one with uppercase
    # for every existing option
        options = (
            [option + next_letter.lower() for option in options]
            + [option + next_letter.upper() for option in options])
    # give new upper and lower to all Incomplete words And the number of words doubles
    return options


def hasher(string):
    hashObject = hashlib.sha256()
    hashObject.update(string.encode())
    answer = hashObject.hexdigest()
    return answer


text = input('Enter your Word or Sentences that want find Hash of them : ')
endWith = input('Enter your End of the word hashed (like 1111) : ')
print('Your suitable Word is : %s' % pow(text, endWith))
