# ANN_final
This project is aimed at using journaling data to predict emotions from entries. 

Files Contained in the Repo
data_cleaning.ipynb: 
    File containing all of the data transformations and cleaning that we had to do on
    both the original dataset and the dataset we collected from students in our class
data_cleaning_import.py: 
    This is the same file as above except as a .py file for easier importing
data.csv: 
    csv file of the Lemotif dataset
student_data.csv:
    csv file of the student journal entries and emotions/activities
model.ipynb:
    This is our initial logistic regression model
distilbert_model.ipynb:
    This is our distilbert models that have different attributes added to them
topic_emotion_correlation.ipynb
    File contaiend topic and emotion correlation analysis to see ow the themes from the journals
    line up with the activities being done in the journal entries
best_model.pt & emotion_classification_model_complete.pt
    Saved models so we don't need to run code again
daily_notes.txt
    daily journal of results and things we have done to keep track and then compile our results. 

# Blog Post:
This is a blog post detailing our work flow and the various challenges we faced. We choose this project since idenitfying your emotions can have tremendous power in helping you to work through them. We found our dataset on Kaggle and it came from a study called, "Lemotif: An Affective Visual Journal Using Deep Neural Networks", by X. Li and Devi Parikh (arXiv:1903.07766)(https://arxiv.org/abs/1903.07766). They collected journal entries from 1474 participants by asking respondents the following two questions: 
    What were salient aspects of your day yesterday? 
    How did you feel about them?
They then were asked to label which emotions and activities were expressed or are mentioned in the journal entry. The emotions they had available are happy, satisfied, calm, proud, excited, frustrated, anxious, surprised, nostalgic, bored, sad, angry, confused, disgusted, afraid, ashamed, awkward, and jealous. The topics they included were family, work, food, sleep, friends, health, recreation, god, love, school, exercise. The goal of the initial study was to develop tools for a journaling app to create image motifs of the emotions or activities that someone has expressed in a journal entry. We wanted to focus more on identifying emotions and seeing how that aligns with activities present in the journal entries. 
The challenges we anticipated during this project were poor performance on emotions that aren't highly expressed in the dataset, long run times on training models, lower accuracy due to using small models so we can run them. 

# Data Cleaning and Transformations
The lemotif data came in the format of a csv with the journal entries being one column and then the rest of the columns each referring to an emotion or topic. each entry in these colmns was either TRUE or FALSE depending on whether it was expressed in the journal entry. First, we renamed the columns to be more easy to work with. Then we wrote code to transform the emotions and topics columns into a single vector of ones and zeros depending on if it was expressed/present or not. 

The student data came in a different format due to the way google forms saves things so it just gave us a string corresponding to the emotions or topics that people in our class had ticked on the form. We turned these into lists then transformed them into the same type of vectors as above. This format of data allows us to easily train models and compare their outputs against the vectors. 

# Early modeling and topic emotion correlations

# DistilBert modeling

# Working to improve performance

# Analysis of results & Conclusion



