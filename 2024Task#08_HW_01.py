# - **Task #08 作業 01【實作題】階乘總和**
    
#     #練習：階乘總和
    
#     ❏ Requirements：
    
#     1. 利用迴圈讓使用者可以重複輸入一個數字 n
    
#     2. 利用程式計算 1! + 2! + 3! + ... + n! 的總和
    
#     3. 每一個回合請將階乘總和的結果印出
    
#     ❏ Sample Input： 4 ← 使用者輸入
    
#     ❏ Sample Output： 33 ← 畫面輸出
    
#     ❏ Sample Code：

x = input() # 4

'''
Your Code
'''

print(f) # 33




#先相乘得到一個總數，
#把總數存起來
#下一個相乘的結果都要和上一次的結果相加

number = int(input('請輸入正整數'))
multiplication_sum = 1 #存放相乘的結果
Total = 0 #和上一次的結果相加的總和
for x in range(1, number+1):
    multiplication_sum = multiplication_sum * x
    Total = Total + multiplication_sum
print(Total)

#方法2、math.factorial()-->
import math
number = int(input('請輸入正整數'))
Total = 0
for x in range(1,number+1):
      Total += math.factorial(x)
      print(Total)
