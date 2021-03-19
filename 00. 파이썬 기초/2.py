#파이썬에서 파일 읽고 쓰기

file = open("sample.txt", mode="w", encoding="utf-8")
file.write("Hello, 파이썬!")
file.close()

rfile = open("sample.txt", mode="r", encoding="utf-8")
content = rfile.read()
rfile.close()

print(content)

rfile = open("sample.txt", mode="r", encoding="utf-8")
a = rfile.read(10)
print(a)
rfile.seek(0)

a = rfile.read(10)
print(a)
rfile.close()

with open("sample.txt", mode="r", encoding="utf-8") as file:
    print(file.read())

with open("sample.txt", mode="r", encoding="utf-8") as s, \
     open("sample2.txt", mode="w", encoding="utf-8") as t:
    t.write(s.read().replace("파이썬", "Python"))