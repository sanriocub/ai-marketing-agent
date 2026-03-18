# agent.py
import streamlit as st
from openai import OpenAI, OpenAIError

# Use the secret
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_campaign(audience, platform, goal, style):
    """
    Generate marketing campaign ideas, captions, reels, and strategy.
    """
    prompt = f"""
    You are a creative and strategic social media marketer.

    Target audience: {audience}
    Platform: {platform}
    Goal: {goal}
    Style: {style}

    Generate:
    CAMPAIGNS:
    - 3 creative campaign ideas

    CAPTIONS:
    - 5 engaging captions

    REELS:
    - 2 TikTok/Instagram reel ideas

    STRATEGY:
    - Best posting strategy
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        return f"⚠️ OpenAI API error: {e}"