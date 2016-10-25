import random

print("***************************")        # 처음 출력창
print("****가위바위보 프로그램****")
print("***************************")
print("")
print("")
print("가위바위보를 실시합니다.")
print("(가위 : '가위'입력, 바위 : '바위' 입력, 보자기 : '보자기'입력)")
print("(다른 문자 입력시 강제종료)")
print("")

while True:                    # 가위바위보를 10번 반복
    print("가위바위보!")
    player = input("")                  # 사용자의 수 결정
    if player == '가위':
        print("사용자 : 가위")
    elif player == '바위':
        print("사용자 : 바위")
    elif player == '보자기':
        print("사용자 : 보자기")
    else:
         print("프로그램을 종료합니다.")
         break

    print("")
    
    cpunum = random.randint(0, 2)              # 컴퓨터의 수를 무작위로 결정
    if cpunum == 0:
        cpu = '가위'
        print("컴퓨터 : 가위")
    elif cpunum == 1:
        cpu = '바위'
        print("컴퓨터 : 바위")
    elif cpunum == 2:
        cpu = '보자기'
        print("컴퓨터 : 보자기")

    print("")
    
    if player == cpu:                       # 승패 판정
        print("비겼습니다.")
    elif player == '가위' and cpu == '바위':
        print("컴퓨터가 이겼습니다.")
    elif player == '가위' and cpu == '보자기':
        print("사용자가 이겼습니다.")
    elif player == '바위' and cpu == '가위':
        print("사용자가 이겼습니다.")
    elif player == '바위' and cpu == '보자기':
        print("컴퓨터가 이겼습니다.")
    elif player == '보자기' and cpu == '가위':
        print("컴퓨터가 이겼습니다.")
    elif player == '보자기' and cpu == '바위':
        print("사용자가 이겼습니다.")
    else:
        print("오류 : 사용자와 컴퓨터가 정한 수가 유효하지 않습니다.")
        break
    print("")

    yesno = input("다시 하시겠습니까?(y입력 : 예, n입력 : 아니오)")
    if yesno == 'n':
        print("프로그램을 종료합니다.")
        break
    else:
        print("")


    
