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

    file_name = input("Enter the name for the audio file (without the extension): ")
    file_path = f"{file_name}.mp3"

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(file_path)

    print(f"Text converted to speech and saved as {file_path}.")

    os.system(f"start {file_path}")

if __name__ == "__main__":
    text_to_speak = input("Enter the text you want to convert to speech: ")
    voice_choice = input("Choose a voice (woman or man): ").lower()

    convert_to_speech(text_to_speak, voice_choice)
