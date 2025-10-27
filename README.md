# AI Image Generator

A powerful Streamlit web application that generates AI images using Stability AI's SDXL model with intelligent prompt enhancement powered by Groq's Llama model.

## Features

### 🎨 AI-Powered Image Generation
- **Stability AI Integration**: Uses Stability AI's SDXL (Stable Diffusion XL) model for high-quality image generation
- **High Resolution**: Generates images at 2536x896 resolution
- **Advanced Parameters**: 
  - 50 inference steps for detailed results
  - CFG Scale of 8.0 for balanced creativity and prompt adherence

### 🎭 Mood Selection
Choose from 6 distinct artistic moods to enhance your images:
- **Cinematic**: Dramatic lighting, epic scenes
- **Fantasy**: Magical, ethereal elements
- **Cyberpunk**: Neon lights, futuristic urban aesthetic
- **Minimalist**: Clean, simple compositions
- **Vintage**: Retro, nostalgic atmosphere
- **Abstract**: Creative, non-representational art

### 🤖 Intelligent Prompt Enhancement
- **Groq AI Integration**: Uses Groq's Llama 3.3 70B model for prompt enhancement
- Automatically enriches user prompts with relevant details and artistic elements
- Preserves user intent while adding professional descriptors

### 💾 Download Capability
- Download generated images directly from the app
- Images saved in PNG format

## Prerequisites

- Python 3.10 or higher
- API Keys:
  - **Stability AI API Key**: Get from [platform.stability.ai](https://platform.stability.ai/)
  - **Groq API Key**: Get from [console.groq.com](https://console.groq.com/)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Inevitable07H/Ai-image-gen.git
cd Ai-image-gen
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

#### Option A: Using Streamlit Secrets (Recommended for Deployment)
Create a `.streamlit/secrets.toml` file:
```toml
STABILITY_API_KEY = "your_stability_api_key_here"
GROQ_API_KEY = "your_groq_api_key_here"
```

#### Option B: Using Environment Variables
```bash
# On Windows:
set STABILITY_API_KEY=your_stability_api_key_here
set GROQ_API_KEY=your_groq_api_key_here

# On macOS/Linux:
export STABILITY_API_KEY=your_stability_api_key_here
export GROQ_API_KEY=your_groq_api_key_here
```

## Usage

### Run Locally
```bash
streamlit run image_generator_new.py
```

The app will open in your default web browser at `http://localhost:8501`

### How to Use the App

1. **Enter API Keys** (if not configured via secrets/environment):
   - Enter your Stability AI API key in the sidebar
   - Enter your Groq API key in the sidebar

2. **Select a Mood**:
   - Choose from 6 available mood presets
   - Each mood adds unique artistic elements to your images

3. **Enter Your Prompt**:
   - Describe the image you want to generate
   - The AI will automatically enhance your prompt based on the selected mood

4. **Generate**:
   - Click the "Generate Image" button
   - Wait for the AI to process and generate your image

5. **Download**:
   - Once generated, download your image using the download button

## Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select `image_generator_new.py` as the main file
5. Add your API keys in the Secrets section:
   ```toml
   STABILITY_API_KEY = "your_key_here"
   GROQ_API_KEY = "your_key_here"
   ```
6. Deploy!

### Hugging Face Spaces

1. Create a new Space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Select **Streamlit** as the SDK
3. Upload your files or connect your GitHub repo
4. Add secrets in Settings > Repository secrets:
   - `STABILITY_API_KEY`
   - `GROQ_API_KEY`
5. The app will automatically deploy

### Other Platforms

- **Railway.app**: Connect GitHub repo and add environment variables
- **DigitalOcean App Platform**: Deploy from GitHub with environment variables
- **Google Cloud Run**: Containerize and deploy with secrets
- **AWS App Runner**: Deploy from GitHub with environment variables

## Technical Details

### Models Used
- **Image Generation**: Stability AI SDXL (Stable Diffusion XL)
- **Prompt Enhancement**: Groq Llama 3.3 70B Versatile

### Generation Parameters
- **Resolution**: 2536 x 896 pixels
- **Steps**: 50 (higher quality, longer generation time)
- **CFG Scale**: 8.0 (balanced between creativity and prompt adherence)

### Dependencies
Key libraries used:
- `streamlit`: Web application framework
- `requests`: API communication
- `Pillow`: Image processing
- `groq`: Groq API client

## Troubleshooting

### Common Issues

**"Invalid API Key" Error**
- Verify your API keys are correct
- Check that keys are properly set in secrets or environment variables

**Image Generation Fails**
- Ensure you have sufficient API credits
- Check your internet connection
- Verify the Stability AI API is operational

**Prompt Enhancement Doesn't Work**
- Verify Groq API key is valid
- Check Groq API rate limits

**Slow Generation**
- This is normal - high-quality images take time
- 50 steps can take 30-60 seconds depending on API load

## Credits

- **Stability AI**: For the SDXL image generation model
- **Groq**: For fast LLM inference and prompt enhancement
- **Streamlit**: For the web application framework

## License

MIT License - Feel free to use and modify as needed.

## Support

For issues or questions:
- Open an issue on GitHub
- Check the Stability AI and Groq documentation
- Review Streamlit documentation for deployment help

---

**Note**: This application requires active API keys with sufficient credits. Free tiers may have rate limits.
