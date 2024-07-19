import numpy as np
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')

# Add SpacyTextBlob to the pipeline
nlp.add_pipe('spacytextblob')
print(nlp.pipe_names)

# Text Preprocessing
def preprocess_text(text):
    # Create a spaCy document
    doc = nlp(text)
    
    # Remove stopwords and punctuation
    filtered_tokens = [token for token in doc if not token.is_stop and not token.is_punct]
    
    # Lemmatize the tokens
    lemmatized_tokens = [token.lemma_ for token in filtered_tokens]
    
    # Join the lemmatized tokens back into a string
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text

# Sentiment Analysis
def analyze_sentiment(text):
    # Create a spaCy document
    doc = nlp(text)
    
    # Get the sentiment polarity and subjectivity
    polarity = doc._.blob.polarity
    subjectivity = doc._.blob.subjectivity
    
    # Determine the sentiment label
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, polarity, subjectivity


# Load in the dataset
df = pd.read_csv('amazon_product_review.csv')

clean_data = df.dropna(subset=['reviews.text'])

# # Preprocess the text column
clean_data['preprocessed_text'] = clean_data['reviews.text'].apply(preprocess_text)

# # # Analyze the sentiment of the preprocessed text
clean_data['sentiment'], clean_data['polarity'], clean_data['subjectivity'] = zip(*clean_data['preprocessed_text'].apply(analyze_sentiment))

clean_data.iloc[4, :]
print('Original text: ------------------------>\n', clean_data.iloc[4]['reviews.text'])
print('Preprocessed: ------------------------->\n', clean_data.iloc[4]['preprocessed_text'])

clean_data.iloc[4,-4:]
clean_data.columns
# Show text of top 5 most negative reviews along with their polarity and preprocessed text
for index, row in clean_data.sort_values('polarity').head().iterrows():
    print(f"Review: {row['reviews.text']}")
    print(f"Preprocessed Text: {row['preprocessed_text']}")
    print(f"Polarity: {row['polarity']}")
    print()
    
    # Show the top 5 most positive reviews along with their polarity and preprocessed text
for index, row in clean_data.sort_values('polarity', ascending=False).head().iterrows():
    print(f"Review: {row['reviews.text']}")
    print(f"Preprocessed Text: {row['preprocessed_text']}")
    print(f"Polarity: {row['polarity']}")
    print()
    
# compare results of sentiment
sentiment_counts = clean_data['sentiment'].value_counts()
sentiment_counts

# From the above we can see that there is a majority positive sentiment on the amazon products 
# in comparison to the Neutral and negative sentinments.
# So therefore an overall positive status on the product reviews at amazon based on our data