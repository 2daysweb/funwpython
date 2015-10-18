#Finding cube root through approximation methods

x = 64.0
epsilon = 0.01
step = epsilon**2
numGuesses = 0.0
ans = 0.0

#condition(1)ensures we don't loop too far, (2) ensures we don't stop early
while (abs(ans**3 - x)) >= epsilon and ans <= x:
    ans += step
    #Keep track of the number of guesses made via while loop
    numGuesses += 1
print('numGuesses = ' + " " + str(numGuesses))

#condition used as success metric of our approx method 
if abs(ans**3 - x) >= epsilon:
    print("Failed on square root of" + " " + str(x))
else:
    print(str(ans) + " " + "is close to cube root of" + " " + str(x))


    
    
