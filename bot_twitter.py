# Import necessary libraries
import openai
import tweepy
import requests
from decouple import config 

# Fetch API keys and tokens from environment variables for various services
CONSUMER_KEY = config('CONSUMER_KEY') # -> on shell terminal command: export CONSUMER_KEY="your CONSUMER_KEY"
CONSUMER_SECRET = config('CONSUMER_SECRET') ##
ACCESS_TOKEN = config('ACCESS_TOKEN') ## 
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET') ## 

CURRENTS_API_KEY = config('CURRENTS_API_KEY') ##
UNSPLASH_ACCESS_KEY = config('UNSPLASH_ACCESS_KEY') ##
OPENAI_API_KEY = config('OPENAI_API_KEY') ##

# Authenticate with Tweepy for Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# Set up OpenAI configuration
openai.api_key = OPENAI_API_KEY

def fetch_news_from_currents():
    """Fetch latest news using the Currents API."""
    url = "https://api.currentsapi.services/v1/latest-news"
    headers = {'Authorization': CURRENTS_API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        news = response.json()
        if news and news.get('news'):
            return news['news'][0]
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
    return None

def generate_tweet_based_on_news(news_title):
    """Generate a tweet based on a given news title using OpenAI."""
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Write a tweet about the following news article: {news_title}",
            max_tokens=280
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating tweet: {e}")
        return None

def fetch_random_image_based_on_query(query):
    """Fetch a random image relevant to a query using the Unsplash API."""
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = response.json()
        if image_data and image_data.get('urls'):
            return image_data['urls']['small']
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
    return None

def main():
    # 1. Fetch latest news
    news = fetch_news_from_currents()
    if not news:
        return

    news_title = news['title']

    # 2. Generate a tweet based on the news title
    tweet = generate_tweet_based_on_news(news_title)
    if not tweet:
        return

    # 3. Fetch a relevant image
    image_url = fetch_random_image_based_on_query(news_title)
    if image_url:
        image_response = requests.get(image_url)
        with open("temp_image.jpg", "wb") as f:
            f.write(image_response.content)
        # 4. Post the tweet with the image
        media = twitter_api.media_upload("temp_image.jpg")
        tweet += f" #news"
        twitter_api.update_status(status=tweet, media_ids=[media.media_id])
    else:
        # If no image is found, just tweet the text
        twitter_api.update_status(status=tweet)

if __name__ == "__main__":
    main()
