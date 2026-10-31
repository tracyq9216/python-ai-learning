import csv

with open("ledger.csv","w",encoding="utf-8",newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["日期","类别","金额"])
    writer.writerow(["10-25","餐饮",35])

with open("ledger.csv","a",encoding="utf-8",newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["10-25","餐饮",30.85])
    writer.writerow(["10-25","材料",359])
    writer.writerow(["10-25","餐饮",22.5])

with open("ledger.csv","r",encoding="utf-8",newline="")as f:
    reader = csv.reader(f)
    for row in reader:
        print(*row)

with open("ledger.csv","r",encoding="utf-8",newline="")as f:
    reader = csv.reader(f)
    next(reader)
    total=0

    for row in reader:
        amount=float(row[2])
        total=total+amount
    print("总计：",total)

def ask_amount():
    while True:
        try:
            amount=float(input("金额："))            
            print("记下了",amount)
            return amount
        except ValueError:
            print("请输入数字")
print(ask_amount())