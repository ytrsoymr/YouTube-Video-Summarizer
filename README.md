# YouTube Video Summarizer

This Streamlit app summarizes YouTube videos into concise bullet-point notes using Google Gemini AI.

## Features

- Paste a YouTube video URL and get a transcript summary.
- Uses [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) to fetch transcripts.
- Summarizes content with [Google Gemini](https://ai.google.dev/).
- Clean, simple Streamlit interface.

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   Or use [pyproject.toml](e:/youtube-video-summarizer/pyproject.toml) with:
   ```sh
   pip install .
   ```

3. **Set up your API key**
   - Create a `.env` file with:
     ```
     GOOGLE_API_KEY="your-google-api-key"
     ```

## Usage

Run the app with:
```sh
streamlit run app.py
```

Paste a YouTube video URL and click "Get Summary" to see the notes.

## Project Structure

- [`app.py`](e:/youtube-video-summarizer/app.py): Main Streamlit app.
- [`pyproject.toml`](e:/youtube-video-summarizer/pyproject.toml): Dependency management.
- `.env`: Stores your Google API key.
