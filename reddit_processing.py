import praw
from psaw import PushshiftAPI
import pandas as pd
import numpy as np

def find_submission(ids):
    try:
        submission = reddit.submission(id = ids['Submission'])
        ids['Submission_Author'] = submission.author
        ids['Submission_Title'] = submission.title
    except prawcore.exceptions.NotFound:
        ids['Submission_Author'] = 'idk'
        ids['Submission_Title'] = 'removed'
    return ids

reddit = praw.Reddit(

)


api = PushshiftAPI()

subreddits = ['trueantivaccination','vaccines','covidvaccine','covidvaccinated','antivaxxers',
'conspiracy', 'conspiracytheories','conspiracy_commons', 'covid19','coronavirus', 'conservative', 'news'] 

#worldnews

subreddit_data = []


for subreddit in subreddits:
    url = f"https://raw.githubusercontent.com/yuhsin-huang/Math168Project/main/{subreddit}.csv"
    data = pd.read_csv(url)
    data = data.dropna(subset = ['Author'])

    submissions = pd.DataFrame(data = {'Submission':data['Submission'].unique()})
    submissions = submissions.apply(find_submission, axis = 1)

    data_joined = data.merge(submissions, how = 'left', on = 'Submission')

    data_joined = data_joined.dropna(subset = ['Author'])
    data_joined = data_joined.dropna(subset = ['Parent_Author', 'Submission_Author'], how = 'all')
    data_joined = data_joined[total_data["Author"] != "AutoModerator"]

    subreddit_data.append(data_joined)

reddit_data = pd.concat(subreddit_data, ignore_index = True)
reddit_data.to_csv("C:\\Users\\chris\\Documents\\Math168Project\\reddit_data.csv", index = True)

