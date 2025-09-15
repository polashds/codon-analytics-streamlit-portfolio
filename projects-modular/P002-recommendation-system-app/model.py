
from surprise import Dataset, SVD, Reader

def train_model(df):
    reader = Reader(rating_scale=(df['rating'].min(), df['rating'].max()))
    data = Dataset.load_from_df(df[['user_id','item_id','rating']], reader)
    trainset = data.build_full_trainset()
    model = SVD()
    model.fit(trainset)
    return model

def predict_rating(model, user, item):
    pred = model.predict(user, item)
    return pred.est