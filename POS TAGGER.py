import nltk
from nltk import word_tokenize, pos_tag

# From command prompt
# type python
# >>> import nltk
# >>> nltk.download()
# >>> install corpora & book

source = "source.txt"
fname = open("source","r")
content = fname.read()

sentences = nltk.sent_tokenize(content)

data = []
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))
print(data)