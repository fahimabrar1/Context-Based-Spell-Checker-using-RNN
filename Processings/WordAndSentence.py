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

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

# function optimized to run on gpu
@jit
def extract_sentence(df , tokenizer , SentenceHolder):
       _contentHolderLength = SentenceHolder.shape[0]
       for content in df:
              if pd.isna(content) == False:
                     print("Contnet :", content)
                     sentence = tokenizer.word_tokenizer(content)
                     print(sentence)




# function optimized to run on gpu
@jit
def extract_words(df):
       _contentHolderLength = wordHolder.shape[0]
       for content in df:
              if pd.isna(content) == False:
                     print("Contnet :" , content)
                     sentence = tokenizer.word_tokenizer(content)
                     print(sentence)
                     nwordsindex = []
                     for i, word in enumerate(sentence):
                            nowBreak = False
                            for char in word:
                                   if(char == others[5] or char == others[6]):
                                          nwordsindex.append(i)
                                          nowBreak = True
                                          break

                            if nowBreak == False:
                                   for char in word:
                                          for d in digits:
                                                 if (char == d):
                                                        nwordsindex.append(i)
                                                        nowBreak = True
                                                        break
                                          if nowBreak == True:
                                                 break

                            if nowBreak == False:

                                   for char in word:
                                          for p in punctuations:
                                                 if (char == p):
                                                        nwordsindex.append(i)
                                                        nowBreak = True
                                                        break
                                          if nowBreak == True:
                                                 break


                     nwordsindex.reverse()

                     print("nwordsindex: ",nwordsindex)

                     if len(nwordsindex) > 0:
                            for i in nwordsindex:
                                   sentence.pop(i)
                     print("WORDS :       ", sentence)

                     for _word in sentence:
                            #print(wordHolder)
                            #print(wordHolder.shape[0])
                            wordHolder.loc[_contentHolderLength]=_word
                            _contentHolderLength += 1




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
       df = pd.read_csv (r'D:\Python\Context Based Spell Checker using RNN\Test Sheets\Test By Fahim.csv')


       wordHolder = pd.DataFrame()
       wordHolder['wordList'] = []
       SentenceHolder = pd.DataFrame()
       SentenceHolder['SentenceList'] = []

       tokenizer = Tokenizer()
       # Tokenizing words
       print('TOKENIZED WORDS')

       print(df['content'])
       # extract_words(df['content'])
       extract_sentence(df['content'] , tokenizer , SentenceHolder)

       print(wordHolder)

       print("End")