# #練習：元素位置異動

# ❏ Requirements：

# 1. 建立一個列表（List ）初始化為 1, 2... 9 的元素

# 2. 利用程式將最左邊的元素移動到最右邊

# 2. 最後請將移動的結果印出

# ❏ Sample Input： [1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化

# ❏ Sample Output： [2, 3, 4, 5, 6, 7, 8, 9, 1] ← 畫面輸出



mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_element = mylist.pop(0)
print('first element:', first_element)
mylist.append(first_element)
print(mylist)

-----

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
a.append(a.pop(0))#a.pop()刪除最後一個字元(9)，且返回該值。然後將該值append至最後，即最右邊
print(a)
