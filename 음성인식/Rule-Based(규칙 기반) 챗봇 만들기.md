# Rule-Based(규칙 기반) 챗봇 만들기
# Rule-Based 설계하기
- Intent(의도)
- Entity(개체)
- 대화의 규칙을 직접 설계해서 어떤 말이 만들어진 규칙에 해당한다면 답변하는 방식이다.

# 테스트 데이터
![image](https://user-images.githubusercontent.com/102650331/174028082-3d41a9de-435e-4446-900f-71eb13963ea9.png)

- request: 예문(rule을 만들기 위한 예문)
- rule: request를 참조하는 레퍼런스, 규칙
- response: 챗봇이 답변할 내용

# 1차 코드
```python
# pip install openpyxl

import pandas as pd

# 데이터 로딩
chatbot_data = pd.read_excel("chatbot_data.xlsx")
# print(chatbot_data)

# rule 저장
# rule의 데이터를 split하여 list형태로 변환 후, index값과 함께 dictionary 형태로 저장
chat_dic = {}
row = 0

for rule in chatbot_data["rule"]:
    chat_dic[row] = rule.split("|")
    row += 1

# print(chat_dic)

# 챗봇 함수
# 느그 아부지 뭐하시노?
def chat(request):
    for k, v in chat_dic.items():
        chat_flag = False
        # request에 rule에 있는 단어가 포함되어 있는지 확인한다.
        for word in v:
            print(word)
            if word in request:
                chat_flag = True
            else:
                chat_flag = False
                break

        if chat_flag:
            return chatbot_data["response"][k]

    return "무슨 말인지 모르겠어요"

# 채팅
while True:
    req = input("대화를 입력해보세요.: ")
    if req == "exit":
        break
    else:
        print("jarvis: " + chat(req))

```

```python
# pip install openpyxl
# https://needjarvis.tistory.com/639

import pandas as pd

# 데이터 로딩
chatbot_data = pd.read_excel("chatbot_data.xlsx")
# print(chatbot_data)

# rule 저장
# rule의 데이터를 split하여 list형태로 변환 후, index값과 함께 dictionary 형태로 저장
chat_dic = {}
row = 0

for rule in chatbot_data["rule"]:
    chat_dic[row] = rule.split("|")
    row += 1

# print(chat_dic)

# 챗봇 함수
# 느그 아부지 뭐하시노?
def chat(request):
    for k, v in chat_dic.items():
        index = -1
        for word in v:
            try:
                if index == -1:
                    index = request.index(word)
                else:
                    # 이전 index 값은 현재 index값보다 이전이어야 한다.
                    if index < request.index(word, index):
                        index = request.index(word, index)
                    else:
                        # index 값이 이상할 경우 과감하게 break를 한다.
                        index = -1
                        break
            except ValueError:
                index = -1
                break

        if index > -1:
            return chatbot_data["response"][k]
    return "무슨 말인지 모르겠어요."


# 채팅
while True:
    req = input("대화를 입력해보세요.: ")
    if req == "exit":
        break
    else:
        print("jarvis: " + chat(req))


```
