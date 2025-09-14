
import pandas as pd

images = ['img1.jpg', 'img2.jpg']
labels = ['cat', 'dog']

df = pd.DataFrame({'image': images, 'label': labels})
df.to_csv('image_labels.csv', index=False)