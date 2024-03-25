繳交作業直接貼上完整的 Python 程式碼即可（不用上傳 .py 檔案），不用附上題目、標題設定成「2024 Task#07 作業 03」：

#練習：奇偶數分堆

❏ Requirements：

1. 建立一個列表（List ）初始化為 0, 1, 2... 9 的元素

2. 請利用條件判斷與迴圈將 List 中的奇數放在前面、偶數放在後面

3. 最後請將分堆後的結果印出

❏ Sample Input： [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化

❏ Sample Output： [1, 3, 5, 7, 9, 0, 2, 4, 6, 8] ← 畫面輸出

❏ Sample Code：

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
Your Code
'''

print(L) # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]



-------



List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_list = []
even_list = []

for i in List: #List一個一個讀到i中
    if i % 2 != 0: #i如果除以2餘數不等於0
      odd_list.append(i) #用append取出i並存入odd_list末端中，位置在odd_list末尾
      print(odd_list)
    else:
      even_list.append(i) #用append取出i並存入even_list末端位置在odd_list末尾
      print(even_list)
sum_list = odd_list + even_list
odd_list.extend(even_list) #第二種輸出
print('加總：', sum_list)
print('加總：', odd_list)






另一個聰明
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(L)):
    if (i % 2 == 0):
        L.append(i) #偶數複製一個丟到最後面
        L.remove(i) #移除原本這個偶數
print(L)
