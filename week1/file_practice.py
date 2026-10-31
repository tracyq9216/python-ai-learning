# 周日：读写文件

with open("diary.txt","w",encoding="utf-8")as f:
    f.write("今天学了函数\n")
    f.write("明天学文件\n")

with open("diary.txt","r",encoding="utf-8")as f:
    content = f.read()
print(content)

with open("words.txt","w",encoding="utf-8")as f:
    f.write("猫,cat\n")
    f.write("狗,dog\n")
    f.write("苹果,apple\n")
    f.write("太阳,sun\n")

with open("diary.txt","r",encoding="utf-8")as f:
    content =f.read()
print(content)

with open("words.txt","r",encoding="utf-8")as f:
    for line in f:
        print(line.strip())