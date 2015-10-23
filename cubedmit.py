#A simple cube calculator. Slight modification on Eric Grimson's square calculator. 
def cubed(x):
    return x*x*x

#Clever use of while loop imo.
def triplePower(x, n):
    while n>1:
        x = cubed(x)
        n = n/3
    return x


#Note that the values of the global variables (x=5,y=1) don't influence the local procedure carried out in twoPower function
x = 5
n = 1

print(triplePower(2,3))


