#A ball is dropped from a tower of height h. It has initial velocity zero and accelerates downwards under gravity. The challenge is to write a program
#that asks the user to enter the height in meters of the tower and a time interval t
#in seconds, then prints on the screen the height of the ball above the ground at time t after
#it is dropped, ignoring air resistance

h = float(input("Enter the height of the tower: "))
t = float(input("Enter the time interval : "))
s = 9.81*t**2/2

print("The height of the ball is", h-s, "meters")




