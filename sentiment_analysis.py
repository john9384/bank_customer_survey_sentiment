from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

from utils import remove_symbols, filter_stopwords, get_emotions_list




def sentiment(text):
    text_in_lower_case = text.lower()

    # Tokenize Text
    tokenized_words = word_tokenize(text_in_lower_case)

    # Remove Symbols
    filtered_symbols = remove_symbols(tokenized_words)

    # Remove Stopwords
    filtered_stopwords = filter_stopwords(filtered_symbols)


    # Lematizing Words
    wnet = WordNetLemmatizer()
    lemmatized_words =  [wnet.lemmatize(word) for word in filtered_stopwords]

    # Return emotion
    return get_emotions_list(lemmatized_words)
