# Christian Clark, cec81@pitt.edu, November 25 2014

import nltk, pickle

# PART A
# (1) Build tree objects
np = nltk.Tree('(NP (N Marge))')
aux = nltk.Tree('(AUX will)')
vp = nltk.Tree('(VP (V make) (NP (DET a) (N ham) (N sandwich)))')

# (2) Build tree objects for sentences made from combinations of the
# trees in (1)
s1 = nltk.Tree('S', [np, aux, vp])
s2 = nltk.Tree('S', [aux, np, vp])

# (3), (4) Build tree objects for s3, s4, s5
s3_str = '''
(S (NP (N Homer))
   (VP (V ate)
       (NP (NP (DET the)
               (N donut))
           (PP (P on)
               (NP (DET the)
                   (N table))))))
'''
s3 = nltk.Tree(s3_str)

s4_str = '''
(S (NP (DET my)
       (ADJ old)
       (N cat))
   (VP (VP (V died))
       (PP (P on)
           (NP (N Tuesday)))))
'''
s4 = nltk.Tree(s4_str)

s5_str = '''
(S (NP (N children))
   (AUX must)
   (VP (VP (V play))
       (PP (P in)
           (NP (DET the)
               (N park)))
       (PP (P with)
           (NP (DET their)
               (N friends)))))
'''
s5 = nltk.Tree(s5_str)

# (5) Extract list of production rules and examine them
s5_rules = s5.productions()

print 'PART A'
print '5a.\t', len(s5_rules), 'context-free rules are used in s5.'
print '5b.\t', len(set(s5_rules)), 'unique context-free rules are used in s5.'
print '5c.\t', len([r for r in s5_rules if r.is_lexical()]), 'lexical rules',\
      'are used in s5.'
print ''

# PART B
# (1) List all of the CF rules appearing in s6 through s11, and build a grammar
# from them
rules = '''
S -> NP VP | NP AUX VP
NP -> DET ADJ N | DET ADJ ADJ N | N | PRO | DET N | NP CP | NP CONJ NP | NP PP
NP -> N N
VP -> VP PP | V NP | V NP PP | V NP NP | V ADJP | VP CONJ VP | V | V NP CP
VP -> VP ADVP
PP -> P NP
CP -> COMP S
ADJP -> ADJP CONJ ADJP | ADJ | ADV ADJ
ADVP -> ADV ADV
DET -> 'the' | 'his' | 'her'
ADJ -> 'big' | 'tiny' | 'nerdy'
N -> 'bully' | 'kid' | 'school' | 'book' | 'sister' | 't' | 'Homer' | 'Marge'
N -> 'friends' | 'work' | 'bar' | 'Lisa' | 'brother' | 'peanut' | 'butter'
V -> 'punched' | 'gave' | 'given' | 'are' | 'drank' | 'sang' | 'told' | 'liked'
P -> 'after' | 'to' | 'from' | 'in'
PRO -> 'he' | 'I' | 'him' | 'she'
COMP -> 'that'
AUX -> 'had'
CONJ -> 'and' | 'but'
ADJ -> 'poor' | 'happy'
ADV -> 'very' | 'much'
'''

grammar1 = nltk.parse_cfg(rules)

# (2) Explore the rules extracted from grammar1
g1_rules = grammar1.productions()

print 'PART B'
print '2a.\t', grammar1.start(), 'is the start state of grammar1.'
print '2b.\tThere are', len(g1_rules), 'context-free rules in grammar1.'
print '2c.\tThere are', len([r for r in g1_rules if r.is_lexical()]),\
      'lexical rules in grammar1.'
print '2d.\tThere are',\
      len(grammar1.productions(lhs=nltk.grammar.Nonterminal('VP'))),\
      'VP rules in grammar1.'
print '2e.\tThere are',\
      len(grammar1.productions(lhs=nltk.grammar.Nonterminal('V'))),\
      'V rules in grammar1.'
print ''

s6 = 'the big bully punched the tiny nerdy kid after school'
s7 = 'he gave the book to his sister'
s8 = 'he gave the book that I had given him t to his sister'
s9 = 'Homer and Marge are poor but very happy'
s10 = 'Homer and his friends from work drank and sang in the bar'
s11 = 'Lisa told her brother that she liked peanut butter very much'

# (3), (4) Build a chart parser from grammar1 and parse s6 through s11
chartParser = nltk.ChartParser(grammar1)
print '4.\tSentences 6-11 parsed by chart parser:'
for s in [s6,s7,s8,s9,s10,s11]:
    print chartParser.parse(s.split())
    print ''

# PART C
# (1) Examine s10, which is ambiguous
print 'PART C'
print '1.\tThese are all the possible parses of s10:'
for p in chartParser.nbest_parse(s10.split()):
    print p
    print ''
print 'There are four different possible parses for s10. The phrases',\
      '\'from work\' and \'in the bar\' can be interpreted multiple ways:',\
      'maybe Homer and his friends are all from work, or maybe just Homer\'s',\
      'friends are from work; and maybe they both drank and sang in the bar,',\
      'or maybe they only sang in the bar. Because there are two different',\
      'possibilities in both cases, there are 2*2=4 possible parses.'
print ''

# (2) Parse s12
s12 = 'Lisa and her friends told Marge that Homer punched the bully in the bar'
print '2.\tSentence 12 parsed by chart parser:'
print chartParser.parse(s12.split())
print ''

# (3) Try out the parser on an original sentence
my_sent = 'her nerdy brother told his friends '+\
              'that she drank peanut butter after work'

print '3.\tThis is my original sentence:'
print my_sent
print ''
print 'Parsed by the chart parser:'
print chartParser.parse(my_sent.split())
print ''
print 'This parse is right about many parts but has some errors too. It\'s',\
      'not too surprising, since my sentence is relatively long, which',\
      'tends to introduce more amibiguity. In fact, I counted 22 different',\
      'parses when I triend chartParser.nbest_parse!'
print ''

# (4)(a),(b) I typed up a list of all of the rules appeaing in s1, s2, and s3,
# and then narrowed it down to the ones that hadn't already been included
# in grammar1.
more_rules_str = '''
S -> AUX NP VP
NP -> DET N N
N -> 'ham' | 'sandwich' | 'donut' | 'table' 
AUX -> 'will'
V -> 'make' | 'ate'
DET -> 'a'
P -> 'on'
'''

more_rules = nltk.parse_cfg(more_rules_str)

# (4)(c) Add rules to grammar1
grammar1.productions().extend(more_rules.productions())
grammar1 = nltk.grammar.ContextFreeGrammar(grammar1.start(),\
                                           grammar1.productions())

# (4)(d) Rebuild chart parser and try it on s1, s2 and s3
chartParser = nltk.ChartParser(grammar1)

s1_sent = 'Marge will make a ham sandwich'
s2_sent = 'will Marge make a ham sandwich'
s3_sent = 'Homer ate the donut on the table'

print '4d.\tSentences 1 through 3 parsed by the chart parser:'
for s in [s1_sent,s2_sent,s3_sent]:
    print chartParser.parse(s.split())
    print ''

# (5) Try the updated parser on an original sentence
my_sent2 = 'will her poor friends make him a big sandwich'
print '5.\tHere\'s another sentence I came up with:'
print my_sent2
print ''
print 'And its parse:'
print chartParser.parse(my_sent2.split())
print ''
print 'Looks like the parser was completely correct this time.'

# (6) Pickle grammar1
outfile = open('hw10_grammar.pkl','wb')
pickle.dump(grammar1, outfile, -1)
outfile.close()
