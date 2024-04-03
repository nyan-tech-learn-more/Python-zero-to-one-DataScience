- **Task #02 作業 01【實作題】複雜的字串取代**

    
    ❏ Requirements：
    
    1. 讓使用者輸入一個字串 s
    
    2. 利用程式將字串中出現的 not … at all 取代成 good 後輸出（Note: 可以假設字串中最多只會出現一次 not ... at all）
    
    ❏ Sample Input #1: This company is not poor at all. ← 使用者輸入
    
    ❏ Sample Output #1: This company is good. ← 畫面輸出
    
    ❏ Sample Input #2: I'm not at all happy about it. ← 使用者輸入
    
    ❏ Sample Output #2: I'm good happy about it. ← 畫面輸出
    
    ❏ Sample Code:


s = input() # This company is not poor at all.


'''

s = input() # This company is not poor at all.

#把not取代成Good 不可用，因為無法替代 not .... at all 中間的 會變成This company is good poor 
#移除At All
s = s.replace("not","good")
s = s.replace("at all","")
print(s)
print(s) # This company is good.
'''

print(d) # This company is good.



#-----

string = input()
#This company is not poor at all.
#I'm not at all happy about it.
string1 = string.split('not')
#'this comapny ', ' at all'
string1 = string1[0]
print(string1)
#'this company'

string2 = string.split('at all')
print(string2)
# 'this company is not poor ', ''
# I 'am
string2 = string2[1]
# ' happy about it.'
#["I 'am not ", ' happy about it.']

print(string1 + 'good' + string2)
#'this company' + 'good' + ''
#this company is good
##I 'am good happy about it.
