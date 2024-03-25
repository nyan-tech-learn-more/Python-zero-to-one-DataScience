# 練習：試著用 Python 將網址當中的 domain 取出來。

# ❏ Requirements：

# 1. 讓使用者可以輸入一個網址

# 2. 利用程式取出網址當中的 domain 後輸出

# ❏ Sample Input： https://www.facebook.com/dscareer ← 使用者輸入

# ❏ Sample Output： www.facebook.com ← 畫面輸出

# ❏ Sample Code：

s = input() # https://www.facebook.com/dscareer

'''
Your Code
'''

print(s) # www.facebook.com

#My code

#s = input() # https://www.facebook.com/dscareer
s = "https://www.facebook.com/dscareer"
s = s.split("/") #用/去切字串
#['https:', '', 'www.facebook.com', 'dscareer']
print(s[2]) #取出index 2
print(s) # www.facebook.com
