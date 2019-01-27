from nltk.tag import StanfordPOSTagger
import os
java_path = "C:\Program Files (x86)\Common Files\Oracle\Java\javapath\java.exe"
os.environ['JAVAHOME'] = java_path
path2 = "stanford-ner.jar"
os.environ['CLASSPATH'] = path2
from nltk.tag import StanfordNERTagger

jar = 'D:\stanford-postagger-2018-10-16\stanford-postagger-2018-10-16/stanford-postagger.jar'
model = 'D:\stanford-postagger-2018-10-16\stanford-postagger-2018-10-16\models\english-left3words-distsim.tagger'
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
tagg = pos_tagger.tag('Barak Obama was the president of the united states of America')
print(tagg)

ner = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
ss = ner.tag('Rami Eid is studying at Stony Brook University in NY'.split())
print(ss)