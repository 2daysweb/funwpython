#example of a computation without and w/wo functional abstraction

#setting up our input function and power variable
x = float(input('enter a number: '))
p = int(input('enter an integer power: '))

result = 1


for turn in range(p + 1):
        print('iteration: ' + str(turn) + ' ' \
              'current result: ' + str(result))
        result = result*x

        
