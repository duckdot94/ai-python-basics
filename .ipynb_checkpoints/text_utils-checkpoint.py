# 모듈로 사용할 코드 (text_utils.py로 저장 가능)
# 여기서는 함수만 정의

def clean_text(text):
    """텍스트 정리: 공백 제거, 소문자 변환"""
    return text.strip().lower()

def count_words(text):
    """단어 수 세기"""
    return len(text.split())

def extract_keywords(text, min_length=2):
    """최소 길이 이상의 단어 추출"""
    words = text.lower().split()
    return [w for w in words if len(w) >= min_length]