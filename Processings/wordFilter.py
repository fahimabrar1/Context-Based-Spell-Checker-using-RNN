import pandas as pd
from bltk.langtools import Tokenizer
from bltk.langtools.banglachars import (digits,operators,punctuations,others)
from numba import jit
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
import re

df = pd.read_csv(r'D:\Python\Context Based Spell Checker using RNN\Processings\Processed\BengaliSentiment_WordCorpus.csv')
ls = []

print("1st ",df['wordList'].shape)
for i,element in enumerate(df['wordList']):
    if len(element)<=1:
        ls.append(i)
ls.reverse()
if len(ls)>0:
    for element in ls:
        df['wordList'].pop(element)

print("2nd ",df['wordList'].shape)

ls = []
for i,elem in enumerate(df['wordList']):
    print(i)
    count = 0
    for j, elem1 in enumerate(df['wordList']):
        if elem == elem1 and count < 10:
            count += 1
        elif count >= 10:
            ls.append(elem)
            break
    # if count < 10:
    #     ls.append(i)
df['wordList'] = ls
print(df['wordList'])
# ls.reverse()
# print("Cleaning")
# print(ls)
# if len(ls)>0:
#     for element in ls:
#         df['wordList'].pop(element)

print("3rd ",df['wordList'].shape)
df.to_csv('unique_words_BengaliSentiment.csv', index=False)
