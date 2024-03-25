# ## **Task#04 作業 02**

# 練習：元素位置異動

# ❏ Requirements：

# 1. 建立一個列表（List ）初始化為 1, 2... 9 的元素

# 2. 利用程式將最右邊的元素移動到最左邊邊

# 2. 最後請將移動的結果印出

# ❏ Sample Input： [1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化

# ❏ Sample Output： [9, 1, 2, 3, 4, 5, 6, 7, 8] ← 畫面輸出

# ❏ Sample Code：

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
final_var = mylist[8] #將index8（最後一個）數值存到final_var
mylist.insert(0, final_var) #把final_var插入到index0
mylist.pop() #刪除最後一個數值
print(mylist)

-----

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_element = mylist.pop()  # 取出最後一個元素放到last_lelment
mylist.insert(0, last_element)  # 插入到最前面index0
print(mylist)

----

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
a.insert(0,a.pop()) #a.pop()刪除最後一個字元(9)，且返回該值。然後將該值inser至index 0的位置，即最左邊
print(a)
