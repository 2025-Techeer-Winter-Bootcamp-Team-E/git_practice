"""
Git 협업 연습 프로젝트 - 메인 파일
4명의 팀원이 함께 작업하는 프로젝트입니다.
"""

from team import member1, member2, member3, member4
from utils import print_header, print_separator


def main():
    print_header("Git 협업 연습 프로젝트")

    # 팀원 소개 출력
    print("\n[팀원 소개]")
    print_separator()

    members = [
        member1.introduce(),
        member2.introduce(),
        member3.introduce(),
        member4.introduce(),
    ]

    for info in members:
        print(f"- {info}")

    print_separator()

    # 각 팀원의 기능 실행
    print("\n[각 팀원의 기능 실행]")
    print_separator()

    print("팀원1:", member1.my_function())
    print("팀원2:", member2.my_function())
    print("팀원3:", member3.my_function())
    print("팀원4:", member4.my_function())

    print_separator()
    print("\n프로젝트 실행 완료!")


if __name__ == "__main__":
    main()
