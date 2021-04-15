'''
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자리수만큼 연속 숫자를 포함하는 번호를 생성하는 기능
'''

import numpy

def makeLottoNumber(**kwargs):
    randNumber = numpy.random.choice(range(1,46), 6, replace=False)
    randNumber.sort()

    #최종 로또 번호가 완성될 변수
    lotto = []

    if kwargs.get("include"):
        include = kwargs.get("include")
        lotto.extend(include)

        cntMake = 6 - len(lotto)

        for _ in range(cntMake):
            for j in randNumber:
                if lotto.count(j) == 0:
                    lotto.append(j)
                    break

    else:
        lotto.extend(randNumber)

    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        lotto = list(set(lotto) - set(exclude))

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                randNumber = numpy.random.choice(range(1,46), 6, replace=False)
                randNumber.sort()

                for j in randNumber:
                    if lotto.count(j) == 0 and j not in exclude:
                        lotto.append(j)
                        break

    if kwargs.get("continuty"):
        continuty = kwargs.get("continuty")
        startNumber = numpy.random.choice(lotto, 1)

        sequenceNum = []
        for i in range(startNumber[0], startNumber[0] + continuty):
            sequenceNum.append(i)
        sequenceNum.sort()
        cntMake = 6 - len(sequenceNum)
        lotto = []
        lotto.extend(sequenceNum)

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                randNumber = numpy.random.choice(range(1,46), 6, replace=False)
                randNumber.sort()

                for j in randNumber:
                    if lotto.count(j) == 0 and j not in sequenceNum:
                        lotto.append(j)
                        break

                lotto = list(set(lotto))

    lotto.sort()
    return lotto

print(makeLottoNumber(include=[1, 2], exclude=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
