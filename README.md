# Sentiment analysis on Amazon product reviews
This repository contains the codes and data for the final project of CS 410: Text Information Systems course at UIUC in Fall 2023. The main goal of this project is to build a tool for sentiment analysis of Amazon product reviews and perform sentiment analysis on a large collection of reviews from different categories of products, such as clothes, appliances, software, etc. Other goals are to get insight about various factors that correlate with the sentiment of a review, such as the type of words/phrases used, length of the reviews, etc, and also compare different machine learning classifiers for sentiment analysis on this data.

## Contents
- [Dependencies](#dependencies)
- [Software](#software)
- [Data](#data)
- [Codes](#codes)
  * [Preprocessing](#preprocessing)
  * [Data analysis](#data-analysis)
  * [Sentiment analysis](#training-and-evaluation)
- [Pretrained classifiers](#pretrained-models)
- [Results](#results)
- [Acknowledgements](#acknowledgements)

## Dependencies
The Amazon sentiment analysis software is written in Python 3.9 and has the following dependencies.
- [Python 3.7+](https://www.python.org)
- [scikit-learn 1.2.2](https://scikit-learn.org/stable/index.html)
- [questionary](https://pypi.org/project/questionary/)
- [nltk](https://www.nltk.org/)
- [Numpy](https://numpy.org)
- [Pandas](https://pandas.pydata.org/)

If you have Python3 and pip, use `pip install -r requirements.txt` to install all dependencies.

## Software
The sentiment analysis tool is implemented as a command-line software that takes a product review and a pre-trained classifier as input and predicts the rating (an integer between 1 to 5) and the sentiment of the review (Good, Bad, Average), as well as a probability distribution over the five rating classes.

![alt text](example-test.png)

## Data

The data used in this project is part of the [Amazon reviews dataset from UCSD](https://nijianmo.github.io/amazon/index.html) that was published in 2018, and contains more than 233 million Amazon reviews between the years 1996 to 2018 from 29 different product categories, as well as additional information and metadata for each product. Since this dataset was very large and analyzing all of it was not feasible, we sampled a small collection of it containing at most 200,000 reviews from each of the 8 selected product categories: Fashion, Software, Appliances, Gift Cards, Magazine Subscriptions, Prime Pantry, Luxury Beauty, All Beauty. The total number of analyzed reviews was 1,436,883.

The selected datasets from these 8 categories are available at [this Google Drive link](https://drive.google.com/drive/folders/1V6-7o-2mcjb5A1VQZEFVC3H-xtkz0PyG?usp=sharing).

## Acknowledgements
This project uses some ideas from the projects explained in this report https://cs229.stanford.edu/proj2018/report/122.pdf and this github repository https://github.com/avinash-vk/Sentiment-analysis-on-amazon-reviews.
