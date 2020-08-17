mscore=int(input("請輸入m成績"))
escore=int(input("請輸入e成績"))
if escore>=0 and escore<=100 and mscore>=0 and mscore<=100:
 
    if escore>=90 and mscore>=90:
        print("有獎品")
    elif escore<60 and mscore<60:
        print("有處罰")
    elif escore<60 or mscore<60:        
        print("再加油")
else:
    print("錯誤")