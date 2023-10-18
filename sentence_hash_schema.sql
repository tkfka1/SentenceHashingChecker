-- 데이터베이스 생성
CREATE DATABASE sentenceDB;

-- 데이터베이스 사용
USE sentenceDB;

-- 테이블 생성
CREATE TABLE sentences (
    hash_value CHAR(64) PRIMARY KEY,  -- SHA-256 해시 값
    sentence TEXT NOT NULL,
    duplicate_count INT DEFAULT 1
);

-- 문장 저장 (이 부분은 실행 예시이므로 실제로 SQL 파일에서는 실행하지 않음)
-- REPLACE INTO는 중복 시 업데이트, 아니면 삽입을 수행합니다.
REPLACE INTO sentences (hash_value, sentence) VALUES (SHA256('문장'), '문장');

-- 중복된 문장 찾기
SELECT sentence, duplicate_count
FROM sentences
WHERE duplicate_count > 1;
