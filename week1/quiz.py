words={"苹果":"apple","猫":"cat","狗":"dog","太阳":"sun"}
score=0

for cn,en in words.items():
    answer=input(f"{cn}的英文是？").lower()
    if answer == en :
        print("✅对了")
        score=score+1
    else:
        print(f"❌错了，正确答案是{en}")


print(f"你答对了{score}/{len(words)}题")
if score==len(words):
    print("太棒了！")
else :
    print("继续加油！")