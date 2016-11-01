# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
import nltk
nltk.download('punkt')
nltk.download()
from nltk import word_tokenize,sent_tokenize
from nltk.book import *

list_of_150 = text2[:150]
string_first_150 = ' '.join(list_of_150)
# print (string_first_150)

tokens = nltk.word_tokenize(string_first_150)
print("TOKENS")
print(tokens)

tagged_tokens = nltk.pos_tag(tokens)
print("TAGGED TOKENS")
print(tagged_tokens)



print("\n\nEND*******")
