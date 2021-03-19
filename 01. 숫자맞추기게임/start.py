import random
import os

def inputCheck(msg, casting):
    while True:
        try:
            userInput = casting(input(msg))
            return userInput
        except:
            continue

chance = 10
count = 0

number = random.randint(1, 99)
os.system("cls")
print("1부터 99까지의 숫자를 10번 안에 맞춰 보세요.")

while count < chance:
    count += 1
    userInput = inputCheck("몇 일까요? > ", int)

    if number == userInput:
        break
    elif userInput < number:
        print("{} 보다 큰 숫자입니다.".format(userInput))
    elif userInput > number:
        print("{} 보다 작은 숫자입니다.".format(userInput))

if userInput == number:
    print("성공! {} 이(가) 맞습니다.".format(number))
else:
    print("실패, 정답은 {}입니다.".format(number))