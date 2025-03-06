import torch
import whisper
from pydub import AudioSegment
from pydub.utils import mediainfo
from faster_whisper import WhisperModel

# Choose Backend: "whisper" (default) or "faster-whisper"
USE_FASTER_WHISPER = True  # Set to False to use OpenAI Whisper

# Determine device: "mps" for Whisper, "cpu" for Faster-Whisper
whisper_device = "mps" if torch.backends.mps.is_available() else "cpu"
faster_whisper_device = "cpu"  # Faster-Whisper does NOT support MPS

# Function to check audio duration
def check_audio_duration(audio_file):
    info = mediainfo(audio_file)
    print(f"Audio Duration: {info['duration']} seconds")
    return float(info['duration'])

# Function to convert M4A to WAV
def convert_m4a_to_wav(m4a_file, wav_file):
    print("Converting M4A to WAV...")
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(wav_file, format="wav")
    print("Conversion complete.")
    return wav_file

# Function to transcribe audio using Faster-Whisper
def transcribe_with_faster_whisper(audio_file):
    print("Using Faster-Whisper (CPU mode)...")
    model = WhisperModel("large-v2", device=faster_whisper_device, compute_type="int8")  # int8 for speed

    segments, _ = model.transcribe(audio_file)

    transcript = ""
    print("\n--- Transcription Segments ---")
    for segment in segments:
        print(f"{segment.start:.2f}s - {segment.end:.2f}s: {segment.text}")
        transcript += segment.text + " "

    return transcript

# Function to transcribe audio using OpenAI Whisper
def transcribe_with_whisper(audio_file):
    print("Using OpenAI Whisper with MPS acceleration...")
    model = whisper.load_model("large-v2").to(whisper_device)

    result = model.transcribe(audio_file, temperature=0, logprob_threshold=-1.0, word_timestamps=True)

    transcript = result["text"]

    print("\n--- Transcription Segments ---")
    for segment in result["segments"]:
        print(f"{segment['start']}s - {segment['end']}s: {segment['text']}")

    return transcript

# Function to generate meeting notes from transcript
def generate_meeting_notes(transcript):
    notes = f"""
    **Meeting Notes:**
    
    **Key Discussion Points:**
    - {transcript[:500]}... (Summarized Key Points)
    
    **Decisions Made:**
    - Identify agreements and conclusions from discussion.

    **Action Items:**
    - Extract and assign tasks with deadlines.
    """
    return notes

# Main function
def main():
    input_m4a = "/Users/georgey/stt/stt.m4a"  # Change this to your actual file name
    output_wav = "converted_meeting.wav"

    # Step 1: Check original M4A duration
    print("Checking original M4A audio duration...")
    original_duration = check_audio_duration(input_m4a)

    # Step 2: Convert to WAV
    convert_m4a_to_wav(input_m4a, output_wav)

    # Step 3: Check converted WAV duration
    print("Checking converted WAV audio duration...")
    converted_duration = check_audio_duration(output_wav)

    # Step 4: Verify conversion success
    if abs(original_duration - converted_duration) > 1:  # Allow slight variation
        print("⚠️ Warning: Converted audio duration does not match original. Check the M4A file!")

    # Step 5: Transcribe audio using selected method
    if USE_FASTER_WHISPER:
        transcript = transcribe_with_faster_whisper(output_wav)
    else:
        transcript = transcribe_with_whisper(output_wav)

    # Step 6: Generate meeting notes
    print("Generating meeting notes...")
    meeting_notes = generate_meeting_notes(transcript)

    # Step 7: Print and save notes
    print("\n--- Meeting Notes ---\n")
    print(meeting_notes)

    with open("meeting_notes.txt", "w") as file:
        file.write(meeting_notes)

    print("\n✅ Meeting notes saved to 'meeting_notes.txt'.")

if __name__ == "__main__":
    main()
