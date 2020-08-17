score=int(input("請輸入成績"))
if score>=0 and score<=100:
    if score>=90:
        print("等級A")
    elif score>=80:
        print("等級b")
    elif score>=70:
        print("等級c")
    elif score>=60:
        print("等級d")
    else:
        print("等級e")
else:
    print("錯誤")
    
        