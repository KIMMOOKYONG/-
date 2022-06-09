# 참고
- https://wikidocs.net/15213
- (음성인식 및 음성 생성)https://davey.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%8C%EC%84%B1-%ED%85%8D%EC%8A%A4%ED%8A%B8-%EB%B3%80%ED%99%98-%EB%82%B4-%EB%A7%90-%EB%8C%80%EB%8B%B5-AI-%EB%A1%9C%EB%B4%87-%EB%A7%8C%EB%93%A4%EA%B8%B0-gTTs-SpeechRecognition-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC
- 

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

```python
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang="ko")
    filename = "voice.mp3"
    tts.save(filename)
    # 구글 코랩에서는 실행 안됨
    # playsound.playsound(filename)

speak("안녕하세요. 좋은 아침입니다.")

```
