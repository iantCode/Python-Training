import os

while True:
    os.system("cls")
    s = input("계산식 입력 > ")
    print("결과 :", eval(s))
    os.system("pause")