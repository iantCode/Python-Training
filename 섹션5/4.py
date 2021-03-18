#사용자 함수

def 함수명():
    print("함수호출")
    return True

c = 1

def add(a, b):
    global c #전역변수 c를 사용하겠다.
    c = a + b
    return c

a = 함수명()
b = add(1, 10)
print(b, c)

def get_input_user(msg, casting=str): #=str 는 생략한 경우 기본값으로 생각하게 된다.
    while True:
        try:
            user = casting(input(msg))
            return user
        except:
            continue

user = get_input_user("사용자 이름을 입력하세요. >")
age = get_input_user("사용자 나이를 입력하세요. >", int)
print(user, age)

def save_winner(*args): #Tuple로 입력받음
    print(args)

def save_winner2(**kwargs): #Dictionary로 입력받음
    print(kwargs)
    if kwargs.get("name1"):
        print(kwargs["name1"])

save_winner("홍길동", "가가멜")
save_winner2(name1="홍길동", name2="가가멜")

def outer_function(func):
    def inner_function(*args, **kwargs):
        print("함수명: {}".format(func.__name__))
        print("args : {}".format(args))
        print("kwargs : {}".format(kwargs))
        result = func(*args, **kwargs)
        print("result : {}".format(result))
        return result
    return inner_function

f = outer_function(add)
f(10, 20)