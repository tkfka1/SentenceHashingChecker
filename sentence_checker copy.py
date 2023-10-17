## 문장 저장 딕셔너리
sentences = {}

## 중복된 문장 저장 리스트
duplicated_sentences = []

## 문장 추가 및 중복 확인 함수
def add_sentence(sentence):
    if sentences.get(sentence):
        sentences[sentence] += 1
        duplicated_sentences.append(sentence)
    else:
        sentences[sentence] = 1


## 테스트
# test_sentences = ["안녕하세요", "반갑습니다", "안녕하세요", "오늘은 좋은 날씨입니다"]
# for s in test_sentences:
#    add_sentence(s)

## output.txt 파일에서 테스트
with open("output.txt", "r", encoding="utf-8") as file:
    for line in file:
        add_sentence(line.rstrip())  # rstrip()으로 줄바꿈 문자 제거 후 추가


print("문장 딕셔너리:", sentences)
print("중복문장 리스트:", duplicated_sentences)