#데코레이터

def outer_function(msg):
    def inner_function():
        return "난 내부 함수인데 {} 메세지를 받았어.".format(msg)
    return inner_function

c = outer_function("헬로")
print(c())
print(dir(c))
print(c.__closure__)
print(dir(c.__closure__[0]))
print(c.__closure__[0].cell_contents)

import time

def time_checker(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("함수 {} 실행 시간 : {} 초".format(func.__name__, end_time-start_time))
        return result
    return inner_function

@time_checker
def test():
    start_time = time.time()
    for i in range(5):
        time.sleep(0.1)
    end_time = time.time() - start_time
    print("함수 실행 시간 : {} 초".format(end_time))

@time_checker
def test2():
    for i in range(3):
        time.sleep(0.1)

test()
test2()

from functools import wraps

def login_required(func):
    @wraps(func)  #가 없다면 57줄, 58줄이 정상적으로 데이터를 읽어올 수 없음.
    def inner_function(*args, **kwargs):
        if not kwargs.get("is_login"):
            return "로그인이 필요한 페이지입니다."
        return func(*args, **kwargs)
    return inner_function

@login_required
def login():
    '''로그인 테스트 함수입니다.'''
    print("안녕")

print(login.__name__)
print(login.__doc__)

def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return "<{}>{}</{}>".format(new_args, func(name), new_args)
        return wrapper
    return decorator

@add_tag("html")
def addtest(msg):
    return "반가워 " + msg

print(addtest("홍길동"))