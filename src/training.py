import pandas as pd
from src.preprocessing import clean_text


def predict(clf, review, clean=False):
    if clean:
        review = clean_text(review)
    prediction_df = pd.DataFrame([[review,0]],columns=["reviewText", "y"])
    rating = clf.predict(prediction_df["reviewText"])[0]
    prob_rating = clf.predict_proba(prediction_df["reviewText"])[0]
    return rating, prob_rating