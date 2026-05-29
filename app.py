import streamlit as st
import os

from audio_extractor import download_audio
from transcript import get_transcript
from summarizer import summarize_text

st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon="🎥"
)

st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Enter YouTube URL")

if st.button("Generate Summary"):

    try:

        with st.spinner("Downloading Audio..."):
            audio_file = download_audio(url)

        file_size = round(
            os.path.getsize(audio_file) / (1024 * 1024),
            2
        )

        st.info(f"Audio Size: {file_size} MB")

        with st.spinner("Generating Transcript..."):
            transcript = get_transcript(audio_file)

        with st.spinner("Generating Summary..."):
            summary = summarize_text(transcript)

        st.success("Summary Generated Successfully!")

        st.subheader("Summary")
        st.write(summary)

    except Exception as e:

        st.error(f"Error: {str(e)}")