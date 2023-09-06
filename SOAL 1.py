kata = input ('')
temp = ''
for i in range (len(kata)-1, -1, -1):
    temp+=kata[i]
if(kata == temp):
    print("Palindrom")
else :
    print("Bukan palindrom")