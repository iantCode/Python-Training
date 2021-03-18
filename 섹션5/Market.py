class FishCakeMaker:
    def __init__(self, **kwargs): #생성자
        self._size = 10
        self._flavor = "팥"
        self._price = 100
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "flavor" in kwargs:
            self._size = kwargs.get("flavor")
        if "price" in kwargs:
            self._size = kwargs.get("price")

    def __str__(self):
        return "<Class FishCakeMaker (size={}, flavor={}, price={}".format(self._size, self._flavor, self._price)

    def show(self):
        print("붕어빵 종류 {}".format(self._flavor))
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 가격 {}".format(self._price))

class MarketGoods(FishCakeMaker): #상속 클래스
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self._marketPrice = self._price + margin
    def show(self):
        print(self._flavor, self._marketPrice)

if __name__ == "__main__":
    print("Market.py 직접 실행")