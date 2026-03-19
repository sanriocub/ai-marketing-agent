import streamlit as st
from openai import OpenAI, OpenAIError

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_campaign(audience, platform, goal, style, campaign_type, campaign_desc, date, time, venue):

    prompt = f"""
You are a top-tier social media marketing strategist.

Your job is to create HIGHLY engaging, viral-ready campaigns that feel modern, creative, and platform-native.

Campaign Context:
- Target Audience: {audience}
- Platform: {platform}
- Goal: {goal}
- Style: {style}
- Campaign Type: {campaign_type}
- Description: {campaign_desc}
- Date: {date}
- Time: {time}
- Venue/Platform Details: {venue}

Instructions:
- Be specific, not generic
- Make ideas feel trendy and realistic
- Match tone to the selected style
- Optimise for engagement and virality

Output EXACTLY in this format:

CAMPAIGNS:
1. [Campaign name] – short explanation 
2. [Campaign name] – short explanation
3. [Campaign name] – short explanation

CAPTIONS:
1. ...
2. ...
3. ...
4. ...
5. ...

REELS:
1. ...
2. ...
3. ...
4. ...
5. ...

STRATEGY:
- Best posting time based on platform and audience
- Content frequency
- Hashtag strategy
- Engagement tips
- Anything that you thing will give the campaign extra boost
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an expert marketing strategist."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except OpenAIError as e:
        return f"⚠️ OpenAI API error: {e}"