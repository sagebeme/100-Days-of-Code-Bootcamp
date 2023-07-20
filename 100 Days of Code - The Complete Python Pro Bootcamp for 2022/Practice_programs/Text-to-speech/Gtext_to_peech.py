#!/usr/bin/env python3


from gtts import gTTS
import os

def convert_to_speech(text, voice_type):
    if voice_type == 'woman':
        language = 'en'
    elif voice_type == 'man':
        language = 'en-us'
    else:
        print("Invalid voice choice. Please choose 'woman' or 'man'.")
        return

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

if __name__ == "__main__":
    text_to_speak = input("Enter the text you want to convert to speech: ")
    voice_choice = input("Choose a voice (woman or man): ").lower()

    convert_to_speech(text_to_speak, voice_choice)
