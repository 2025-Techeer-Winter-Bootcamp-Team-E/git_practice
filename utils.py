"""
공통 유틸리티 함수들
주의: 이 파일은 모든 팀원이 수정할 수 있어 충돌이 발생할 수 있습니다!
"""


def print_header(title):
    """헤더 출력"""
    print("=" * 50)
    print(f"  {title}")
    print("=" * 50)


def print_separator():
    """구분선 출력"""
    print("-" * 50)


def greet(name):
    """인사말 반환"""
    return f"안녕하세요, {name}님!"


def calculate_sum(numbers):
    """숫자 리스트의 합계 계산"""
    return sum(numbers)


def calculate_average(numbers):
    """숫자 리스트의 평균 계산"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# ========================================
# 아래에 팀원들이 추가 함수를 작성하세요
# (충돌 연습용)
# ========================================

# 팀원1 추가 함수


# 팀원2 추가 함수


# 팀원3 추가 함수


# 팀원4 추가 함수
