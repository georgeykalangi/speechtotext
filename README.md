# Speech-to-Text Meeting Notes Generator

## Overview
This project converts **M4A audio files** into **transcripts** and **structured meeting notes** using **Whisper AI** and **Faster-Whisper**.  
It supports **Apple Silicon GPU (MPS) acceleration** for Mac Mini M4 and allows easy **switching between Whisper and Faster-Whisper**.

---

## ⚡ Features
Converts `.m4a` audio files to `.wav` format  
Transcribes speech using **Whisper AI or Faster-Whisper**  
Supports **Apple Silicon GPU (MPS) acceleration**  
Generates **structured meeting notes**  
Easy-to-read meeting summaries with **key discussion points, decisions, and action items**  

---

## Prerequisites
Before running the script, make sure you have the following installed:

### **1. Install Python (if not already installed)**
- Check Python version:
  ```bash
  python --version

Install Required Dependencies
Run the following command to install the necessary libraries:

bash
Copy
Edit
pip install torch torchvision torchaudio whisper faster-whisper pydub
3. Install FFmpeg (Required for Audio Processing)
Mac (Homebrew)
bash
Copy
Edit
brew install ffmpeg
Linux (Debian/Ubuntu)
bash
Copy
Edit
sudo apt update && sudo apt install ffmpeg
Windows
Download FFmpeg from ffmpeg.org
Add FFmpeg to your system PATH.
How to Use
1. Place your .m4a file in the project folder
Rename your audio file to meeting.m4a (or update the script with your file name).

2. Run the Script
Run the Python script to generate transcripts and meeting notes:

bash
Copy
Edit
python stt.py
3. View Meeting Notes
After the script finishes, it will generate a file:
meeting_notes.txt
Open the file to view structured meeting notes.
⚙️ Configuration
Switching Between Whisper & Faster-Whisper
Whisper (Default)

Uses Apple Silicon GPU acceleration (MPS).
More accurate but slower.
Faster-Whisper

Runs on CPU (since MPS is not supported).
5-10x faster, but slightly less accurate.
To switch between them, update the stt.py script:

python
Copy
Edit
USE_FASTER_WHISPER = True  # Set to False to use OpenAI Whisper
Troubleshooting
Issue: "unsupported device mps" in Faster-Whisper
Fix: Faster-Whisper does not support mps. The script automatically uses cpu instead.

Issue: Script is too slow
Fix: Use Faster-Whisper (USE_FASTER_WHISPER = True).

Issue: No transcription output
Fix: Ensure FFmpeg is installed:

📜 License
This project is licensed under the MIT License.
