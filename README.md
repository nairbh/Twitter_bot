# Twitter News Bot 🐦📰

This project is a Python-based bot designed to automatically fetch the latest news articles, generate tweets based on them using OpenAI's powerful natural language models, and enhance the tweet with a relevant image sourced from Unsplash.

## Features

- **Fetch Latest News**: Uses the Currents API to get the latest headlines.
- **Dynamic Tweet Generation**: Uses OpenAI to transform news headlines into engaging tweet content.
- **Image Attachment**: Adds relevant imagery to the tweet by querying Unsplash based on the news topic.

## Prerequisites

1. Python 3.x installed.
2. Twitter Developer Account and created application to get access tokens.
3. OpenAI API key.
4. Unsplash Developer Account for image access.
5. Currents API key for news headlines.

## Setup & Configuration

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nairbh/Twitter_bot.git
    cd twitter_bot
    ```

2. **Install required packages**:
    ```bash
    pip3 install -r requirements.txt
    ```

3. **Environment Configuration**:
    Store your API keys and tokens in a `.env` file in the root directory. Use the sample structure provided below:

    ```
    CONSUMER_KEY=YOUR_TWITTER_CONSUMER_KEY
    CONSUMER_SECRET=YOUR_TWITTER_CONSUMER_SECRET
    ACCESS_TOKEN=YOUR_TWITTER_ACCESS_TOKEN
    ACCESS_TOKEN_SECRET=YOUR_TWITTER_ACCESS_TOKEN_SECRET
    CURRENTS_API_KEY=YOUR_CURRENTS_API_KEY
    UNSPLASH_ACCESS_KEY=YOUR_UNSPLASH_ACCESS_KEY
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

4. **Run the Bot**:
    ```bash
    python bot_sphere_infos.py
    ```

## Contributing

If you have suggestions or improvements, feel free to fork this repository and create a pull request. All contributions are welcome!

## License

This project is open-source and available to everyone under the [MIT License](LICENSE).

## Acknowledgements

- [OpenAI](https://openai.com/)
- [Tweepy](https://www.tweepy.org/)
- [Unsplash Developers](https://unsplash.com/developers)
- [Currents API](https://currentsapi.services/)

## Authors

Nairbh - [Github](https://github.com/nairbh)
