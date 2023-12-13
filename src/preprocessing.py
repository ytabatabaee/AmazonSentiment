import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer


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


def word_cloud(data, ax, category):
    """Create a wordcloud of text data
            Parameters
            ----------
            data : dataframe
                Dataframe containing the review text
            ax  : axis
                Plot axis
            category: str
                category of the product review (e.g. "software")
            """
    wordcloud = WordCloud(
    background_color = "white",
    max_font_size = 40,
    max_words = 200,
    stopwords = stopwords.words("english"),
    scale = 3).generate(str(data["reviewText"]))
    ax.axis("off")
    ax.imshow(wordcloud)
    ax.set_title(category, fontsize=30)


def get_top_n_bigram(data, n=None):
    """find the top bigrams in a collection of text data
                Parameters
                ----------
                data : dataframe
                    Dataframe containing the review text
                n  : int
                    Number of returned bigrams
                Returns
                -------
                list
                    top n bigrams in data
                """
    vec = CountVectorizer(ngram_range=(2, 2),stop_words='english').fit(data.values.astype('U'))
    bag_of_words = vec.transform(data)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]


def n_gram_plot(data, title, color):
    """Plots the top n bigrams in data (output of get_top_n_bigram)
                Parameters
                ----------
                data : list
                    the list of bigrams to be plotted
                title  : str
                    title of the plot
                color: str
                    specifies the color of the plot
                """
    x=[x[0] for x in data]
    y=[x[1] for x in data]
    sns.barplot(y=x,x=y,color='{}'.format(color))
    plt.title('{} reviews'.format(title),fontsize=15)
    plt.yticks(rotation=0,fontsize=15)