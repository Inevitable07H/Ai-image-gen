import streamlit as st
import requests
from groq import Groq
from PIL import Image
import io
import os

# ---- PAGE CONFIG ----
st.set_page_config(page_title="🎨 AI Image Generator", page_icon="🎨", layout="centered")

# ---- Custom Styling ----
st.markdown(
    """
    <style>
        body { background-color: #0E1117; color: #E0E0E0; }
        .stTextArea textarea { background-color: #1A1D23; color: #F5F5F5; border-radius: 10px; }
        .stButton button {
            border-radius: 12px;
            background: linear-gradient(90deg, #4F46E5, #9333EA);
            color: white;
            font-weight: 600;
            padding: 0.6rem 1.2rem;
            font-size: 16px;
            transition: 0.3s;
            border: none;
        }
        .stButton button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #6366F1, #A855F7);
        }
        .block-container { padding-top: 2rem; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Title ----
st.title("🎨 **Stability AI – Creative Image Generator**")
st.markdown("Enhance your ideas with smart prompts and cinematic visuals powered by Groq & Stability AI.")

# ---- API KEYS ----
STABILITY_API_KEY = "sk-0DiRwm0wJ5DLOmO0Il2X5yu6gzt4Sx4RKajZ5dV1xqlwVAZW"
GROQ_API_KEY = "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"

# ---- Initialize Groq client ----
groq_client = Groq(api_key=GROQ_API_KEY)

# ---- Session Management ----
if "enhanced_prompt" not in st.session_state:
    st.session_state["enhanced_prompt"] = ""

# ---- Creative Mood Selector ----
mood = st.selectbox(
    "🎭 Choose a creative mood to style your prompt:",
    [
        "Cinematic",
        "Fantasy",
        "Cyberpunk",
        "Photorealistic",
        "Dreamy",
        "Mystical",
        "Minimalist",
        "Surreal",
    ],
    index=0,
)

# ---- Prompt Input ----
prompt = st.text_area(
    "💭 Enter your prompt idea:",
    st.session_state["enhanced_prompt"] or "A futuristic city at sunset",
    height=100,
)

col1, col2 = st.columns(2)

# ---- Enhance Prompt ----
with col1:
    if st.button("✨ Enhance Prompt with AI", use_container_width=True):
        with st.spinner(f"Enhancing your prompt in a {mood.lower()} style... ✨"):
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an expert AI prompt engineer. "
                                "Transform the user’s input into a rich, descriptive prompt for AI image generation. "
                                "Focus on detailed composition, lighting, realism, mood, and atmosphere."
                            ),
                        },
                        {
                            "role": "user",
                            "content": f"Rewrite this prompt in a {mood.lower()} style with vivid, cinematic detail:\n\n{prompt}",
                        },
                    ],
                    temperature=0.9,
                    max_tokens=180,
                )

                enhanced_prompt = response.choices[0].message.content.strip()
                st.session_state["enhanced_prompt"] = enhanced_prompt

                # Auto-fill enhanced prompt back into the text box
                st.experimental_rerun()

            except Exception as e:
                st.error(f"❌ Error enhancing prompt: {e}")

# ---- REST Image Generator (Multipart Form Data) ----
def generate_image(prompt: str):
    try:
        url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
        headers = {
            "Authorization": f"Bearer {STABILITY_API_KEY}",
            "Accept": "image/*",  # Required by API
        }
        files = {
            "none": (None, ""),  # Dummy field to satisfy multipart
        }
        data = {
            "prompt": prompt,
            "mode": "text-to-image",
            "output_format": "png",
            "aspect_ratio": "16:9",
        }

        response = requests.post(url, headers=headers, files=files, data=data)

        if response.status_code == 200:
            img = Image.open(io.BytesIO(response.content))
            return img
        else:
            st.error(f"⚠️ API Error {response.status_code}: {response.text}")
            return None

    except Exception as e:
        st.error(f"❌ Image generation failed: {e}")
        return None

# ---- Generate Image ----
with col2:
    if st.button("🎨 Generate Image", use_container_width=True):
        final_prompt = st.session_state["enhanced_prompt"] or prompt

        if not final_prompt.strip():
            st.warning("⚠️ Please enter or enhance a prompt first!")
        else:
            st.info("Generating your image... please wait ⏳")

            img = generate_image(final_prompt)
            if img:
                st.image(img, caption=final_prompt, use_column_width=True)
                buf = io.BytesIO()
                img.save(buf, format="PNG")
                st.download_button(
                    "📥 Download Image",
                    data=buf.getvalue(),
                    file_name="ai_generated_image.png",
                    mime="image/png",
                    use_container_width=True
                )

# ---- Footer ----
st.markdown(
    "<hr><p style='text-align:center;color:gray;'>✨ Powered by Stability AI × Groq ✨</p>",
    unsafe_allow_html=True,
)
