import time
import random
import os

WORD_LIST = [
    "동해 물과 백두산이 마르고 닳도록",
    "하느님이 보우하사 우리나라 만세",
    "무궁화 삼천리 화려강산",
    "대한사람 대한으로 길이 보전하세"
]

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    os.system("cls")
    startTime = time.time()
    userInput = str(input(q + "\n")).strip()
    endTime = time.time()

    if userInput == "/exit":
        break

    correct = 0
    for i, c in enumerate(userInput):
        if i >= len(q):
            break
        if c == q[i]:
            correct += 1
    
    totalLen = len(q)
    correctRate = correct / totalLen * 100
    errorRate = (totalLen - correct) / totalLen * 100
    speed = correct / (endTime - startTime) * 60

    print("속도: {:0.2f} 정확도: {:0.2f} 오타율: {:0.2f}".format(speed, correctRate, errorRate))
    os.system("pause")