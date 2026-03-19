
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

![Snoopy typing](https://i.pinimg.com/originals/fb/03/8c/fb038c9d39ed13ab401512e9f87d6fa1.gif)  
*When you’re crafting the perfect caption…*  

![Snoopy brainstorming](https://i.pinimg.com/originals/ff/69/93/ff699349b80c0c5d792d29104c0c75dc.gif)  
*When the AI starts thinking…*  

![Snoopy dancing](https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUydnY3b3RvZDBscG1neTZsd2FnMnJmeTcwYzZ4MGJzMWlxNng3YnVxbiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l3q2XXYxkdxzjMC9G/giphy.gif)  
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
* Anaconda Prompt to set the environment
* Python 3.11

---

## 🐾 Author

**Sanriocub Projects**
[GitHub Repo](https://github.com/sanriocub/ai-marketing-agent)

