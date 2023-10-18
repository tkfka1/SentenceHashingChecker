import mysql.connector
import hashlib

# 데이터베이스 연결
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sentenceDB"
)

cursor = conn.cursor()

## 해시 변환 함수
def get_hash(sentence):
    return hashlib.sha256(sentence.encode()).hexdigest()

# 데이터베이스 삽입 및 중복 확인 함수
def add_sentence(sentence):
    hash_value = get_hash(sentence)
    try:
        cursor.execute("INSERT INTO sentences (hash_value, sentence) VALUES (%s, %s)", (hash_value, sentence))
        conn.commit()
    except mysql.connector.IntegrityError:  # 중복된 해시 값이 있다면
        cursor.execute("UPDATE sentences SET duplicate_count = duplicate_count + 1 WHERE hash_value = %s", (hash_value,))
        conn.commit()

# 테스트
sentences = ["안녕하세요", "반갑습니다", "안녕하세요", "오늘은 좋은 날씨입니다"]
for s in sentences:
    add_sentence(s)

cursor.close()
conn.close()