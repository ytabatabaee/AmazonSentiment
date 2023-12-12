import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def clean_text(raw_text):
    """Takes a raw text as input and preprocess it
            Parameters
            ----------
            raw_text : str
                A string containing raw text
            Returns
            -------
            str
                cleaned text after removing punctuations, stopwords and stemming
            """
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
    """Converts a rating to a categorical sentiment
        Parameters
        ----------
        x : int
            The rating of a review, an integer between 1 to 5
        Returns
        -------
        str
            the sentiment of a review that falls into one of three categories: "good", "average", "bad
        """
    if x == 5.0 or x == 4.0:
        return "Good"
    elif x == 3.0:
        return "Average"
    return "Bad"
