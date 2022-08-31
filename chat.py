import random
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

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
    return result
