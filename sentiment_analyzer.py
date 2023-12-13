import questionary
import pickle
from src.training import predict
from src.preprocessing import *
import os


def return_rating(clf, review_text):
    """Takes a classifier and a review as input and predicts and prints the sentiment of the review
                Parameters
                ----------
                clf : classifier object
                   A pre-trained classifier that can predict the sentiment of a review (a number between 1 to 5)
                review_text: str
                    Review text
                """
    rating, prob_rating = predict(clf, review_text)
    print('Overall rating: ' + str(rating) + ', sentiment: ' + rating_to_sentiment(rating))
    print('Probability of the review being rated in categories 1-5:\n', prob_rating)


def call_classifier(review_text):
    """Takes a review text as input and calls a classifier to predict its sentiment
                Parameters
                ----------
                review_text: str
                    Review text
                """
    print('Predicting the sentiment for the following review:')
    print('"' + review_text + '"')
    clf_choice = questionary.select(
        "Select which classifier you would like to use:",
        choices=["1. Default (best performing)", "2. User-specified classifier"]).ask()

    if clf_choice == "1. Default (best performing)":
        if not os.path.exists('models/default_clf_review.pkl'):
            if os.path.exists('models/default_clf_review.pkl.zip'):
                os.system('unzip models/default_clf_review.pkl.zip -d models')
            else:
                print('Classifier path is wrong!')
                return
        with open('models/default_clf_review.pkl', 'rb') as f:
            clf = pickle.load(f)
        return_rating(clf, review_text)

    elif clf_choice == "2. User-specified classifier":
        clf_path = questionary.text("Enter the path to the classifier pickle file: ").ask()
        with open(clf_path, 'rb') as f:
            clf = pickle.load(f)
        return_rating(clf, review_text)


if __name__ == "__main__":
    print('\033[1m ** Sentiment analyzer for Amazon product reviews** \033[0m \n')
    while True:
        section = questionary.select(
            "Enter the full text or a file path containing a customer review for a product:",
            choices=["1. Review text", "2. Review file", "3. Exit"],
        ).ask()

        if section == "1. Review text":
            review_text = questionary.text("Enter review text: ").ask()
            call_classifier(review_text)

        elif section == "2. Review file":
            review_path = questionary.text("Enter the path to the review file: ").ask()
            if os.path.exists(review_path):
                with open(review_path, 'r') as f:
                    review_text = f.read()
            else:
                print('Review path is wrong!')
                exit(0)
            call_classifier(review_text)

        elif section == "3. Exit":
            exit(0)

