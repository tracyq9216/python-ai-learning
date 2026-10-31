scores=[88,92,75]
print(scores[0])
print(scores[-1])
scores.append(60)
print(f"一共有{len(scores)}个分数")

words=["apple","cat","dog"]
print("cat"in words)
words[1]="cow"
print(words)

if "cat" in words:
    print("cat in words")
else:
    print("cat not in words")

words=["apple","cat","dog"]
for w in words:
    print(w)

total=0
for s in [88,92,75]:
    total=total+s
    print(f"加上{s},现在是{total}")
print(f"总分{total}")






scores=[88,92,75,93]
for w in scores:
    print(f"分数:{w}")

total=0
for s in scores:
    total=total+s
print(f"总分:{total}")
print(f"{total/len(scores)}")

count = 0
for p in scores:
    if p >= 80:
        print(p)
        count=count+1
print(f"及格的有{count}个.")

count=0
print(count)
count=count+1
print(count)
count=count+1
print(count)