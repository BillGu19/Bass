# -*- coding: utf-8 -*-
"""GPT2imdb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_484wco-2YnrTKVJr5wN4qW4RDQIuKZD
"""

import pandas as pd
import finetune

url = 'https://raw.githubusercontent.com/BillGu19/Bass/master/name_genre_identifiers.csv'
name_genre = pd.read_csv(url)
name = name_genre['primaryName']
genre = name_genre['top genre']
#print(name)
#print(genre)
#print(name_genre)

from finetune.base_models import BERT, BERTLarge, GPT2, GPT2Medium, GPT2Large, TextCNN, TCN, RoBERTa, DistilBERT
from finetune import Classifier
from finetune import LanguageModel

#X = ['german shepherd', 'maine coon', 'persian', 'beagle']
#Y = ['dog', 'cat', 'cat', 'dog']
model = Classifier(base_model=GPT2)
model.fit(name, genre)

testX = ['Tom Cruise','Jamie Lee Curtis', 'Claire Danes', 'Geena Davis', 'Robert De Niro', 'John Denver', 'Johnny Depp', 'Leonardo DiCaprio', 'Clint Eastwood']
predictions= model.predict(testX)
print(predictions)