from flask import Flask, request, send_file
from gtts import gTTS

def generate_speech():
    msg = input("Your Message: ")
    lang = "en"

    tts = gTTS(text=msg, lang=lang, slow=False, tld='com.au')
    file_name = "output.mp3"
    tts.save(file_name)

    return send_file(file_name, as_attachment=True)