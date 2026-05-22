# Jarvis - Voice Powered Data Analyst Assistant

An AI-powered voice assistant that analyzes data files using natural language.

## Features
- Voice input and output
- Load and analyze CSV and Excel files
- Ask questions about your data in plain English
- Auto-generates charts for visual answers
- Powered by Groq LLaMA 3.3

## Tech Stack
Python, SpeechRecognition, gTTS, Pandas, Matplotlib, Groq API

## How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Groq API key in `.env` file: `GROQ_API_KEY=your_key`
4. Run: `python main.py`

## Demo
Ask Jarvis questions like:
- "Top directors"
- "Which country has the most content?"
- "Movies vs TV shows"
- "Which year has the highest content?"