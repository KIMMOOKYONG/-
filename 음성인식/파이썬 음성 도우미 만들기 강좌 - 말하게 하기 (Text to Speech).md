# 패키지 설치
```
!pip install SpeechRecognition

```
![image](https://user-images.githubusercontent.com/102650331/172747415-a4148621-abb7-47e3-8d2d-4cca1ce9fc64.png)

```
!pip install gTTS

```

```
!pip install playsound

```

```
!apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
!pip install pyAudio

```

# 코드
```python
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("hello shop2word")

```
