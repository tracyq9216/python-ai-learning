history=[]

history.append({"role":"user","content":"你好"})
history.append({"role":"assistant","content":"你好呀小朋友"})

for item in history:
    role=item["role"]
    content=item["content"]
    print(f"{role}:{content}")