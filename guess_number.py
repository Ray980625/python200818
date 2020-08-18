import random
num=random.randint(1,20)
i=0
while i<5:
    i=i+1
    ans=int(input("請輸入數字:"))
    if num == ans:
        print('恭喜答對')
        print("玩了"+str(i)+"次")
        break
    else:
        print('答錯了')
        if ans > num:5
        print("太大了")
        if ans < num:
            print('太小了')
        