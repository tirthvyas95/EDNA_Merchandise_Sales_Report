import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


import nltk


df = pd.read_excel('C:/Users/tirth/Documents/Projects/EDNA Merchandise Sales Report/Source Files/Onyx Data -DataDNA Dataset Challenge - Merchandise Sales Dataset - January 2025.xlsx')

dfsub = df[['Order ID']]

#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('averaged_perceptron_tagger_eng')
#nltk.download('maxent_ne_chunker_tab')
#nltk.download('words')


from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

sia = SentimentIntensityAnalyzer()


#nltk.download('vader_lexicon')

res = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row['Review']
    myid = row['Order ID']
    res[myid] = sia.polarity_scores(text)


vaders = pd.DataFrame(res).T
vaders.reset_index(inplace=True)
vaders.rename(columns={'index': 'Order ID'}, inplace=True)

sentiment_scores = vaders.merge(dfsub, how='left', on='Order ID')
