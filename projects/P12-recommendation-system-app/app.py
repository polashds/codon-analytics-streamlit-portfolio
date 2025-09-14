
from surprise import Dataset, SVD, Reader
from surprise.model_selection import train_test_split

data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], Reader(rating_scale=(1,5)))
trainset, testset = train_test_split(data, test_size=0.25)
model = SVD()
model.fit(trainset)
predictions = model.test(testset)