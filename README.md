# Git 협업 연습 프로젝트

4명의 팀원이 함께 Git 협업을 연습하기 위한 Python 프로젝트입니다.

## 프로젝트 구조

```
git_proctice/
├── main.py          # 메인 실행 파일
├── utils.py         # 공통 유틸리티 (충돌 연습용)
├── team/
│   ├── __init__.py
│   ├── member1.py   # 팀원1 담당
│   ├── member2.py   # 팀원2 담당
│   ├── member3.py   # 팀원3 담당
│   └── member4.py   # 팀원4 담당
└── README.md
```

## 실행 방법

```bash
python main.py
```

---

## 협업 연습 시나리오

### 시나리오 1: 기본 워크플로우 (각자 파일 수정)

각 팀원이 자신의 파일만 수정하여 충돌 없이 협업하는 연습

1. 저장소 클론
   ```bash
   git clone <저장소 URL>
   cd git_proctice
   ```

2. 자신의 파일 수정 (예: 팀원1은 `team/member1.py`)
   - NAME, ROLE, HOBBY 수정
   - my_function() 구현

3. 커밋 & 푸시
   ```bash
   git add team/member1.py
   git commit -m "팀원1: 자기소개 및 기능 구현"
   git push
   ```

---

### 시나리오 2: 브랜치 사용하기

Feature Branch 워크플로우 연습

1. 새 브랜치 생성
   ```bash
   git checkout -b feature/member1-update
   ```

2. 파일 수정 후 커밋
   ```bash
   git add .
   git commit -m "feat: 팀원1 기능 추가"
   ```

3. 원격에 브랜치 푸시
   ```bash
   git push -u origin feature/member1-update
   ```

4. GitHub에서 Pull Request 생성

5. 코드 리뷰 후 main에 머지

---

### 시나리오 3: 충돌 해결 연습

`utils.py` 파일을 동시에 수정하여 충돌 상황 만들기

**팀원1:**
```python
# utils.py에 추가
def member1_util():
    return "팀원1의 유틸 함수"
```

**팀원2:**
```python
# utils.py의 같은 위치에 추가
def member2_util():
    return "팀원2의 유틸 함수"
```

**충돌 해결 방법:**
```bash
git pull origin main
# 충돌 발생!

# 파일 열어서 충돌 마커 확인
<<<<<<< HEAD
def member1_util():
    return "팀원1의 유틸 함수"
=======
def member2_util():
    return "팀원2의 유틸 함수"
>>>>>>> origin/main

# 두 코드 모두 유지하도록 수정 후
git add utils.py
git commit -m "fix: merge conflict 해결"
git push
```

---

### 시나리오 4: 협업 미션

**미션 1:** 각자 자신의 파일에 새로운 함수 추가하기
- `calculate_something()` 함수 구현
- 다른 팀원의 함수를 main.py에서 호출

**미션 2:** utils.py에 팀 공통 함수 추가하기
- 순서대로 한 명씩 추가 (충돌 방지)
- 또는 동시에 추가하여 충돌 해결 연습

**미션 3:** 코드 리뷰 연습
- Pull Request 만들고 서로 리뷰하기
- 리뷰 코멘트 달고 수정 요청하기

---

## 자주 사용하는 Git 명령어

```bash
# 상태 확인
git status
git log --oneline

# 브랜치
git branch              # 브랜치 목록
git checkout -b 이름    # 새 브랜치 생성 및 이동
git checkout main       # main 브랜치로 이동

# 동기화
git pull                # 원격 변경사항 가져오기
git fetch               # 원격 정보만 가져오기

# 커밋
git add .               # 모든 변경사항 스테이징
git commit -m "메시지"  # 커밋
git push                # 푸시

# 되돌리기
git checkout -- 파일명  # 수정 취소
git reset HEAD 파일명   # 스테이징 취소
```

---

## 팀원 정보

| 팀원 | 담당 파일 | 역할 |
|------|-----------|------|
| 팀원1 | team/member1.py | - |
| 팀원2 | team/member2.py | - |
| 팀원3 | team/member3.py | - |
| 팀원4 | team/member4.py | - |
