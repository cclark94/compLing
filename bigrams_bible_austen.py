# Christian Clark, cec81@pitt.edu, 29 September 2014

import pickle, textstats as ts

outFile = open('bigram_bible_austen_out.txt', 'w')


# Part 1: The King James Bible
# (A) and (B) Create token and type lists from the text file

bInfile = open('../Ling 1330/gutenberg/gutenberg/bible-kjv.txt')
bTxt = bInfile.read()
bInfile.close()

bToks = ts.getTokens(bTxt)
bTypes = ts.getTypes(bTxt)


# (C) Write out token and type counts to outFile

outFile.write('There are a total of '+str(len(bToks))+' word tokens and '+\
              str(len(bTypes))+' word types in the King James Bible.'+'\n\n')


# (D) Create bigram frequency dictionary

bBigrFreq = {}
for bigr in ts.getWordNGrams(bToks, 2):
    if bigr in bBigrFreq: bBigrFreq[bigr] += 1
    else: bBigrFreq[bigr] = 1


# (E) Write out the top bigrams and their counts

n1 = 20
outFile.write('Top '+str(n1)+' word bigrams in the Bible:\n')
for bigr in sorted(bBigrFreq, key=bBigrFreq.get, reverse=True)[:n1]:
    outFile.write(bigr[0]+' '+bigr[1]+'\t\t'+str(bBigrFreq[bigr])+'\n')
outFile.write('\n')


# (F) Create 'so-initial' bigram frequency dictionary

bSoFreq = {}
for bigr in bBigrFreq.keys():
    if bigr[0] == 'so': bSoFreq[bigr] = bBigrFreq[bigr]


# (G) Write out the top 'so-initial' bigrams and their counts

n2 = 20
outFile.write('Top '+str(n2)+' \'so\'-initial bigrams in the Bible:\n')
for bigr in sorted(bSoFreq, key=bSoFreq.get, reverse=True)[:n2]:
    outFile.write(bigr[0]+' '+bigr[1]+'\t\t'+str(bSoFreq[bigr])+'\n')
outFile.write('\n')


# (H) Write out the frequency count of 'so'

outFile.write('There are '+str(sum(bSoFreq.values()))+\
              ' appearances of the word \'so\' in the Bible.\n')
outFile.write(16*'_'+'\n\n')


# (I) Pickle the bigram frequency dictionary

bDictOut = open('bible_bigram_frequency.p', 'wb')
pickle.dump(bBigrFreq, bDictOut, -1)
bDictOut.close()


# (J) Part 2: Jane Austen
# (A) and (B) Create token and type lists from the text file

aInfile1 = open('../Ling 1330/gutenberg/gutenberg/austen-emma.txt')
aInfile2 = open('../Ling 1330/gutenberg/gutenberg/austen-persuasion.txt')
aInfile3 = open('../Ling 1330/gutenberg/gutenberg/austen-sense.txt')
aTxt1 = aInfile1.read()
aTxt2 = aInfile2.read()
aTxt3 = aInfile3.read()
aInfile1.close()
aInfile2.close()
aInfile3.close()

aToks = ts.getTokens(aTxt1) + ts.getTokens(aTxt2) + ts.getTokens(aTxt3)
aTypes = sorted(list(set(ts.getTypes(aTxt1) + ts.getTypes(aTxt2) + \
                         ts.getTypes(aTxt3))))


# (C) Write out token and type counts to outFile

outFile.write('There are a total of '+str(len(aToks))+' word tokens and '+\
              str(len(aTypes))+' word types in the Jane Austen corpus.'+'\n\n')


# (D) Create bigram frequency dictionary
# I use the nested for loops in order to avoid including the couple of extra
# bigrams that would appear if I just looped through aToks (the last word of
# aTxt1 plus the first word of aTxt2, the last word of aTxt2 plus the first word
# of aTxt3).

aBigrFreq = {}
for txt in [aTxt1, aTxt2, aTxt3]:
    for bigr in ts.getWordNGrams(ts.getTokens(txt), 2):
        if bigr in aBigrFreq: aBigrFreq[bigr] += 1
        else: aBigrFreq[bigr] = 1


# (E) Write out the top bigrams and their counts

n3 = 20
outFile.write('Top '+str(n3)+' word bigrams in the Austen corpus:\n')
for bigr in sorted(aBigrFreq, key=aBigrFreq.get, reverse=True)[:n3]:
    outFile.write(bigr[0]+' '+bigr[1]+'\t\t'+str(aBigrFreq[bigr])+'\n')
outFile.write('\n')


# (F) Create 'so-initial' bigram frequency dictionary

aSoFreq = {}
for bigr in aBigrFreq.keys():
    if bigr[0] == 'so': aSoFreq[bigr] = aBigrFreq[bigr]


# (G) Write out the top 'so-initial' bigrams and their counts

n4 = 20
outFile.write('Top '+str(n4)+' \'so\'-initial bigrams in the Austen corpus:\n')
for bigr in sorted(aSoFreq, key=aSoFreq.get, reverse=True)[:n4]:
    outFile.write(bigr[0]+' '+bigr[1]+'\t\t'+str(aSoFreq[bigr])+'\n')
outFile.write('\n')


# (H) Write out the frequency count of 'so'

outFile.write('There are '+str(sum(aSoFreq.values()))+\
              ' appearances of the word \'so\' in the Austen corpus.\n\n')


# (I) Pickle the bigram frequency dictionary

bDictOut = open('austen_bigram_frequency.p', 'wb')
pickle.dump(aBigrFreq, bDictOut, -1)
bDictOut.close()


outFile.close()
