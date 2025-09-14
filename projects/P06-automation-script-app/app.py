
import pandas as pd

# Automate merging multiple CSVs
import glob
all_files = glob.glob("data/*.csv")
df_list = [pd.read_csv(f) for f in all_files]
merged_df = pd.concat(df_list)
merged_df.to_csv('merged_data.csv', index=False)