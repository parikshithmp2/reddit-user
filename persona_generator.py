import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import APIConnectionError, RateLimitError, OpenAIError


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_persona(posts, comments):
    combined = "\n".join(posts + comments)[:15000]

    prompt = f"""
You are an AI assistant. Based on the following Reddit posts and comments, generate a detailed User Persona.

Content:
{combined}

Please include:
- Personality traits
- Values and beliefs
- Interests and hobbies
- Writing style
- For each trait, cite a specific post or comment that supports it.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except (RateLimitError, OpenAIError, APIConnectionError) as e:
        print(f"⚠️ OpenAI API failed: {e}")
        print("🟡 Using simulated output instead...")

        # Return dummy persona for demonstration
        return f"""
🧑 User Persona (Simulated Output)

- **Personality Traits:** Curious, humorous, and highly engaged in niche communities.
  - 🧩 Cited from Comment: "{comments[0][:80]}..."

- **Values & Beliefs:** Values privacy, anonymity, and freedom of expression.
  - 📌 Cited from Post: "{posts[0][:80]}..."

- **Interests & Hobbies:** Enjoys gaming, memes, technology debates, and life advice threads.
  - 🎮 Cited from Post: "{posts[1][:80]}..."

- **Writing Style:** Informal, sarcastic, and often uses memes or emojis.
  - ✍️ Cited from Comment: "{comments[1][:80]}..."
"""
