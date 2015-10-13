# Christian ...

import pickle, textstats as ts

outFile = open('2009-Obama_out.txt', 'w')


# Part 1: The King James Bible
# (A) and (B) Create token and type lists from the text file

bInfile = open('2009-Obama.txt')
bTxt = bInfile.read()
bInfile.close()

bToks = ts.getTokens(bTxt)
bTypes = ts.getTypes(bTxt)


# (C) Write out token and type counts to outFile

outFile.write('There are a total of '+str(len(bToks))+' word tokens and '+\
              str(len(bTypes))+' word types in Obama\'s speech.'+'\n\n')


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

bDictOut = open('Obama_bigram_frequency.p', 'wb')
pickle.dump(bBigrFreq, bDictOut, -1)
bDictOut.close()


outFile.close()
