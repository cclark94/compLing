# Christian Clark, cec81@pitt.edu, September 16 2014

fox = """Through three cheese trees three free fleas flew.
While these fleas flew, freezy breeze blew.
Freezy breeze made these three trees freeze."""

tale = """It was the best of times, it was the worst of times,
it was the age of wisdom, it was the age of foolishness,
it was the epoch of belief, it was the epoch of incredulity,
it was the season of Light, it was the season of Darkness,
it was the spring of hope, it was the winter of despair,
we had everything before us, we had nothing before us,
we were all going direct to heaven, we were all going direct
the other way.""" 


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


def getTypeFreq(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a frequency count dictionary.
    KEY is a word, VALUE is its frequency count.
    """
    # [2] Complete this function. YOUR CODE BELOW.
    # Use getTokens().

    freqDict = {}
    tokens = getTokens(txt)

    for t in tokens:
        if freqDict.has_key(t):
            freqDict[t] += 1
        else:
            freqDict[t] = 1
    
    return freqDict


def getTypes(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a alphabetically sorted list of unique word types.
    """ 
    # [3] Complete this function. YOUR CODE BELOW. 
    # Use getTypeFreq().

    types = getTypeFreq(txt).keys()
    types.sort()
    return types


def getXLengthWords(wtypes, x):
    """Takes a list of unique words (= word types) and integer x as
    arguments. Returns a sorted list of words whose length is at least x.
    """
    # [4] Complete this function. YOUR CODE BELOW.

    longEnough = []
    for t in wtypes:
        if len(t) >= x:
            longEnough += [t]

    return longEnough


def getXFreqWords(freqdi, x):
    """Takes a word frequency dictionary and integer x as arguments.
    Returns a sorted list of words that are at least x in frequency.
    """
    # [5] Complete this function. YOUR CODE BELOW.
    
    freqEnough = []
    for w in freqdi:
        if freqdi[w] >= x:
            freqEnough += [w]

    freqEnough.sort()
    return freqEnough


def getWordsByLengthDict(wtypes):
    """Takes a list of unique words (=word types) as the argument.
    Returns a dictionary where each key is word length, and the
    value is a list of words that are of that length.
    """
    # [6] Complete this function. YOUR CODE BELOW.

    lengthDict = {}
    for t in wtypes:
        if len(t) in lengthDict:
            lengthDict[len(t)] += [t]
        else:
            lengthDict[len(t)] = [t]

    return lengthDict


def getCharNGrams(txt, n):
    """Given a string and an n, returns a list of character n-grams."""
    nGrams = []
    for i in range(len(txt)+1-n):
        nGrams.append(txt[i:(i+n)])

    return nGrams


def getWordNGrams(wds, n):
    """Given a tokenized word list and n, returns a list of word-level
    n-grams. Each list member is a tuple.
    """
    nGrams = []
    for i in range(len(wds)+1-n):
        nGrams.append(tuple(wds[i:(i+n)]))

    return nGrams


def getFreq(li):
    """Takes a list as input, returns a dictionary of frequency count."""
    di = {}
    for x in li:
        if x not in di: di[x] = 1
        else: di[x] += 1

    return di
    

def main():
    """A void function that demonstrates how the functions are used."""
    taletoks = getTokens(tale)
    taletypes = getTypes(tale)
    talefreq = getTypeFreq(tale)

    print 'There are', len(taletoks), 'word tokens in tale.'
    print 'There are', len(taletypes), 'unique word types in tale.'
    print 'The word "it" occurs', talefreq['it'], 'times in the text.'
    
    print 'Words that are at least 10-characters long:',
    print ' '.join(getXLengthWords(taletypes, 10))
    print 'Words that occur at least 8 times:',
    print ' '.join(getXFreqWords(talefreq, 8))
    print 'Words that are exactly 7-characters long:',
    print ' '.join(getWordsByLengthDict(taletypes)[7])


if __name__ == '__main__':
    main()
