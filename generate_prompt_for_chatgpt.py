import os

def load_user_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def build_chatgpt_prompt(user_text):
    prompt = f"""
You are an AI that builds psychological user personas based on Reddit content.
Below is a Reddit user’s recent posts and comments. Analyze and write a user persona.

--- START OF REDDIT CONTENT ---
{user_text}
--- END OF REDDIT CONTENT ---

The output should include:

- Name (make one up)
- Age (guess range)
- Interests
- Personality Traits
- Communication Style
- Political/Social Views (if obvious)
- Sample Quote from their writing
- CITE which comments/posts were used.
"""
    return prompt

if __name__ == "__main__":
    username = input("Enter Reddit username (e.g., kojied): ")
    raw_file = f"{username}_raw.txt"

    if not os.path.exists(raw_file):
        print(f"❌ File {raw_file} not found. Run your Reddit scraper first.")
        exit()

    user_data = load_user_data(raw_file)
    chatgpt_prompt = build_chatgpt_prompt(user_data)

    prompt_file = f"{username}_chatgpt_prompt.txt"
    with open(prompt_file, "w", encoding="utf-8") as f:
        f.write(chatgpt_prompt)

    print(f"✅ Prompt saved to {prompt_file}")
    print("➡️ Open https://chat.openai.com and paste the contents of this prompt file.")
    print(f"📝 Save ChatGPT's response to {username}_persona.txt")
