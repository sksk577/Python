
# 가위바위보 프로그램 주석


## 프로그램 실행 시 화면 출력 부분

```
import random

print("***************************")
print("****가위바위보 프로그램****")
print("***************************")
print("")
print("")
print("가위바위보를 10번 실시합니다.")
print("가위 : 0, 바위 : 1, 보자기 : 2")
print("")
print("(다른 숫자 입력시 강제종료)")
print("")
```

## 사용자와 컴퓨터의 수 결정 부분

*사용자의 수*
```
for i in range(1, 11): 
    print("가위바위보!")
    player = int(input(""))
    if player == 0:
        print("사:
        print("사용자 : 보자기")
       print("프로그램을 종료합니다.")
        break    
    print("")
```

*컴퓨터의 수*

```
    cpu = random.randint(0, 2)
    if cpu == 0:
        print("컴퓨터 : 가위")
    elif cpu == 1:
        print("컴퓨터 : 바위")
    elif cpu == 2:
        print("컴퓨터 : 보자기")
    print("")
```

## 가위바위보 결과 출력 부분

```
    if player == cpu:
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
