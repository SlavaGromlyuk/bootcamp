import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

''' 
Similarity between cat and monkey is highest (0.5929) because they are both animals.
Similarity between banana and monkey is 0.4042 and is higher then similarity between 
banana and cat (0.2236) because the model recognises that monkeys eat banana, but not cats.  
'''

word1 = nlp("Sun")
word2 = nlp("rocket")
word3 = nlp("Moon")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

''' 
Similarity between Sun and rocket is lowest (0.0357)
because on is an astral object and another is man-made type of transport.
Similarity between moon and rocket (0.2199) is higher because the model
recognises that rockets are used to travel to the Moon.  
Similarity between Moon and Sun is highest (0.6069) because both are 
recognised as astral objects. 
'''

nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

''' 
If using Simple Model for finding similarities between words, the User Warning comes up 
to say that this model does not have word vectors loaded, so results will be based on the 
tagger, parser and NER.
Similarity between cat and monkey (0.6771) is higher than using Medium Model. 
Similarity between banana and monkey (0.7276) is higher than using Medium Model.
Similarity between banana and cat (0.6807)is higher than using Medium Model.  
The results suggest that using the Medium Model gives more accurate results.
'''