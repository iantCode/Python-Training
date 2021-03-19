import random
import os

numbers = []
number = str(random.randint(0, 9))
countStrike = 0
countBall = 0

for i in range(3):
    while number in numbers:
        number = str(random.randint(0, 9))
    numbers.append(number)

os.system("cls")
print("*" * 10)
print("숫자야구게임을 시작합니다.")
print("*" * 10)

while countStrike < 3:
    num = str(input("숫자 3자리를 입력하세요 > ")) #인덱싱으로 처리하면 편하다!
    countStrike = 0
    countBall = 0

    if len(num) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j:
                    countStrike += 1
                elif num[i] == numbers[j] and i != j:
                    countBall += 1

        if countStrike == 0 and countBall == 0:
            print("3아웃")
        else:
            output = ""
            if countStrike > 0:
                output += "{} 스트라이크 ".format(countStrike)
            if countBall > 0:
                output += "{} 볼 ".format(countBall)
            print(output[:-1])

print("게임 성공")