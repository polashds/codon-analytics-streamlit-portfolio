
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.read_csv('user_content.csv')
similarity_matrix = cosine_similarity(df.drop('user_id', axis=1))
df_sim = pd.DataFrame(similarity_matrix, index=df['user_id'], columns=df['user_id'])