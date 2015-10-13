# Christian Clark, cec81@pitt.edu, 18 September 2014

# Copy over the getTokens() function from Homework #2.
# [1] Your code below:
def getTokens(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a list of tokenized words.
    Symbols are separated out, and upper case is lowered.
    """

    sym = "~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?"
    # [1] Complete this function. YOUR CODE BELOW.
    for s in sym:
        txt = txt.replace(s, ' '+s+' ')
    
    return txt.lower().split()

# Copy over the isPalindrome() function from Lab4.pdf, page 16.
# [2] Your code below:
def isPalindrome(wd):
    """Palindrome test. Takes a string, returns True/False."""
    
    rev = ''
    for i in wd:
        rev = i + rev   

    return wd == rev


# Now open austen-emma.txt for reading, and then assign the 
# entire text content to a string variable.
# MAKE SURE TO CLOSE THE FILE WHEN YOU'RE DONE.
# [3] Your code below:
inFile = open('austen-emma.txt')
text = inFile.read()
inFile.close()

# Tokenize the text using the getTokens function above. Create
# a list variable "toks" that holds the tokenized result.
# [4] Your code below:
toks = getTokens(text)

# Uncomment command below if you want to look at the first
# 30 words of Emma. 
#print toks[:30]


# We initialize 'palcount' here as an empty dictionary.
# It will hold the palindrome words and their counts. 
palcount = {}


# Now iterate through the tokens; for each token, see if
# it is an all-alphabetic word and a palindrome. If it is,
# update palcount. To see if a word consists of alphabetic
# characters only, use the .isalpha() string method. 
# [5] Your code below:
for tok in toks:
    if tok.isalpha() and isPalindrome(tok):
        if palcount.has_key(tok):
            palcount[tok] += 1
        else:
            palcount[tok] = 1

# palcount should be populated now. Uncomment below to see it.
#print palcount


# Let's write out your palindrome results to a file.
# First open a file named 'pal_emma_out.txt' for writing.
# [6] Your code below:

outFile = open('pal_emma_out.txt', 'w')

# Now write out the content of palcount to the file. 
# Follow the file format specified.
# DON'T FORGET TO CLOSE YOUR FILE WHEN YOU'RE DONE. 
# [7] Your code below:
pals = sorted(palcount)

for pal in pals:
    outFile.write(pal+' '+str(palcount[pal])+'\n') 

outFile.close()
