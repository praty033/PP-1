# ProofPixels 🕵️

An AI-powered platform that detects fake news and AI-generated images,
with explainable predictions, saved history, and downloadable PDF reports.

## Features
- Fake news detection (Hugging Face transformer model)
- AI-generated image detection
- Explainable AI (shows which words influenced each decision)
- SQLite-backed history
- PDF report generation
- Interactive Streamlit dashboard

## Tech Stack
Python, Streamlit, Hugging Face Transformers, PyTorch, SQLite, ReportLab, Plotly

## Live Demo
[your-app-name.streamlit.app](https://your-app-name.streamlit.app)

## Run Locally
\`\`\`bash
git clone https://github.com/praty033/PP-1.git
cd PP-1
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
\`\`\`