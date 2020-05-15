## sentiment.py
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

from flair.data import Sentence
#from flair.models import SequenceTagger
from flair.models import TextClassifier
classifier = TextClassifier.load('en-sentiment')


def make_sentiment(text, model):
    """
    :param text: string text
    :param model: string which model to use for sentiment analysis
    :return: sentiment score as number
    """
    if model == 'nltk':
        sentiment = sid.polarity_scores(text)['compound']
    elif model == 'flair':
        s = Sentence(text)
        classifier.predict(s)
        sentiment = s.labels
        try:
            if sentiment[0].value == "POSITIVE":
                return sentiment[0].score
            elif sentiment[0].value == "NEGATIVE":
                return sentiment[0].score * -1
        except:
            return None
    return sentiment