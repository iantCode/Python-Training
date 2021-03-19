#파이썬 예외 처리 try / except

try:
    #n = "10.5"
    #v = n[0]
    n = []
    v = n[0]
except ValueError as e:
    print("오류 발생 : {}".format(e))
except:
    print("다른 오류 발생")
else:
    print("오류 발생 안함")
finally:
    print("try 문 종료")