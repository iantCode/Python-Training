import random
import os

wordsDict = {
    "사자": "lion",
    "호랑이": "tiger",
    "사과": "apple",
    "비행기": "airplane",
}

words = []
for word in wordsDict:
    words.append(word)

random.shuffle(words)
os.system("cls")

chance = 3
for i in range(0, len(words)):
    q = words[i]

    for j in range(0, chance):
        userInput = str(input("{}의 영어 단어를 입력하세요. > ".format(q)))
        english = wordsDict[q]
        if userInput.strip().lower() == english.lower():
            print("맞았습니다.")
            break
        else:
            print("틀렸습니다.")

    if userInput != english:
        print("정답은 {} 입니다.".format(english))

print("문제가 더 없습니다.")