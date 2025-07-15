# 🧠 Reddit User Persona Generator

This project scrapes a Reddit user's recent activity and generates a detailed psychological user persona. It was developed as part of an assignment for the BeyondChats AI/LLM Internship selection process.

---

## 📌 Features

- ✅ Takes Reddit profile URL as input
- ✅ Scrapes recent **posts and comments**
- ✅ Saves raw data to `.txt`
- ✅ Generates a structured **ChatGPT prompt**
- ✅ Outputs a **user persona** with citations using ChatGPT (free mode)
- ✅ No OpenAI API key needed (manual ChatGPT use supported)

---

## 🖥️ Requirements

- Python 3.8+
- `praw` (Reddit API wrapper)
- `python-dotenv`

---

## 🛠️ Setup

1. **Install dependencies**

```bash
pip install -r requirements.txt
```
2. **Create a Reddit App (one-time setup)**

- Go to https://www.reddit.com/prefs/apps

- Create a "script" type app.

- Set redirect URI to: http://localhost:8080

- Copy the Client ID and Secret

3. **Create a .env file**
REDDIT_CLIENT_ID=your_id_here
REDDIT_CLIENT_SECRET=your_secret_here
REDDIT_USER_AGENT=my_persona_script

## 🚀 Usage
1. **Scrape Reddit Data**

```bash
python generate_persona.py
```
- Enter the Reddit profile URL like:
```
https://www.reddit.com/user/kojied/
```
- This will create a file: kojied_raw.txt

2. **Generate Prompt for ChatGPT**

```bash
python generate_prompt_for_chatgpt.py
```
- Enter the Reddit username (e.g., kojied)

- This will create: kojied_chatgpt_prompt.txt

3. **Use ChatGPT (No API Needed)**

- Go to https://chat.openai.com

- Paste the contents of the prompt file

- Wait for the persona output

- Copy and save the output in a file like: kojied_persona.txt

## 📁 Folder Structure
```
reddit-persona-generator/
├── generate_persona.py
├── generate_prompt_for_chatgpt.py
├── .env
├── requirements.txt
├── kojied_raw.txt
├── kojied_chatgpt_prompt.txt
├── kojied_persona.txt
└── README.md
```

## 💡 Sample Output
The final persona includes:

Name (fictional)

Age (guessed range)

Interests

- Personality traits

- Communication style

- Political/social views

- Sample quote

- Citations from Reddit posts/comments

## 📽️ Demo Video
- Link:https://drive.google.com/file/d/1dK8Vug55G90jGOkzwZzw6hqA_UT1fBTe/view?usp=sharing

## 📋 PEP-8 & Code Style
- All Python files follow PEP-8 guidelines

- Comments are added for clarity

- Functional programming structure is maintained










