import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# Function to convert text to speech
def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

# This function returns pydub's audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1-generate kripaya dhyan dijiye
    start = 0
    finish = 3000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from-city

    # 3-Generate se chalkar
    start = 7000
    finish = 11000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4-is via-city

    # 5-Generate ke raaste
    start = 10000
    finish = 12000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7-Generate ko jaane wali gaadi sankhya
    start = 11000
    finish = 13000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9-Generate kuch hi samay me plateform sankhya
    start = 13000
    finish = 15000
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11-Generate par aa rhi hai
    start = 15000
    finish = 17000
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")
def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2-Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4-Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6-Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8-Generate train no and name
        train_info = str(item['train_no']) + " " + item['train_name']
        textToSpeech(train_info, '8_hindi.mp3')

        # 10-Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]
        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
