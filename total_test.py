import chat
import face_expression
from gtts import gTTS
import os
import time
import playsound
import random
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re

filename = 'answer.mp3'

def chat_ai(text):
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    df = pd.read_csv('text_data/ChatbotData.csv')
    df_embeding = pd.read_csv('text_data/embeding.csv', header=None)

    em_result = model.encode(text)
    co_result = []

    for tmp in range(len(df_embeding)):
        data = df_embeding.iloc[tmp]
        co_result.append(cosine_similarity([em_result], [data])[0][0])

    r = random.randint(0, 5)

    df['cos'] = co_result
    df_result = df.sort_values('cos', ascending=False)
    result = df_result.iloc[r]['A']
    print(result)

    voice_result = str(result)
    filter = re.compile(r'[^ A-Za-z0-9가-힣+]')
    voice_result = filter.sub(' ',voice_result)

    tts = gTTS(text=voice_result, lang='ko', slow=True)
    tts.save(filename)
    playsound.playsound(filename)


chat_ai('난 행복해')



