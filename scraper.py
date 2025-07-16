import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def fetch_user_data(username, limit=50):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for post in user.submissions.new(limit=limit):
        posts.append(f"Title: {post.title}\nBody: {post.selftext}\n")

    for comment in user.comments.new(limit=limit):
        comments.append(f"Comment: {comment.body}\n")

    return posts, comments
