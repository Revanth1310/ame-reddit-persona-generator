import os
import re
import praw
import google.generativeai as genai
from dotenv import load_dotenv
from textwrap import fill

load_dotenv()

# Set up Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent="user_persona_extractor"
)

# Set up Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

def extract_username(url):
    match = re.search(r"reddit\.com/user/([^/]+)/?", url)
    return match.group(1) if match else None

def fetch_user_content(username, limit=10):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for submission in user.submissions.new(limit=limit):
        posts.append(f"[{submission.subreddit}] {submission.title}\n{submission.selftext[:300]}")
    for comment in user.comments.new(limit=limit):
        comments.append(f"[{comment.subreddit}] {comment.body[:300]}")

    return posts, comments

def generate_persona(username, posts, comments):
    prompt = f"""
You are an AI trained to generate user personas based on Reddit content. Create a persona in the style of a professional UX profile like the one for "Lucas Mellor" (age, occupation, motivations, habits, frustrations, personality, goals, etc).

Use the following content from user u/{username}:

POSTS:
{chr(10).join(posts)}

COMMENTS:
{chr(10).join(comments)}

Output the persona in clean, structured text (not JSON). Include citations to Reddit comments or posts that support each point.
"""

    response = model.generate_content(prompt)
    return response.text

def save_to_file(username, persona_text):
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved to {filename}")

if __name__ == "__main__":
    reddit_url = input("Enter Reddit profile URL: ").strip()
    username = extract_username(reddit_url)

    if username:
        print(f"Scraping data for u/{username}...")
        posts, comments = fetch_user_content(username)
        print(f"Generating persona using Gemini...")
        persona_text = generate_persona(username, posts, comments)
        save_to_file(username, persona_text)
    else:
        print("❌ Invalid Reddit profile URL.")
