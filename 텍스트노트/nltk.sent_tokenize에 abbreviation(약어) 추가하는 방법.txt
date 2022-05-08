#----------------------------
# nltk.sent_tokenize에 abbreviation(약어) 추가하는 방법
#----------------------------

# nltk.sent_tokenize로 문장 나누기
nltk.sent_tokenize를 사용할 경우, punkt 모델을 활용하여 sentence tokenization을 진행하게 된다.
문제는 punkt 모델에 학습되어 있지않는 약어(Abbreviation) 정보가 문서에 포함되어 있을 경우 문장 나누기 기능에 오류가 발생한다.

다음은 그 해결 방법이다.
참조로 punkt는 기본적으로 "글자 전부가 대문자인 단어" 외에는 모두 소문자 단어로 치환하여 처리한다. 따라서 추가 정보를 등록할때, 약어가 전부 대문자가 아닌 경우 소문자로 치환해서 등록해주어야 한다.

# 튜닝된 Tokenizer를 통해 다시 Sentence 분리하기
import nltk

from nltk.data import load
tokenizer = load("tokenizers/punkt/english.pickle")
extra_abbreviations = [
    "RE","re","pat", "no", "nos","vol","jan","feb","mar","apr","jun",
    "jul","aug","sep","oct","nov","dec","eng","ser","ind","ed","pp",
    "e.g","al","T.E.N.S", "E.M.S","F.E","U.H.T.S.T","degree",
    "/gm","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
    "P","Q","R","S","T","U","V","W","X","Y","Z"]
tokenizer._params.abbrev_types.update(extra_abbreviations)

load_file=open("./input.txt","r")
save_file=open("./output.txt","w")
no_blank = False
while True:
    line = load_file.readline()
    if line == "":
        break
    if line.strip() == "":
        if no_blank:
            continue
        save_file.write(f"{line}")
    else:
        print(line)
        result_ = tokenizer.tokenize(line)
        print(result_)
        result  = [ f"{cur_line}\n" for cur_line in result_ ]
        for save_line in result:
            save_file.write(save_line)
