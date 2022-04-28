import praw
import csv

reddit = praw.Reddit(
    client_id = '',
    client_secret="",
    user_agent="",
    username="",
    password=""
)


subreddit = reddit.subreddit("covidvaccine").top("year") #gets top submissions in r/covidvaccine in the past year

with open("reddit_demo.csv", 'a', encoding="utf-8") as file:
    headers = ['ID', 'Date_utc', 'Author', 'Body','Post_ID', 'Post_Author']
    writer  = csv.DictWriter(file, fieldnames = headers, extrasaction='ignore')
    writer.writeheader()
    for post in subreddit:
        post.comments.replace_more()
        for comment in post.comments:
            data = {'ID':comment.id, 'Date_utc':comment.created_utc, 'Author':comment.author, 'Body': comment.body,
            'Post_ID':post, 'Post_Author':post.author}
            writer.writerow(data)

