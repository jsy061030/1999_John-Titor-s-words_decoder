dic = {'0':0,'1':1, '2':2, '3':3,'4':4,'5':5,'6':6,\
       '7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14, 'F':15}
sp = str()
s = input()
if len(s) % 2 != 0:
    print('Input Error!')
    exit()
for i in range(len(s)//2):
    num = dic[s[i*2]] * 16 + dic[s[i*2+1]]
    sp += chr(num)
print(sp)