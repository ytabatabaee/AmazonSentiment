import questionary
import pickle
# from src.training import predict_review, predict_summary
import os

if __name__ == "__main__":
    while True:
        section = questionary.select(
            "Enter the full text or summary of a customer review for a product:",
            choices=["1. Full review", "2. Summary", "3. Exit"],
        ).ask()

        if section == "1. Full review":
            clf_choice = questionary.select(
                "Select which classifier you would like to use:",
                choices=["1. Default (best performing)", "2. Naive Bayes", "3. SVM"],
            ).ask()
            clf = None
            if clf_choice == "1. Default (best performing)":
                with open('models/default_clf_review.pkl', 'rb') as f:
                    clf = pickle.load(f)
                
        elif section == "2. Summary":
            clf_choice = questionary.select(
                "Select which classifier you would like to use:",
                choices=["1. Default (best performing)", "2. Naive Bayes", "3. SVM"],
            ).ask()
            clf = None
            if clf_choice == "1. Default (best performing)":
                with open('models/default_clf_review.pkl', 'rb') as f:
                    clf = pickle.load(f)

        elif section == "3. Exit":
            exit(0)
