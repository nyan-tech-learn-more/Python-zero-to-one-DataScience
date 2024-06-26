#練習：請將不同的 dict 元素合併成一個 dict

❏ Requirements：

1. 初始化三個 dict 分別為 {1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60}
2. 利用程式將三個 dict 的結果合併之後輸出

❏ Sample Input： {1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60} ← 預設初始化

❏ Sample Output： {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} ← 畫面輸出

❏ Sample Code：

#-------------
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}


d1.update(d2)
d1.update(d3)

print(d1) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#-------------------

d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}

d = {**d1,**d2,**d3}
print(d)
