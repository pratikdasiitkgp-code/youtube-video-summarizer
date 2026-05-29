# 🎥 YouTube Video Summarizer using OpenAI Whisper & GPT

## 📌 Overview

This project is an AI-powered YouTube Video Summarizer built with Streamlit, OpenAI Whisper, and GPT-4.1-mini.

The application downloads audio from a YouTube video, generates a transcript using OpenAI Whisper Speech-to-Text, and produces a concise summary using OpenAI GPT.

Unlike transcript-based approaches, this solution works even when YouTube transcripts are unavailable.

---

## 🚀 Features

* Summarize YouTube videos from a URL
* Download audio using yt-dlp
* Generate transcripts using OpenAI Whisper
* Create AI-generated summaries using GPT-4.1-mini
* Streamlit-based interactive UI
* Handles videos without YouTube captions
* Error handling for invalid videos

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI API
* Whisper Speech-to-Text
* GPT-4.1-mini
* yt-dlp
* FFmpeg

---

## 📂 Project Structure

youtube-video-summarizer/

├── app.py

├── audio_extractor.py

├── transcript.py

├── summarizer.py

├── requirements.txt

├── .env

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/youtube-video-summarizer.git

cd youtube-video-summarizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install FFmpeg

Download and install FFmpeg.

Add the FFmpeg bin folder to your system PATH.

Verify installation:

```bash
ffmpeg -version
```

### Configure OpenAI API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Workflow

1. Enter YouTube URL
2. Audio is downloaded using yt-dlp
3. Audio is transcribed using OpenAI Whisper
4. GPT generates a concise summary
5. Summary is displayed in Streamlit

---

## 💡 Future Enhancements

* PDF summary export
* Multi-language support
* Chapter-wise summaries
* Video thumbnail preview
* Timestamp-based summaries
* Long video chunking
* Deploy on Streamlit Cloud

---

## 🎯 Skills Demonstrated

* Generative AI
* Prompt Engineering
* OpenAI API Integration
* Speech-to-Text Systems
* LLM Applications
* Streamlit Deployment
* Python Development

---

## 👨‍💻 Author

Pratik Das

Data Science | AI/ML | Generative AI
