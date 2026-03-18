import streamlit as st
from agent import generate_campaign
from openai import OpenAI, OpenAIError

# Use the secret
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Marketing Agent", layout="wide")

st.markdown(
    """
    <h1 style='font-family: "Comic Sans MS", cursive, sans-serif; font-size:24px;'>
        <img src="https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUydGcyOXU0ejQxdHM3NGpnMjNtMzltY2d3NjI0eDZraHdwOGQxeGZ3ZiZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/IhgKEBNmk3aZEe4dbw/giphy.gif" 
             width="300" 
             style="vertical-align:middle;"> 
        ⭐ AI Marketing Agent
    </h1>
    """,
    unsafe_allow_html=True
)
st.write("Create campaigns using AI + creativity ✨")

# Sidebar
st.sidebar.markdown("## 🐅 Made by Sanriocub Projects")
st.sidebar.markdown("[GitHub Repo](https://github.com/sanriocub/ai-marketing-agent)")
st.sidebar.markdown("---")

# Inputs
audience = st.text_input("🧸 Target Audience")
platform = st.selectbox("🦢 Platform", ["Instagram", "TikTok", "LinkedIn"])
goal = st.text_input("🐆 Campaign Goal")
style = st.selectbox("🦔 Style", ["Gen Z fun", "Luxury aesthetic", "Minimal clean"])

# Generate button
if st.button("Generate Campaign 🎬"):
    with st.spinner("Generating your campaign..."):
        result = generate_campaign(audience, platform, goal, style)

    st.success("Done!")

    # Save history
    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append(result)

    # Split sections
    sections = {
        "CAMPAIGNS": "",
        "CAPTIONS": "",
        "REELS": "",
        "STRATEGY": ""
    }

    current_section = None
    for line in result.split("\n"):
        line = line.strip()

        if "CAMPAIGNS" in line:
            current_section = "CAMPAIGNS"
        elif "CAPTIONS" in line:
            current_section = "CAPTIONS"
        elif "REELS" in line:
            current_section = "REELS"
        elif "STRATEGY" in line:
            current_section = "STRATEGY"
        elif current_section:
            sections[current_section] += line + "\n"

    # Tabs UI
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Campaigns", "✍️ Captions", "🎬 Reels", "📅 Strategy"])

    with tab1:
        st.markdown(sections["CAMPAIGNS"])

    with tab2:
        st.markdown(sections["CAPTIONS"])

        # Copy buttons for captions
        captions = sections["CAPTIONS"].split("\n")
        for i, cap in enumerate(captions):
            if cap.strip():
                st.code(cap)
                st.button(f"Copy Caption {i+1}", key=f"copy_{i}")

    with tab3:
        st.markdown(sections["REELS"])

    with tab4:
        st.markdown(sections["STRATEGY"])

    # Download
    st.download_button(
        label="📥 Download Campaign",
        data=result,
        file_name="campaign_plan.txt",
        mime="text/plain"
    )

# History section
st.markdown("---")
st.subheader("🕘 Past Campaigns")

if "history" in st.session_state:
    for i, item in enumerate(reversed(st.session_state.history)):
        with st.expander(f"Campaign {i+1}"):
            st.markdown(item)