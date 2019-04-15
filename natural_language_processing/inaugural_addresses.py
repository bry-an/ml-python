from nltk.corpus import PlaintextCorpusReader
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
sr = stopwords.words('english')
corpus_root = 'E:/Code/machine-learning/machine-learning-python/natural_language_processing/inaugurals'
wordlist = PlaintextCorpusReader(corpus_root, ".*")
print(wordlist.fileids())

trump_words = wordlist.words('trump2017.txt')
obama_words = wordlist.words('obama2009.txt')
# remove punctuation
trump_words = [word for word in trump_words if len(word) > 1]
obama_words = [word for word in obama_words if len(word) > 1]
# remove applause
obama_words = [word for word in obama_words if word != 'Applause'] 
obama_words = [word for word in obama_words if word != '.)'] 
freq_trump = nltk.FreqDist(w for w in trump_words if not w in sr)
freq_obama = nltk.FreqDist(w for w in obama_words if not w in sr)
            
# for key,val in freq_obama:
#     print(str(key) + ':' + str(val))

# freq_trump.plot(20, cumulative=False)
freq_obama.plot(20, cumulative=False)