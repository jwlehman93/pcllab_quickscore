import nltk
from nltk.corpus import stopwords
import gensim
from gensim.models import KeyedVectors
import os, re
#import spellChecker 

class quickscore:
	
	# Inititalize the instance of the class
	def __init__(self,modelFile):
		self.model = KeyedVectors.load_word2vec_format(modelFile, binary=True)
		self.model.init_sims(replace=True)
		self.STOPLIST = stopwords.words('english')	
	
	def w2vScore(self, response, target):
		keywords = re.findall('[a-z_]+', target.lower())  #converts all words to lower case
		responses = re.findall('[a-z_]+', response.lower()) 
		keywords = [i for i in  keywords if i not in self.STOPLIST] #Filters out the words that are in the stoplist
		responses = [i for i in  responses if i not in self.STOPLIST] 
		if len(keywords) == 0 : #checks for the length of the keywords
			return 0;
		keywordsPrepared = []
		responsesPrepared = []
		for i in keywords:
			if i in self.model.vocab:
				keywordsPrepared.append(i) #only adds the words that are in the models vocabulary, ignores all the other words
		for i in responses:
			if i in self.model.vocab:
				responsesPrepared.append(i) #only adds the words that are in the models vocabulary, ignores all the other words	
		if len(keywordsPrepared) == 0 or len(responsesPrepared) == 0 :
			return 0;
		result = self.model.n_similarity(responsesPrepared, keywordsPrepared) #Gets the score, Value b/w 0 and 1
    		return result    
