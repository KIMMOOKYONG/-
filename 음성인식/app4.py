import speech_recognition as sr 
import numpy as np
import pandas as pd
import jellyfish
from gtts import gTTS
from playsound import playsound

df = pd.read_csv("https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv")

# create the recognizer 
r = sr.Recognizer() 

# define the microphone 
mic = sr.Microphone(device_index=0) 

i = 0
while True:
    i = i + 1

    print("Listening...")

    try:
        # record your speech 
        with mic as source: 
            audio = r.listen(source) 

        # speech recognition 
        # 한글 음성 인식 설정, language="ko"
        result = r.recognize_google(audio, language="ko")

        if "마무리" in result:
            break

        idx = df.loc[:,"Q"].apply(lambda x: jellyfish.jaro_distance(str(x),result)).sort_values(ascending=False).index[0]

        s = gTTS(df.loc[idx,"A"], lang="ko")
        s.save(f"sample{i}.mp3")
        playsound(f"sample{i}.mp3")
    except Exception as e:
        pass