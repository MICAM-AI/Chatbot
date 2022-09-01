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

#filename = 'answer.mp3'
model = SentenceTransformer('jhgan/ko-sroberta-multitask')
df = pd.read_csv('text_data/ChatbotData.csv')
df_embeding = pd.read_csv('text_data/embeding.csv', header=None)

def chat_ai(text, rank):
    em_result = model.encode(text)
    co_result = []

    for tmp in range(len(df_embeding)):
        data = df_embeding.iloc[tmp]
        co_result.append(cosine_similarity([em_result], [data])[0][0])

    #r = random.randint(0, 5)

    df['cos'] = co_result
    df_result = df.sort_values('cos', ascending=False)
    result = df_result.iloc[rank]['A']
    #print(result)
    make_sound_mp3(result)

    return result

tmp_dict = {
    '응, 속상했어':4, #자신을 비난하지 마세요.
    '다 나때문인거 같아': 1, #아니에요 너무 자책하지 마세요
    '그런 말을 해줘서 고마워' : 4, # 잊지말고 보답하세요
    'ㅋㅋㅋ 다시올게':4 #다녀오세요!
}

def sinario(tmp):
    if tmp in tmp_dict.keys():
        #print('in')
        #print(tmp)
        input_text = tmp
        #print(input_text)
        input_rank = tmp_dict[f'{input_text}']
        #print(input_rank)
        print(chat_ai(input_text, input_rank))
    else:
        input_text = tmp
        input_rank = random.randint(0, 5)
        print(chat_ai(input_text, input_rank))

def make_sound_mp3(text):
    voice_result = str(text)
    filter = re.compile(r'[^ A-Za-z0-9가-힣+]')
    voice_result = filter.sub(' ', voice_result)

    tts = gTTS(text=voice_result, lang='ko', slow=True)
    tts.save('result.mp3')
    time.sleep(0.3)
    playsound.playsound('result.mp3')


