

繳交作業直接貼上完整的 Python 程式碼即可（不用上傳 .py 檔案），不用附上題目、標題設定成「2024 Task#10 作業 02」：

#練習：這裡有一個「讓使用者輸入一個整數 n，然後定義兩個函數來找出小於 n 的所有質數」的範例，請增加例外處理的機制處理非數值的輸入的例外狀況。

❏ Requirements：

1. 讓使用者輸入一個整數 n，有可能輸入非數值的資料導致錯誤

2. 請新增一段例外處理，當使用者輸入錯誤的結果能捕捉

❏ Sample Input： abc ← 使用者輸入

❏ Sample Output： 請輸入大於零的正整數 ← 畫面輸出

❏ Sample Code：


def is_prime(num):
    """判斷一個數字是否為質數"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(n):
    """找出小於 n 的所有質數"""
    prime_list = []
    for num in range(2, n):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

while True:
    try:  
        x = int(input("請輸入一個整數 n: "))
    except ValueError:
        print("不可以輸數字串")
    else:
        if x <= 0:
            print("不可以輸入0")
    result = primes(x)
    print(", ".join(map(str, result)))

# while True 迴圈會一直執行，直到使用者輸入一個有效的整數。
# 如果使用者輸入了一個錯誤的值，例如一個非數字字串，則會觸發 ValueError 例外。
# 在 except ValueError 塊中，程式碼會輸出 "不可以輸數字串" 訊息。
# 然後，程式碼會繼續執行 while True 迴圈，並再次提示使用者輸入一個整數。
# 因此，如果出現錯誤，程式碼會一直要求使用者重新輸入，直到輸入一個有效的整數
