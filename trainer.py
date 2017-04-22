import nltk
import random
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

class trainClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        self.votes = []
        for self.i in self._classifiers:
            self.j = self.i.classify(features)
            self.votes.append(self.j)
        return mode(self.votes)

    def confidence(self, features):
        self.votes = []
        for self.i in self._classifiers:
            self.j = self.i.classify(features)
            self.votes.append(self.j)

        self.choice_votes = self.votes.count(mode(self.votes))
        self.conf = self.choice_votes / len(self.votes)
        return self.conf

    def featureFind(self,document,wf):
        self.words = word_tokenize(document)
        self.features = {}
        for self.i in wf:
            self.features[self.i] = (self.i in self.words)

        return self.features

    def train(self):
        self.pos = open("data/positive.txt", "r").read()
        self.neg = open("data/negative.txt", "r").read()
        self.words = []
        self.doc = []

        for p in self.pos.split('\n'):
            self.doc.append((p, "pos"))
            words = word_tokenize(p)
            pos = nltk.pos_tag(words)
            for w in pos:
                if w[1][0] in ["J"]:
                    self.words.append(w[0].lower())

        for p in self.neg.split('\n'):
            self.doc.append((p, "neg"))
            words = word_tokenize(p)
            pos = nltk.pos_tag(words)
            for w in pos:
                if w[1][0] in ["J"]:
                    self.words.append(w[0].lower())

        pickle.dump(self.doc, open("pickle/doc.pickle", "wb"))
        self.words = nltk.FreqDist(self.words)
        self.wordFeat = [i for (i, c)in self.words.most_common(5000)]
        pickle.dump(self.wordFeat, open("pickle/wordFeat.pickle", "wb"))
        self.featSet = [(trainClassifier().featureFind(self.rev,self.wordFeat), self.category) for (self.rev, self.category) in self.doc]
        random.shuffle(self.featSet)
        self.testSet = self.featSet[10000:]
        self.triainSet = self.featSet[:10000]
        pickle.dump(self.featSet,open("pickle/featSet.pickle", "wb"))
        ONB = nltk.NaiveBayesClassifier.train(self.triainSet)
        print("Original Naive Bayes Algo accuracy:",round((nltk.classify.accuracy(ONB, self.testSet)) * 100,2),"%")
        pickle.dump(ONB, open("pickle/ONB.pickle", "wb"))
        MNB = SklearnClassifier(MultinomialNB())
        MNB.train(self.triainSet)
        print("MultinomialNB accuracy:",round((nltk.classify.accuracy(MNB, self.testSet)) * 100,2),"%")
        pickle.dump(MNB, open("pickle/MNB.pickle", "wb"))
        BNB = SklearnClassifier(BernoulliNB())
        BNB.train(self.triainSet)
        print("BernoulliNB accuracy percent:",round((nltk.classify.accuracy(BNB, self.testSet)) * 100,2),"%")
        pickle.dump(BNB, open("pickle/BNB.pickle", "wb"))
        LR = SklearnClassifier(LogisticRegression())
        LR.train(self.triainSet)
        print("LogisticRegression accuracy:",round((nltk.classify.accuracy(LR, self.testSet)) * 100,2),"%")
        pickle.dump(LR, open("pickle/LR.pickle", "wb"))
        LSVC = SklearnClassifier(LinearSVC())
        LSVC.train(self.triainSet)
        print("LinearSVC accuracy:",round((nltk.classify.accuracy(LSVC, self.testSet)) * 100,2),"%")
        pickle.dump(LSVC, open("pickle/LSVC.pickle", "wb"))
        SGDC = SklearnClassifier(SGDClassifier())
        SGDC.train(self.triainSet)
        print("SGDClassifier accuracy:", round(nltk.classify.accuracy(SGDC, self.testSet) * 100,2),"%")
        pickle.dump(SGDC, open("pickle/SGDC.pickle", "wb"))
