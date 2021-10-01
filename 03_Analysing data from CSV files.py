from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import Counter

plt.style.use('fivethirtyeight')

data=pd.read_csv('data.csv')
ids=data['Responder_id']
lang=data['LanguagesWorkedWith']
language_counter = Counter()

for response in lang:
    language_counter.update(response['LanguagesWorkedWith'].split(';'))

# with open ('data.csv') as csv_file:
#     csv_reader=csv.DictReader(csv_file)



    # row=next(csv_reader)
    # print(row['LanguagesWorkedWith'].split(';'))         #create a list of values in 'LanguagesWorkedWith' column

    # language_counter= Counter()

    # for row in csv_reader:
    #     language_counter.update(row['LanguagesWorkedWith'].split(':'))    #use of counter library attached in this folder as a .jpg file, kindly refer

print(language_counter.most_common(10))      #print 10 most commom languages from 'LanguagesWorkedWith' column.

