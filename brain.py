import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_brain(prompt, context=""):
    full_prompt = f"""
You are Jarvis, a Data Analyst assistant.
Answer in maximum 2 sentences. Be direct and concise.
No code blocks. No bullet points. Just plain spoken sentences.

Data Context:
{context}

User Question: {prompt}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": full_prompt}],
        max_tokens=150
    )
    return response.choices[0].message.content   

def decide_chart(prompt):
    chart_prompt = f"""
You are a data analyst assistant. Based on the user's question, decide what chart to show.
The dataset has these columns: type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description.

Respond ONLY in JSON format like this:
{{"chart": true, "column": "country", "kind": "bar", "top_n": 10, "title": "Top 10 Countries by Content"}}

If no chart is needed respond:
{{"chart": false}}

Rules:
- kind must be either "bar" or "pie"
- pie only for type/rating columns with few categories
- top_n is how many items to show (5, 10, 15, 20)
- column must be one of the actual dataset columns listed above

User question: {prompt}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": chart_prompt}],
        max_tokens=100
    )
    import json
    try:
        text = response.choices[0].message.content.strip()
        text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except:
        return {"chart": False}