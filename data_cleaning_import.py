# %%
#loading packages
import pandas as pd
import matplotlib as plt
import seaborn as sns


# %%
# reading the csv and checking it loads properly
def main()-> None:
    df = pd.read_csv("data.csv")
    stu_df = pd.read_csv("student_data.csv")

    df.head(1)
    stu_df.head(1)

if __name__ == "__main__":
    main()


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


def create_student_vectors(df: pd.DataFrame)->pd.DataFrame:
    """
    This function takes in the pandas data frame from the raw csv file of our classes journal entries
    It fixes column names and then created vector representations of the emotions and activities
    that our classmates flagged in the journal entries. It creates an overall vector including 
    all activities and emotions and vectors specific to emotions and activities. 
    arguments:
        df: pandas data frame
    returns:
        df: the cleaned and expanded dataset
    """
    df.columns = ["timestamp", "journal", "attributes"]
    labels = ["afraid", "angry", "anxious", "ashamed", "awkward", "bored", "calm", 
              "confused", "disgusted", "excited", "frustrated", "happy", "jealous", 
              "nostalgic", "proud", "sad", "satisfied", "surprised", "exercise", "family", 
              "food", "friends", "god", "health", "love", "recreation", "school", "sleep", 
              "work"]
    new_column = []
    
    for i in range(len(df)):
        vec = [0] * len(labels)
        attributes = df.loc[i, "attributes"]
        attributes_list = attributes.split(",")
        for i in range(len(attributes_list)):
            if attributes_list[i][0]==" ":
                attributes_list[i] = attributes_list[i][1:] 
        
        for j in range(len(attributes_list)):
            for m in range(len(labels)):
                if attributes_list[j] == labels[m]:
                    vec[m]+=1
        new_column.append(vec)

    df.insert(len(df.columns), "overall_vector", new_column)
    
    emotions = []
    activities = []

    for i in range(len(new_column)):

        emotions.append(new_column[i][:18])
        
        activities.append(new_column[i][18:])

    df.insert(len(df.columns),"emotion_vectors", emotions)
    df.insert(len(df.columns),"activity_vectors", activities)
        


