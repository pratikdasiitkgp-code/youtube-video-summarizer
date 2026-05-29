import streamlit as st
import os

from audio_extractor import download_audio
from transcript import get_transcript
from summarizer import summarize_text

st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon="🎥",
    layout="centered"
)

st.title("🎥 YouTube Video Summarizer")

st.write(
    "Enter a YouTube URL to generate a transcript and AI-powered summary."
)

url = st.text_input("Enter YouTube URL")

if st.button("Generate Summary"):

    if not url:
        st.warning("Please enter a YouTube URL.")
        st.stop()

    try:

        with st.spinner("Downloading Audio..."):
            audio_file = download_audio(url)

        if not os.path.exists(audio_file):
            st.error("Audio download failed.")
            st.stop()

        file_size = round(
            os.path.getsize(audio_file) / (1024 * 1024),
            2
        )

        st.info(f"Downloaded Audio Size: {file_size} MB")

        with st.spinner("Generating Transcript using Whisper..."):
            transcript = get_transcript(audio_file)

        st.success("Transcript Generated Successfully!")

        with st.expander("View Transcript"):
            st.write(transcript)

        with st.spinner("Generating AI Summary..."):
            summary = summarize_text(transcript)

        st.success("Summary Generated Successfully!")

        st.subheader("📌 Summary")
        st.write(summary)

    except Exception as e:

        error_msg = str(e)

        if "403" in error_msg:
            st.error(
                "YouTube blocked access to this video. "
                "Try another public YouTube video."
            )

        elif "413" in error_msg:
            st.error(
                "Audio file is too large. "
                "Please try a shorter video."
            )

        else:
            st.error(f"Error: {error_msg}")