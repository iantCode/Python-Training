import os

operator = ("+", "-", "*", "/", "=")

def StringCalculator(userInput, showHistory=False):
    stringList = []
    lastOperatorPos = 0

    if userInput[-1] not in operator:
        userInput += "="

    for i, s in enumerate(userInput):
        if s in operator:
            if userInput[lastOperatorPos:i].strip() != "":
                stringList.append(userInput[lastOperatorPos:i].strip())
                stringList.append(s)
                lastOperatorPos = i + 1

    stringList.pop(-1)

    pos = 0
    while True:
        if pos + 1 > len(stringList):
            break
        if len(stringList) > pos + 1 and stringList[pos] in operator:
            temp = " ".join(stringList[pos-1:pos+2])
            del stringList[0:3]
            stringList.insert(0, str(eval(temp)))
            pos = 0
            if showHistory:
                print(stringList)
        pos += 1
    
    if len(stringList) > 0:
        result = float(stringList[0])

    return round(result, 4)

os.system("cls")
while True:
    userInput = input("계산식을 입력하세요 > ")
    if userInput == "/exit":
        break
    result = StringCalculator(userInput, True)
    print("결과: {}".format(result))
    os.system("pause")