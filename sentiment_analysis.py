# Step 1 - Data preparation and initial cleaning
import pandas as pd

# Loading the dataset
reviews_data = pd.read_csv('amazon_product_reviews.csv', low_memory=False)

# Selecting relevant columns and removing missing values
reviews_data = reviews_data[['reviews.text']].dropna()
reviews_data = reviews_data.sample(100)

# Step 2 - NLP processing 
import spacy
nlp = spacy.load('en_core_web_sm')

# Function to convert text to lower case, remove stop words and punctuation
def preprocess(text):
    doc = nlp(text)
    return ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

# Function to convert preprocessed text to a SpaCy doc
def get_doc(text):
    return nlp(text)

# Apply pre-processing
reviews_data['processed_reviews'] = reviews_data['reviews.text'].apply(preprocess)
reviews_data['doc'] = reviews_data['processed_reviews'].apply(get_doc)

#Step 3 - Sentiment analysis
from textblob import TextBlob

# Function to analyze sentiment with TextBlob
def analyse_polarity(text):
   
    blob = TextBlob(text)
    polarity_score = blob.sentiment.polarity

    if 0.5 > polarity_score > 0:
        sentiment = 'positive'
    elif polarity_score > 0.5:
        sentiment = 'very positive'
    elif -0.5 < polarity_score < 0:
        sentiment = 'negative'
    elif polarity_score < -0.5:
        sentiment = 'very negative'
    else:
        sentiment = 'neutral'
    return sentiment

# Apply function to analyse the sentiment of individual product reviews 
reviews_data['sentiment'] = reviews_data['processed_reviews'].apply(analyse_polarity)

print(reviews_data.head())