scores={"小明":88,"Lucy":98,"Nancy":75}

def show_score(name,score):
    print(f"{name} 考了{score}分")

for name,score in scores.items():
    show_score(name,score)

def say_hello(name):
    print(f"你好，{name}!")
    print("欢迎来上课")

say_hello("小明")
say_hello("Lucy")

def pass_or_not(name,score):
    if score >=80:
        print(f"{name} pass")
    else:
        print(f"{name} not pass")

for name,score in scores.items():
    pass_or_not(name,score)