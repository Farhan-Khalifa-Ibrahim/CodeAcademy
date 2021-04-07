import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', -1)

jeapardy_data = pd.read_csv('jeopardy.csv')
#print(jeapardy_data.columns)

jeapardy_data = jeapardy_data.rename(columns = {' Air Date': 'Air_Date', ' Round': 'Round', ' Category': 'Category', ' Value': 'Value', ' Question': 'Question', ' Answer': 'Answer'})

#filter for specific words
def filter_data(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data[data['Question'].apply(filter)]

filtered = filter_data(jeapardy_data, ["king", "England's"])

print(filtered["Question"])
print()

#Remove a $ sign and adjust Float Value Column to a numeric datatype 
jeapardy_data['Float Value'] = jeapardy_data['Value'].replace('[None]', '0',regex=True).replace('[\$,]', '',regex=True)
jeapardy_data['Float Value'] =pd.to_numeric(jeapardy_data['Float Value'])

filtered = filter_data(jeapardy_data, ["King"])

print(filtered["Float Value"].mean())
print()
print(jeapardy_data.dtypes)
print()

#a function that returns the count of the unique answers
def get_answer_counts(data):
  return data['Answer'].value_counts()

print(get_answer_counts(filtered))