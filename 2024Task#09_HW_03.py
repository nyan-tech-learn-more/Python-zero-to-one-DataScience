繳交作業直接貼上完整的 Python 程式碼即可（不用上傳 .py 檔案），不用附上題目、標題設定成「2024 Task#09 作業 03」：

#練習：請撰寫一個 sum(…) function 將輸入的參數計算總和後回傳。

❏ Requirements：

1. 定義一個可以計算總和的 sum function，其中參數的數量可以是動態不固定的

❏ Sample Input #01： f(1, 2, 3) ← 預設呼叫

❏ Sample Output #01： 6 ← 畫面輸出

❏ Sample Input #02： f(1, 2, 3, 4, 5) ← 預設呼叫

❏ Sample Output #02： 15 ← 畫面輸出

❏ Sample Code：

def f('''Your Code'''):
    '''
    Your Code
    '''

print(f(1, 2, 3)) # 6
print(f(1, 2, 3, 4, 5)) # 15


#---

def functionsum(*args):
    num = 0
    for x in args:
        num = num + x
    return num
print(functionsum(1,2,3,4,5))




def functionsum(*args):
  return sum(args)

print(functionsum(1, 2, 3, 4, 5))
