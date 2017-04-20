import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize



class sent(ClassifierI):
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
    def ment(text):

        doc = pickle.load(open("pickle/documents.pickle", "rb"))
        wordFeat = pickle.load(open("pickle/word_features5k.pickle", "rb"))
        featSet = pickle.load(open("pickle/featuresets.pickle", "rb"))
        classifier = pickle.load(open("pickle/originalnaivebayes5k.pickle", "rb"))
        MNB_classifier = pickle.load(open("pickle/MNB_classifier5k.pickle", "rb"))
        BernoulliNB_classifier = pickle.load(open("pickle/BernoulliNB_classifier5k.pickle", "rb"))
        LogisticRegression_classifier = pickle.load(open("pickle/LogisticRegression_classifier5k.pickle", "rb"))
        LinearSVC_classifier = pickle.load(open("pickle/LinearSVC_classifier5k.pickle", "rb"))
        SGDC_classifier = pickle.load(open("pickle/SGDC_classifier5k.pickle", "rb"))

        voted_classifier = sent(classifier,LinearSVC_classifier,MNB_classifier,BernoulliNB_classifier,LogisticRegression_classifier)
        feats = sent().featureFind(text,wordFeat)
        out = (voted_classifier.confidence(feats))*100
        # out = str(out)+"%"
        return voted_classifier.classify(feats),out