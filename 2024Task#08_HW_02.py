- **Task #08 作業 02【實作題】字串計數**
    
    繳交作業直接貼上完整的 Python 程式碼即可（不用上傳 .py 檔案），不用附上題目、標題設定成「2024 Task#08 作業 02」：
    
    #練習：字母頻率（frequency of letters; character frequencies），指的是各個字母在文本材料中出現的頻率。常被應用於密碼學，尤其是可破解古典密碼的頻率分析。例如，摩斯密碼中越常用的字母，其編碼符號就越短；而數據壓縮技術中也有相似的方法，如夫曼編碼就是按來源符號出現的機率大小去編碼。接下來，讓我們來試試看如何在 Python 實現從字串中計算每個字母出現頻率的問題？
    
    ❏ Requirements：
    
    1. 讓使用者可重複輸入字串
    
    2. 每一回合計算該字串中每個字母的出現次數並且存入 dict 中
    
    3. 將使用者輸入字串的字母及其計數印出
    
    ❏ Sample Input： Hello World ← 使用者輸入
    
    ❏ Sample Output： {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1} ← 畫面輸出
    
    ❏ Sample Code：

x = input() # Hello World

'''
Your Code
'''

print(f) # {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1}


#---


str = input() #
wordlist = {} #字典, key:value
print(wordlist)
for x in str:
    if x in wordlist: 
        wordlist[x] = wordlist[x] + 1
    if x not in wordlist:
        wordlist[x] = 1
print(wordlist)


str = input() #
wordlist = {} #字典, key:value
print(wordlist)
for x in str: #str每個字串拆出來放到x變數
    wordlist[x] = wordlist.get(x, 0)+1 #把字串放到字典
  #get(key, default) 將 key 取出字典中的值，如果找不到 key 則返回 0，找到的話＋ㄅ
print(wordlist)



#使用方法
# 創建一個字典，將鍵 'name' 和值 'John' 添加到其中
my_dict = {'name': 'John'}

# 將鍵 'age' 和值 30 添加到字典中
my_dict['age'] = 30

# 將鍵 'gender' 和值 'Male' 添加到字典中
my_dict['gender'] = 'Male'

# 輸出整個字典
#print(my_dict) # 輸出 {'name': 'John', 'age': 30, 'gender': 'Male'}
      
