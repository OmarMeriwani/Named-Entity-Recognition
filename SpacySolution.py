import spacy
from spacy import displacy
from collections import Counter
#import en_core_web_sm
#nlp = spacy.load('C:/Users/Omar/Downloads/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0')
nlp = spacy.load('D:\en_core_web_lg-2.0.0\en_core_web_lg-2.0.0\en_core_web_lg\en_core_web_lg-2.0.0')
from pprint import pprint

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc.ents])
