scores={"小明":88,"Lucy":98,"Nancy":75}

def is_pass(score):
    if score>=80:
        return True
    else :
        return False

count=0
for name,score in scores.items():
    if is_pass(score):
        count=count+1

print(f"及格的有{count}人")



def average(nums):
    if len(nums)==0:
        return 0
    total=sum(nums)
    return total/len(nums)

result=average(scores.values())
print(f"平均分是{result}分")