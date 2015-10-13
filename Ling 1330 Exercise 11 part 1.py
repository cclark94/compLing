# Christian Clark, cec81@pitt.edu, November 12 2014

import nltk, random

# Create list of tuples containing each name followed by its gender. Shuffle
# the list so that male and female names are mixed together.
names = [(name, 'male') for name in nltk.corpus.names.words('male.txt')] +\
	[(name, 'female') for name in nltk.corpus.names.words('female.txt')]
random.shuffle(names)

# Partition the names into a test set, a development set
# and a larger training set.
trainNames = names[1500:]
testNames = names[:750]
devtestNames = names[750:1500]

# Creature a function that returns a dictionary of features that might be
# good predictors of the gender of a given name.
def gender_features(name):
    return {'last_letter': name[-1],
            'first_letter': name[0],
            'last_two_letters': name[-2:]}

# Create list-like objects containing the features of each name followed by
# the name's gender (but not the name itself). 
trainSet = nltk.classify.apply_features(gender_features, trainNames)
testSet = nltk.classify.apply_features(gender_features, testNames)

# Train a Naive Bayes Classifier using the training data
classifier = nltk.NaiveBayesClassifier.train(trainSet)

# Find the accuracy of the classifier by trying it out with the test data
print 'Accuracy:', nltk.classify.accuracy(classifier, testSet)
print

# Create a list with a tuple showing each wrongly classified name from the
# development set. The tuple has the actual gender, the classifier's guess
# of the gender, and the name itself.
errors = []
for (name, gender) in devtestNames:
    guess =  classifier.classify(gender_features(name))
    if guess != gender:
        errors.append((gender, guess, name))

# Display all of the erors from the development set.
for (gender, guess, name) in errors:
    print 'Actual:', gender, '\tGuess:', guess, '\tName:', name
print

# Show the ten features that best predict whether a name is female or male.
classifier.show_most_informative_features()
