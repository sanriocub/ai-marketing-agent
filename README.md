
# ⭐ AI Marketing Agent

Create campaigns using AI + creativity ✨

---

## 🐔 Features

- Generate **creative campaign ideas** tailored to your target audience  
- Suggest **captions** for Instagram, TikTok, or LinkedIn  
- Recommend **reel/video ideas** and **posting strategy**  
- Keep a **history** of past campaigns  
- **Download campaigns** as text files  

---

## 🖥️ Demo & Fun

While your campaigns load, enjoy some Snoopy vibes 🐶  

![Snoopy typing](https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif)  
*When you’re crafting the perfect caption…*  

![Snoopy brainstorming](https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif)  
*When the AI starts thinking…*  

![Snoopy dancing](https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif)  
*When the campaign generation is done!*  

---

## 🐅 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/sanriocub/ai-marketing-agent.git
cd ai-marketing-agent
````

### 2. Create & activate your conda environment

```bash
conda create -n ai_marketing_agent python=3.11
conda activate ai_marketing_agent
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup your OpenAI API key

Create `.streamlit/secrets.toml`:

```toml
# .streamlit/secrets.toml
OPENAI_API_KEY="your_openai_api_key_here"
```

> 🐆 **Do not commit this file to GitHub**. Add it to `.gitignore`.

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🫎 Usage

1. Enter your **target audience**, **platform**, **goal**, and **style**.
2. Click **Generate Campaign 🎬**.
3. Browse through **Campaigns**, **Captions**, **Reels**, and **Strategy** tabs.
4. Download your campaign or copy captions directly.
5. View your past campaigns in the history section.

---

## 🦔 Git Ignore

```gitignore
.env
__pycache__/
*.pyc
.streamlit/secrets.toml
```

---

## 💻 Built With

* [Streamlit](https://streamlit.io/) – Web interface
* [OpenAI API](https://platform.openai.com/) – Campaign generation
* Python 3.11

---

## 🐾 Author

**Sanriocub Projects**
[GitHub Repo](https://github.com/sanriocub/ai-marketing-agent)

