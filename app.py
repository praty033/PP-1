import streamlit as st
import pandas as pd
import plotly.express as px

from fake_news import analyze_news
from image_detector import analyze_image
from explainability import explain_news
from database import init_db, save_result, get_history
from report_generator import generate_report
from utils import ensure_folder

st.set_page_config(page_title="ProofPixels", page_icon="🕵️")
init_db()
ensure_folder("uploads")
ensure_folder("reports")

st.sidebar.title("ProofPixels")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Fake News Detection", "Image Detection", "Dashboard", "About"]
)

if page == "Home":
    st.title("🕵️ ProofPixels")
    st.write(
        "An AI-powered platform that detects fake news articles and "
        "AI-generated images, with explainable predictions, saved history, "
        "and downloadable PDF reports."
    )

elif page == "Fake News Detection":
    st.title("📰 Fake News Detection")
    news_text = st.text_area("Paste a news article, headline, or social media post:")

    if st.button("Analyze") and news_text.strip():
        with st.spinner("Analyzing..."):
            prediction, score = analyze_news(news_text)

        st.subheader(f"Result: {prediction}")
        st.write(f"Confidence: {score:.2%}")

        with st.spinner("Figuring out why..."):
            top_words = explain_news(news_text)

        st.write("Words that influenced this decision most:")
        for word, impact in top_words:
            st.write(f"- **{word}** (impact: {impact:.3f})")

        save_result("news", news_text, prediction, score)

        path = generate_report("News", news_text, prediction, score)
        with open(path, "rb") as f:
            st.download_button("Download PDF Report", f, file_name="report.pdf")

elif page == "Image Detection":
    st.title("🖼️ AI Image Detection")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, width=300)

        temp_path = f"uploads/{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                prediction, score = analyze_image(temp_path)

            st.subheader(f"Result: {prediction}")
            st.write(f"Confidence: {score:.2%}")

            save_result("image", uploaded_file.name, prediction, score)

            path = generate_report("Image", uploaded_file.name, prediction, score)
            with open(path, "rb") as f:
                st.download_button("Download PDF Report", f, file_name="report.pdf")

elif page == "Dashboard":
    st.title("📊 Dashboard")
    history = get_history()

    if history:
        df = pd.DataFrame(
            history,
            columns=["Type", "Content", "Prediction", "Score", "Timestamp"]
        )
        st.metric("Total Analyses", len(df))

        fig = px.pie(df, names="Prediction", title="Fake vs Real Breakdown")
        st.plotly_chart(fig)

        st.dataframe(df)
    else:
        st.write("No analyses yet — go run a check first!")

elif page == "About":
    st.title("About ProofPixels")
    st.write(
        "Built using Streamlit, Hugging Face Transformers, PyTorch, "
        "SQLite, ReportLab, and Plotly."
    )