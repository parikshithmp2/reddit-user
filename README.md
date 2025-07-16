# Reddit User Persona Generator
This is a Python-based tool that takes a Reddit user's profile URL, scrapes their recent posts and comments, and generates a **user persona** using OpenAI's GPT API (or a fallback if quota is exceeded).

# Features
- Scrapes up to 50 posts & 50 comments from a given Reddit user
- Sends content to OpenAI (GPT-3.5) to generate a detailed user persona
- Includes citations from the user's posts/comments
- Saves output in a readable `.txt` format
- Handles OpenAI API errors and rate limits with fallback logic

# Project Structure
reddit_user/
├── user_persona.py # Main script to run
├── scraper.py # Scrapes Reddit data
├── persona_generator.py # Sends content to GPT (or fallback)
├── requirements.txt # All dependencies
├── .env.example # Template for env config
├── personas/ # Output folder for personas
└── README.md # Project info

## Install Dependencies
pip install -r requirements.txt

## Configure Environment Variables
Create a .env file in the root folder and add:

REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=reddit_user_persona
OPENAI_API_KEY=your_openai_api_key

## Run this command in the terminal:
python user_persona.py https://www.reddit.com/user/kojied/

## The output will be saved as:
personas/kojied.txt
personas/Hungry-Move-6603.txt
