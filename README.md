# 🧠 Reddit User Persona Generator

This tool scrapes a Reddit user's profile and generates a detailed persona using the Gemini LLM (Google Generative AI), mimicking the style of professional UX personas.

---

## 📌 Features

- Scrapes **Reddit posts and comments**.
- Builds a structured **persona**: motivations, behaviors, frustrations, goals.
- **Cites** posts/comments used for generating traits.
- Outputs to a .txt file.
- Uses **Gemini LLM** for rich persona generation.

---

## 🔧 Tech Stack

- Python 3.8+
- Reddit API via [PRAW](https://praw.readthedocs.io)
- Google Gemini via [google-generativeai](https://pypi.org/project/google-generativeai/)
- Environment config via python-dotenv

---

## 🚀 How to Clone and Run

'''bash
git clone https://github.com/your-username/reddit-persona-generator.git
cd reddit-persona-generator
