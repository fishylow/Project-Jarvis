import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) #remove stupid futurewarning of whisper
import whisper
import sounddevice as sd
import numpy as np
import webrtcvad
import queue

from modules.prompts import *

# Load the Whisper model
model = whisper.load_model("medium.en")


# Initialize variables to store the latest transcription and prompt
latest_transcription = None
prompt = None

# Set recording parameters
fs = 16000  # Sample rate (16kHz)
block_duration = 0.03  # Duration of a single audio block in seconds (30ms)
max_record_time = 30
max_blocks = int(max_record_time / block_duration)
vad = webrtcvad.Vad()
vad.set_mode(3)  # Set VAD sensitivity: 0 (aggressive) to 3 (lenient)

# Create a queue to hold recorded audio blocks
audio_queue = queue.Queue()

# Function to record audio in chunks and use VAD to detect speech
def callback(indata, frames, time, status):
    if status:
        print(f"Recording status: {status}")
    
    # Convert audio to mono
    audio_chunk = indata[:, 0]
    
    # Convert the audio chunk to 16-bit PCM format for VAD
    pcm_audio = (audio_chunk * 32767).astype(np.int16).tobytes()
    
    # Check if speech is detected in the chunk
    if vad.is_speech(pcm_audio, fs):
        audio_queue.put(audio_chunk)  # Add chunk to queue if speech is detected


# Function to record and transcribe audio
def record_and_transcribe():
    global latest_transcription, prompt
    audio_data = []
    block_count = 0

    # Start recording in callback mode
    with sd.InputStream(samplerate=fs, channels=1, blocksize=int(fs * block_duration), callback=callback):
        print("Start speaking...")
        
        # Continue recording until silence is detected (i.e., no speech for a while)
        while True:
            try:
                chunk = audio_queue.get(timeout=1)
                audio_data.extend(chunk)
                block_count += 1

                if block_count >= max_blocks:
                    print("Reached 30-second limit.")
                    break
                
            except queue.Empty:
                if len(audio_data) > 0:
                    print("Transcribing...")
                    # Convert recorded audio data into a numpy array
                    audio_array = np.array(audio_data, dtype=np.float32)

                    # Use Whisper to transcribe the recorded audio
                    result = model.transcribe(audio_array, fp16=False)
                    transcript = result['text'].strip()  # Clean up leading/trailing spaces
                    
                    # Check if the transcription is not empty before saving it
                    if transcript:
                        latest_transcription = transcript
                        print("Latest Transcription:", latest_transcription)     
                        prompt_keyword_check(latest_transcription)
                        break
                    else:
                        print("Empty transcription, skipping.")
                    
                    break  # Stop recording after transcribing the speech

# Main loop to continuously detect speech and transcribe
def main():
    try:
        while True:
            record_and_transcribe()
    except KeyboardInterrupt:
        print("Transcription stopped.")

        
if __name__ == "__main__":
    main()
