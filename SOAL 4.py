x = int(input())

pembagi = 0
if x > 1 :
    for i in range(2, x):
        if (x % i) == 0:
            pembagi += 1
        
if pembagi == 0 and x > 1 :
    print("Bilangan prima")
else:
    print("Bukan bilangan prima")
