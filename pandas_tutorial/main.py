import pandas as pd

df = pd.read_csv("data/survey_results_public.csv")

# if you want to know how many rows, and coloum
# print(df.shape)

#if you want to know each other coloum type
# print(df.info())

pd.set_option("display.max_columns", 85)
pd.set_option('display.width', 85)
print(df)