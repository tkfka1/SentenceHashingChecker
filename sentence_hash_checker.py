import hashlib

## SHA-256 해시 함수변환 함수
def get_hash(sentence):
    return hashlib.sha256(sentence.encode()).hexdigest()

## 해시 테이블 딕셔너리
hash_table = {}

## 중복된 문장 저장 리스트
duplicated_sentences = []

## 문장 추가 및 중복 확인 함수
def add_sentence(sentence):
    hash_value = get_hash(sentence)

    if hash_value not in hash_table:
        hash_table[hash_value] = [sentence]
    else:
        if sentence in hash_table[hash_value]:
            # print("중복된 문장:", sentence)
            duplicated_sentences.append(sentence)
            return
        else:
            hash_table[hash_value].append(sentence)

## 테스트
sentences = ["안녕하세요", "반갑습니다", "안녕하세요", "오늘은 좋은 날씨입니다"]
for s in sentences:
   add_sentence(s)

## output.txt 파일에서 테스트
with open('output.txt', 'r', encoding='utf-8') as file:
    for line in file:
        add_sentence(line.rstrip())

print("해시 테이블:", hash_table)
print("중복된 문장 리스트:", duplicated_sentences)