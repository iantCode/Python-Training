#한글 : ((초성 * 21) + 중성) * 28 + 종성 + 0xAC00 (44032)
#초성 : ((x - 44032) / 28) / 21
#중성 : ((x - 44032) / 28) % 28
#종성 : (x - 44032) % 28

import time
import random
import os

CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

WORD_LIST = [
    "동해 물과 백두산이 마르고 닳도록",
    "하느님이 보우하사 우리나라 만세",
    "무궁화 삼천리 화려강산",
    "대한사람 대한으로 길이 보전하세"
]

def breakKorean(string):
    wordList = list(userInput)
    brokenWord = []
    for k in wordList:
        if ord(k) >= ord("가") and ord(k) <= ord("힣"):
            charIndex = ord(k) - 44032

            #초성
            charCho = int((charIndex / 28) / 21)
            brokenWord.append(CHO[charCho])

            #중성
            charJung = int((charIndex / 28) % 21)
            brokenWord.append(JUNG[charJung])

            #종성
            charJong = int(charIndex % 28)
            if charJong > 0:
                brokenWord.append(JONG[charJong])
        
        else:
            brokenWord.append(k)

    return brokenWord

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    os.system("cls")
    startTime = time.time()
    userInput = str(input(q + "\n")).strip()
    endTime = time.time()

    brokenQ = breakKorean(q)
    brokenUserInput = breakKorean(userInput)

    if userInput == "/exit":
        break

    correct = 0
    for i, c in enumerate(brokenUserInput):
        if i >= len(brokenQ):
            break
        if c == brokenQ[i]:
            correct += 1
    
    totalLen = len(brokenQ)
    correctRate = correct / totalLen * 100
    errorRate = (totalLen - correct) / totalLen * 100
    speed = correct / (endTime - startTime) * 60

    print("속도: {:0.2f} 정확도: {:0.2f} 오타율: {:0.2f}".format(speed, correctRate, errorRate))
    os.system("pause")