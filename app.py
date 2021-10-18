from sentiment_analysis import sentiment
from utils import plot_graph

if __name__ == "__main__":
    text = open('response_data/response.txt', encoding='utf-8').read()


    def analysis(speech):
        emotion_list = sentiment(speech)
        print(emotion_list)
        plot_graph(emotion_list)


    analysis(text)