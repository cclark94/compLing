# Christian Clark, cec81@pitt.edu, November 11 2013

import cPickle, nltk
from urllib import urlopen

inFile = open('trigram_tagger.pkl','rb')
t3 = cPickle.load(inFile)
inFile.close()

url = 'https://www.fanfiction.net/s/2636963/1/Harry-Potter-and-the-Nightmares-of-Futures-Past'
html = urlopen(url).read()
txt = nltk.clean_html(html)

punkt = nltk.PunktSentenceTokenizer()
sents = punkt.tokenize(txt)

tok_sents = []
for s in sents:
    tok_sents.append(nltk.word_tokenize(s))

tagged_sents = []
for s in tok_sents:
    tagged_sents.append(t3.tag(s))

outFile = open('Ling 1330 Homework 8 part 3 file.txt', 'w')
for t in tagged_sents:
    for w in t:
        outFile.write(w[0]+' '+w[1]+'\n')
    outFile.write('='*16 + '\n')

outFile.close()
