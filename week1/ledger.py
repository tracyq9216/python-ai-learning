import csv

def ask_amount():
    while True:
        try:
            amount=float(input("金额："))            
            return amount
        except ValueError:
            print("请输入数字")
            
def add_entry():
    date = input("日期：")
    category = input("类别：")
    amount = ask_amount()
            
    with open("ledger.csv","a",encoding="utf-8",newline="")as f:
        writer = csv.writer(f)
        writer.writerow([date,category,amount])

def show_totals():
    with open("ledger.csv","r",encoding="utf-8",newline="")as f:
        reader = csv.reader(f)
        next(reader)
        totals={}
        for row in reader:
            print(*row)
            category=row[1]
            amount=float(row[2])
            if category in totals:
                totals[category]=totals[category]+amount
            else:
                totals[category]=amount

        for category,amount in totals.items():
            print(category,"总计：",round(amount,2),"元")

def main():
    add_entry()
    show_totals()

main()