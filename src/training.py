import pandas as pd
from src.preprocessing import clean_text
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer,TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import ComplementNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, chi2


def predict(clf, review, clean=False):
    """Takes a classifier and a review as input and predicts its sentiment
                Parameters
                ----------
                clf : classifier object
                    Sentiment analysis classifier
                review: str
                    Review text object
                clean: bool
                    clean the text before predicting its review if True
                Returns
                -------
                rating: int
                    an integer between 1 to 5 which shows the predicted sentiment of the review
                prob_rating: list
                    a probability distribution over the 5 ratings
                """
    if clean:
        review = clean_text(review)
    prediction_df = pd.DataFrame([[review, 0]], columns=["reviewText", "y"])
    rating = clf.predict(prediction_df["reviewText"])[0]
    try: # if the classifier can predict probabilities
        prob_rating = clf.predict_proba(prediction_df["reviewText"])[0]
    except:
        prob_rating = None
    return rating, prob_rating


def create_classifier(vector_representation, feature_selection, classifier):
    """Takes elements of a classifier as input and creates a pipeline containing them
                    Parameters
                    ----------
                    vector_representation : sklearn.feature_extraction.text object
                        Count vectorizer or TF-IDF vectorizer
                    feature_selection:
                        sklearn.feature_selection object
                    classifier:
                        classifier object
                    Returns
                    -------
                    an sklearn.pipeline object containing vector_representation,
                    feature_selection and the classifier objects
                    """
    return Pipeline([('vect', vector_representation), ('chi', feature_selection), ('clf', classifier)])
