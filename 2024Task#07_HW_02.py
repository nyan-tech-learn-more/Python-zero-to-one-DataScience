繳交作業直接貼上完整的 Python 程式碼即可（不用上傳 .py 檔案），不用附上題目、標題設定成「2024 Task#07 作業 02」：

#練習：n! 階乘代表 1 * 2 * 3 ... * n 的乘積總和，請用 Python 程式實現 n! 計算。

❏ Requirements：

1. 讓使用者可以自行輸入一個數字 n，請檢查 n 是否為合法數字否則回傳錯誤巡席

2. 利用程式計算 n! 的結果並且印在畫面上

❏ Sample Input #01： 4 ← 使用者輸入

❏ Sample Output #01： 24 ← 畫面輸出

❏ Sample Input #02： a ← 使用者輸入

❏ Sample Output #02： a 是一個不合法的輸入，無法運算 ← 畫面輸出

❏ Sample Code：


x = input() # 4

'''
Your Code
'''

print(f) # 24


-------------

num = input()
y = 1
if num.isdigit() and int(num)>0: #如果輸入的num是數字(True)且大於0才執行
    num = int(num) #宣告數字為int
    for i in range(1,num+ 1): #  從第一個到開始取．輸入的數字是最後一個，還要加1（最後一個不會取所以要+1)，1..2..3..4..5......輸入數字
        y = y * i #1乘以1存回y,1(y)乘以2(i)存回y,2(y)乘以3(i)存回y
      #6(y)乘以4(i)存回y
        print(y) #列印y
else:
    print("請輸入正整數")
    
    
    
#------
 10
 
 
1
2
6
24
120
720
5040
40320
362880
3628800
