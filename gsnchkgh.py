#Finding a square root of an integer
#Program uses a guess and check method


x = int(input("Enter a number: "))
ans = 0

while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print(str(ans) + " " + "is most def the square root of" + " " + str(x))
else:
    print(str(x)+ " " + "is not a perfect square dewd")

    
