# 🤖 AI Marketing Agent

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-black?logo=openai)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> An AI-powered marketing assistant that generates creative campaign ideas, captions, and posting strategies — all from a simple Streamlit interface.

---

## ✨ Features

- 🎯 **Campaign Generator** — Get tailored campaign ideas for your audience and platform  
- 💡 **Content Inspiration** — 3 campaign ideas, 5 captions, and 2 reel concepts per request  
- 📅 **Posting Strategy** — AI-based recommendations for timing and style  
- 🧩 **No-Code Interface** — Use Streamlit to interact with the model easily  
- 🔐 **.env Security** — Keep your API keys safe and out of version control  

---

## 🗂️ Project Structure

```bash
ai_marketing_agent/
│
├── agent.py           # Core logic using OpenAI API
├── app.py             # Streamlit web interface
├── .env               # Stores your OpenAI API key
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation


---

## Setup Instructions
1️⃣ Clone or create your project
git clone [github.com](https://github.com/yourusername/ai-marketing-agent.git)
cd ai-marketing-agent


2️⃣ Create a virtual environment
Using Anaconda:
conda create -n ai_agent python=3.10
conda activate ai_agent

Or with venv:
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows


3️⃣ Install dependencies
pip install -r requirements.txt


4️⃣ Set up your environment variables
Create a file named .env:
OPENAI_API_KEY=your_real_openai_api_key_here


5️⃣ Run the app
streamlit run app.py


🧠 Example Usage
Enter your Target Audience (e.g., Gen Z fashion lovers)
Choose a Platform (Instagram, TikTok, etc.)
Describe your Goal (Increase engagement, Build awareness)
Pick your Style (Trendy & bold, Luxury aesthetic, etc.)
Hit Generate Campaign 🎬


🚀 Future Enhancements
🔍 Audience persona builder
🧾 Competitor content analyzer
🧠 A/B ad copy tester
📅 Automated posting scheduler
💬 Multi‑agent collaboration (copywriter + strategist modes)


🛠️ Built With


Tool	Purpose

python.org
Core programming language

streamlit.io
Web app framework

platform.openai.com
AI content generation

pypi.org
Manage environment variables


🌟 Show Your Support
If you like this project, please ⭐ star this repo and share it with others who love AI + marketing!