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
    if clean:
        review = clean_text(review)
    prediction_df = pd.DataFrame([[review,0]],columns=["reviewText", "y"])
    rating = clf.predict(prediction_df["reviewText"])[0]
    prob_rating = clf.predict_proba(prediction_df["reviewText"])[0]
    return rating, prob_rating


def create_classifier(vector_representation, feature_selection, classifier):
    return Pipeline([('vect', vector_representation), ('chi', feature_selection), ('clf', classifier)])
