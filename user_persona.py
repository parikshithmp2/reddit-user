import sys
from scraper import fetch_user_data
from persona_generator import generate_persona
import os

def extract_username(url):
    return url.rstrip('/').split('/')[-1]

def save_output(username, persona_text):
    os.makedirs("personas", exist_ok=True)
    with open(f"personas/{username}.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python user_persona.py <Reddit profile URL>")
        return

    url = sys.argv[1]
    username = extract_username(url)
    print(f"Fetching data for user: {username}")

    posts, comments = fetch_user_data(username)
    print("Generating persona...")
    persona = generate_persona(posts, comments)
    
    save_output(username, persona)
    print(f"Persona saved at: personas/{username}.txt")

if __name__ == "__main__":
    main()
