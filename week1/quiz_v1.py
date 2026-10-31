# 单词小测验v1

def ask_word(cn,en):
    answer = input(f"{cn}的英文是？").strip().lower()
    if answer==en:
        print("✅答对了")
        return True
    else :
        print(f"❌正确答案是{en}")
        return False

def run_quiz(word_dict):
    wrong={}
    for cn,en in word_dict.items():
        if ask_word(cn,en)!=True:
            wrong[cn]=en
    total=len(word_dict)
    wrong_count=len(wrong)
    right_count=total-wrong_count
    print(f"这一轮答对{right_count}/{total}题")
    return wrong

def main():
    words={"猫":"cat","狗":"dog","苹果":"apple","太阳":"sun"}
    left=run_quiz(words)
    while len(left)>0:
        print("再来一轮错词！")
        left=run_quiz(left)
    print("🎉全部答对，太棒了！")

main()