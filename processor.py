import pandas as pd
import re

emotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
emotion_df = pd.read_csv('lexicons_compiled.csv')

def emotion_list(emotion):
    return emotion_df[emotion_df['emotion'] == emotion]['word']

emotion_dict = dict(zip(emotions, list(map(emotion_list, emotions))))

def calculate_emotion_score(text, emotion):
    words = re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', '', text)).lower().split(' ')
    return sum(emotion_dict[emotion].isin(words))
    

tweets = pd.read_csv('sample.csv')

for emotion in emotions:
    tweets[emotion] = tweets['text'].apply(lambda text: calculate_emotion_score(text, emotion))

print(tweets)

