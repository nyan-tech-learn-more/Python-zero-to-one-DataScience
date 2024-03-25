#練習：請將列表中重複的元素移除並且將元素由大到小排列

❏ Requirements：

1. 在程式中初始化一個列表，其內容為 [1, 1, 3, 9, 7, 8, 8, 8]

2. 利用程式將列表中重複的元素移除

3. 最後請將剩餘元素由大至小排序後印出

❏ Sample Input： [1, 1, 3, 9, 7, 8, 8, 8] ← 預設初始化

❏ Sample Output： [9, 8, 7, 3, 1] ← 畫面輸出

❏ Sample Code：

```python
#方法1

List = [1, 1, 3, 9, 7, 8, 8, 8]
newset = set(List) #用set()特性去重複，集合（Set）是 Python 中的一種容器類型，它由一些唯一且不可變的元素組成
newlist = list(newset) #因為set不可變，要先轉成list
newlist.sort(reverse=True) #排序list, reverse是由大到小
print(newlist) # [9, 8, 7, 3, 1]

#方法2

List = [1, 1, 3, 9, 7, 8, 8, 8]
newset = set(List) 
#用set()特性去重複，集合（Set）是 Python 中的一種容器類型，它由一些唯一且不可變的元素組成

newlist = sorted(newset, reverse=True) 
#最簡單的一個內建函式 sorted，可以幫助我們對一個 List 進行 Sorting。sorted 會回傳一個新的 List，不會改變本來的 List。而新的 List 預設會是以 Ascending order 排序 (由小到大)，但如果我們將 Flog reverse 改成 True 的話就會得到 Descending order (由大到小)。除了可以對 List 排序外，sorted 也可以對 Tuple 和 Set (本身沒有順序) 進行排序，但是 Output 都是 List

print(newlist) # [9, 8, 7, 3, 1]

#reverse 也能用[::-1]倒敘
```

#https://ithelp.ithome.com.tw/articles/10225670?sc=rss.iron

#https://docs.python.org/zh-tw/3/howto/sorting.html
