import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def clean_text(raw_text):
    prepared_text = raw_text.lower()
    # 1. Remove Punctuation marks
    prepared_text = prepared_text.translate(prepared_text.maketrans("", "", string.punctuation))
    # 2. Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = prepared_text.split()
    tokens = [word for word in tokens if word not in stop_words]
    # 3. Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(tokens)


def rating_to_sentiment(x):
    if x == 5.0 or x == 4.0:
        return "Good"
    elif x == 3.0:
        return "Average"
    return "Bad"
