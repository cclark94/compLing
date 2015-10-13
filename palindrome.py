# Christian Clark, cec81@pitt.edu, September 3 2014

palindrome = False

print 'Hello! Let\'s find a palindrome.'

while not palindrome:
    userString = raw_input('Give me a word: ')

    string = userString
    for char in ',"\':. ':
        string = string.replace(char, '')
    string = string.lower()

    if len(userString) < 3:
        print 'Sorry,', '"'+userString+'"', 'is too short to be a palindrome.'

    else:
        mismatchFound = False
        for i in range(len(string)/2):
            if string[i] != string[-1-i]:
                mismatchFound = True
                print 'NO,', '"'+userString+'"', 'is not a palindrome.'
                break

        if not mismatchFound:
            palindrome = True
            print 'YES,', '"'+userString+'"', 'is a palindrome.'

print 'Goodbye.'
