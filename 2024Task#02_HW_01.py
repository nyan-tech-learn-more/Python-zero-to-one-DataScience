# 1請問「=」運算的行為的是什麼？以下程式碼會印出的結果是什麼？

x = 123
y = 456

x = y
y = 789

print(x)
print(y)

#OUTPUT
x = 456
y = 789


#2. 在 Python 中，「*」跟「**」運算分別代表什麼，哪一個運算優先順序比較高？
# *=相乘
# **= 次方
# **優先序比較高


#3. 在 Python 中，請問「/」跟「//」運算分別代表什麼，哪一個運算優先順序比較高？
# / = 相除

# // = 整數相除，結果會只有整數

#4. 該如何把「4.3」變成整數型態？該如何把「3」變成浮點數型態呢？
x = 4.3

x = int(x) #透過int()把x轉為int後存回x

print(type(x)) #int 型別

y = 3

y = float(y) #y=3轉float存回y

print(type(y),y) #確認型別


#5. 如果在程式中看到這個錯誤「NameError: name 'n' is not defined」可能的原因是什麼？
#變數n可能沒有被定義宣告
