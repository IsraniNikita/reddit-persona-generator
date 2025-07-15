import os
import praw
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def get_user_data(username):
    redditor = reddit.redditor(username)
    comments = [comment.body for comment in redditor.comments.new(limit=20)]
    posts = [post.title + "\n" + post.selftext for post in redditor.submissions.new(limit=10)]
    return comments, posts

# Example test
if __name__ == "__main__":
    url = input("Paste Reddit Profile URL: ")
    username = url.split("/user/")[1].replace("/", "")
    comments, posts = get_user_data(username)
    
    with open(f"{username}_raw.txt", "w", encoding="utf-8") as f:
        f.write("### POSTS ###\n")
        for p in posts:
            f.write(p + "\n\n")
        f.write("### COMMENTS ###\n")
        for c in comments:
            f.write(c + "\n\n")
    
    print(f"Data saved to {username}_raw.txt")
