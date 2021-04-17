
n,m = map(int, input().split())
n = n//2
string=".|."

#Top Cone
for i in range(n):
    print(
        ((string*i) +string+ (string*i)).center(m,'-')
    )

#Middle Belt
print("WELCOME".center(m,'-'))

#Bottom Cone
for i in range(n):
    print(
        ((string*(n-1-i)) +string+ (string*(n-1-i))).center(m,'-')
    )   
