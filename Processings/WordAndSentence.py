# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:08:26 2021

@author: fahim
"""
import pandas as pd
from bltk.langtools import Tokenizer
from bltk.langtools.banglachars import (digits,operators,punctuations,others)
from numba import jit
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
import re

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

# function optimized to run on gpu
#@jit(forceobj=True)
def extract_sentence(df , tokenizer , SentenceHolder):
       print("TOKENIZED SENTENCES")
       ina = 1
       for para in df:
              print(ina)
              ina += 1
              sentences = tokenizer.sentence_tokenizer(para)
              for i,sen in enumerate(sentences):
                     sen = "".join(i for i in sen if i in ["।"] or 2432 <= ord(i) <= 2559 or ord(i) == 32)
                     sen = " ".join(sen.split())
                     sen = sen[:-1]
                     sen = sen.strip()
                     if len(sen)>1:
                            SentenceHolder.loc[len(SentenceHolder.index)] = [sen]


       print(SentenceHolder)
       SentenceHolder.to_csv('full_doc_test_SentenceCorpus.csv', index=False)



# function optimized to run on gpu
#@jit
def extract_words(df,wordHolder):
       _contentHolderLength = wordHolder.shape[0]
       ina = 1
       for content in df:
              ina+=1
              print(ina)
              if pd.isna(content) == False:
                     #print("Contnet :" , content)
                     words = tokenizer.word_tokenizer(content)
                     print(words)
                     holder =[]
                     for i,e in enumerate(words):
                            for j in e:
                                   if( 2544 > ord(j) > 2533 ):
                                          print("J: ",j,"    i: ",i)
                                          holder.append(i)
                                          break
                     holder.reverse()
                     if len(holder) > 0:
                           for i in holder:
                                  words.pop(i)
                     #print("Words: ",words)
                     for i in words:
                            i = i.strip()
                            wordHolder.loc[len(wordHolder.index)] = i
       wordHolder.to_csv('BengaliSentiment_WordCorpus.csv' , index=False)




if __name__=="__main__":

       print(f'Digits: {digits}')
       print(f'Operators: {operators}')
       print(f'Punctuation marks: {punctuations}')
       print(f'Others: {others}')

       print()
       print()
       print()

       # Just type the path of the csv file
       #df = pd.read_csv (r'D:\Python\Context Based Spell Checker using RNN\Data Extracted\dhakatribunebangla_1.csv')
       df = pd.read_csv (r'D:\Python\Context Based Spell Checker using RNN\Processings\Data\full_doc_test.csv')

       wordHolder = pd.DataFrame()
       wordHolder['wordList'] = []
       SentenceHolder = pd.DataFrame()
       SentenceHolder['SentenceList'] = []
       # SentenceHolder = []

       tokenizer = Tokenizer()
       # Tokenizing words
       print('TOKENIZED WORDS')

       print(df['text'])
       #extract_words(df['data'])

       #extract_sentence(df['text'] , tokenizer , SentenceHolder)


       word_df = pd.read_csv (r'/Processed/BengaliSentiment_SentenceCorpus.csv')
       extract_words(word_df['SentenceList'],wordHolder)
       print(wordHolder)
       #
       # print("End")