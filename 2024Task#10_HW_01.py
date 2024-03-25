- **Task #10 作業 01【簡答題】例外處理**
    
    繳交作業時請直接複製以下題目到作業填答區，並將「(在這裡回答)」部分改寫成你的答案，不用附上題目、標題設定成「2024 Task#10 作業 01」：
    
    1. 回想看看到目前為止，你曾經遇到過哪些錯誤發生？
    
    (在這裡回答)
    
    語法不對
    
    2. 試著解釋什麼是「例外處理」，並且說明在哪些情況適合使用？
    
    (在這裡回答)
    
    希望遇到與預期不合時候做特定處理
    
    目的是在程式執行過程中遇到異常的情況時能夠正確處理這些異常，避免程式崩潰或出現不可預測的結果。在適當的情況下，我們可以使用 try...except...finally 來處理異常。
    
    3. 請問以下程式碼的「變數 e」代表的意義是什麼？
try:
    x = input() / input()
except Exception as e:
    print(e)
(在這裡回答)例外資訊存到(e)


4. 請問以下程式碼的「raise」跟「finally」的用法為何？
try:
    raise Exception('spam', 'eggs')
except Exception as e:
    print(e)
finally:
    print('done')

finally 一定會輸出done

else表示完全沒有錯誤，就會直行該區塊的程式，Finally不論程式對錯，都會執行該區域
