import random

print("***************************")        # 처음 출력창
print("****가위바위보 프로그램****")
print("***************************")
print("")
print("")
print("가위바위보를 실시합니다.")
print("가위 : 0, 바위 : 1, 보자기 : 2")
print("")
print("(다른 숫자 입력시 강제종료)")
print("")

while True:                    # 가위바위보를 10번 반복
    print("가위바위보!")
    player = int(input(""))                 # 사용자의 수 결정
    if player == 0:
        print("사용자 : 가위")
    elif player == 1:
        print("사용자 : 바위")
    elif player == 2:
        print("사용자 : 보자기")
    else:
         print("프로그램을 종료합니다.")
         break

    print("")
    
    cpu = random.randint(0, 2)              # 컴퓨터의 수를 무작위로 결정
    if cpu == 0:
        print("컴퓨터 : 가위")
    elif cpu == 1:
        print("컴퓨터 : 바위")
    elif cpu == 2:
        print("컴퓨터 : 보자기")

    print("")
    
    if player == cpu:                       # 승패 판정
        print("비겼습니다.")
    elif player == 0 and cpu == 1:
        print("컴퓨터가 이겼습니다.")
    elif player == 0 and cpu == 2:
        print("사용자가 이겼습니다.")
    elif player == 1 and cpu == 0:
        print("사용자가 이겼습니다.")
    elif player == 1 and cpu == 2:
        print("컴퓨터가 이겼습니다.")
    elif player == 2 and cpu == 0:
        print("컴퓨터가 이겼습니다.")
    elif player == 2 and cpu == 1:
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


    
