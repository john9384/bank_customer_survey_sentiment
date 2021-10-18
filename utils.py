import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

import re





def remove_symbols(text_arr):
    clean_text = []
    for word in text_arr:
        res = re.sub(r'[^\w\s]', "", word)
        if res != "":
            clean_text.append(res)
    return clean_text

def filter_stopwords(word_list):
    clean_text = []

    for word in word_list:
        if not word in stopwords.words('english'):
            clean_text.append(word)

    return clean_text

def get_emotions_list(word_list):
    emotion_list = []
    with open('emotions_data/emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in word_list:
                emotion_list.append(emotion)
                
    return emotion_list


def plot_graph(emotion_list):
    count = Counter(emotion_list)
    fig, axs = plt.subplots()
    axs.bar(count.keys(), count.values())
    fig.autofmt_xdate()
    plt.savefig('output_img/graph.png')
    plt.show()
