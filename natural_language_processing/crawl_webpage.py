import nltk
nltk.download('stopwords')
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
sr = stopwords.words('english')


response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
html = response.read()
soup = BeautifulSoup(html)
text = soup.get_text(strip = True)
# convert text into tokens
tokens = [t for t in text.split()]
clean_tokens = tokens[:]
for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)