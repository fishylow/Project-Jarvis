from modules.gpt import *
from modules.tts import *

def prompt_keyword_check(latest_transcription):
    # Detect if "Jarvis" is in the transcription
    if "Jarvis" in latest_transcription:
        # Find the index of the keyword "Jarvis" and everything after it
        jarvis_index = latest_transcription.index("Jarvis")
        prompt = latest_transcription[jarvis_index+7:]
        print("Prompt detected:", prompt)
        
        # Send the prompt to GPT-4 and wait for the response
        gpt_response = run_conversation(prompt)
        gpt_message = gpt_response.choices[0].message.content

        #print message
        print("[", gpt_response.usage.total_tokens, "]", "\033[32mJarvis Response:", gpt_message, "\033[0m")
        engine.say(gpt_message)
        engine.runAndWait()
        return 0
    return 0