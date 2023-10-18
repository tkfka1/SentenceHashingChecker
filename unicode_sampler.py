import random

def random_unicode_string(length):
    unicode_ranges = [
        (0x0020, 0x007F),  # Basic Latin
        (0x0370, 0x03FF),  # Greek and Coptic
        (0x0400, 0x04FF),  # Cyrillic
        (0x4E00, 0x9FFF),  # CJK Ideographs
        (0xAC00, 0xD7A3),  # Hangul Syllables (완성형 한글)
    ]

    result = []

    for _ in range(length):
        ## 유니코드 범위 랜덤선택
        range_choice = random.choice(unicode_ranges)
        ## 선택한 유니코드 시작과 끝범위 안에서 랜덤선택
        code_point = random.randint(range_choice[0], range_choice[1])
        # result.append(code_point)
        result.append(chr(code_point))

    # return result
    return ''.join(result)

## 문자,문장 개수
n = 100
s = 10000

## 테스트 출력
# print(random_unicode_string(n))

## 문자열 생성
random_string = random_unicode_string(n)

## 파일에 저장
with open('output.txt', 'w', encoding='utf-8') as file:
    for _ in range(s):
        random_string = random_unicode_string(n)
        file.write(random_string + '\n')

print(f"{s} lines of random unicode strings have been saved to output.txt.")