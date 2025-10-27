# AI Image Generator

A Streamlit web app that generates images using Stable Diffusion.

## Deployment Options

### 1. Streamlit Cloud (Recommended)
- Go to [share.streamlit.io](https://share.streamlit.io)
- Connect your GitHub repository
- Select Advanced Settings:
  - Set Memory to at least 8GB
  - Python version: 3.10+
  - Add secrets if needed

### 2. Hugging Face Spaces
- Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces)
- Choose Streamlit as the SDK
- Set hardware to CPU (16GB) or GPU

### 3. Self-hosted Options
- Railway.app
- DigitalOcean App Platform
- Google Cloud Run
- AWS App Runner

## Local Development
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run image_generator.py
```

## Hardware Requirements
- Minimum 8GB RAM
- GPU optional but recommended
- Storage: ~5GB for model weights

## Environment Variables
- `TORCH_DEVICE`: Set to 'cpu' or 'cuda' (default: 'cpu')
- `MODEL_ID`: Stable Diffusion model ID (default: 'CompVis/stable-diffusion-v1-4')