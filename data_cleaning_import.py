# %%
#loading packages
import pandas as pd
import matplotlib as plt
import seaborn as sns


# %%
# reading the csv and checking it loads properly
df = pd.read_csv("data.csv")

#print(df.columns)
df.head(1)


# %%
def clean_create_vectors(df):
    df.columns = ["journal", 
              "afraid", "angry", "anxious", "ashamed", "awkward", "bored", 
              "calm", "confused", "disgusted", "excited", "frustrated", "happy", "jealous", 
              "nostalgic", "proud", "sad", "satisfied", "surprised", 
              "exercise", "family", "food", "friends", "god", "health", "love", "recreation", "school", "sleep", "work"]
    transform = {"True":1, 
                 "False":0}
    
    attributes = []
    labels = ["afraid", "angry", "anxious", "ashamed", "awkward", "bored", 
              "calm", "confused", "disgusted", "excited", "frustrated", "happy", "jealous", 
              "nostalgic", "proud", "sad", "satisfied", "surprised"]
    
    for i in range(len(df)):
        vec = []
        for j in range(18):
            value = df.loc[i, labels[j]]
            vec.append(transform[str(value)])
        attributes.append(vec)

    df.insert(1, "emotion_vectors", attributes)

    attributes = []
    labels = ["exercise", "family", "food", "friends", "god", "health", "love", "recreation", "school", "sleep", "work"]
    for i in range(len(df)):
        vec = []
        for j in range(11):
            value = df.loc[i, labels[j]]
            vec.append(transform[str(value)])
        attributes.append(vec)

    df.insert(1, "activity_vectors", attributes)
    return df

#new_df = clean_create_vectors(df)
#new_df.head()


            


# %%
#new_df.head()


