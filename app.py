import streamlit as st
from dotenv import load_dotenv
import os
import re
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt template
prompt = """
You are a YouTube video summarizer. You will take the transcript text
and summarize the video into important bullet points within 250 words.
Please summarize the following transcript:
"""

# Extract video ID from a YouTube URL
def get_video_id(youtube_url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(regex, youtube_url)
    return match.group(1) if match else None

# Get transcript using the latest `fetch()` method
def extract_transcript_details(youtube_url):
    try:
        video_id = get_video_id(youtube_url)
        if not video_id:
            return "❌ Invalid YouTube URL format."

        # Create API object and fetch transcript
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)  # returns FetchedTranscript object

        # Join all transcript snippets
        full_transcript = " ".join([snippet.text for snippet in transcript])
        return full_transcript

    except TranscriptsDisabled:
        return "❌ Transcripts are disabled for this video."
    except NoTranscriptFound:
        return "❌ No transcript found for this video."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Generate Gemini summary
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit app UI
st.title("🎥 YouTube Video to Detailed Notes Converter")
youtube_link = st.text_input("Paste YouTube Video URL:")

if youtube_link:
    video_id = get_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Summary"):
    with st.spinner("⏳ Fetching transcript and generating summary..."):
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text.startswith("❌"):
            st.error(transcript_text)
        else:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## 📝 Summary Notes:")
            st.write(summary)
