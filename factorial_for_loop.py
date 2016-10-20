# Created on 20 oct 2016
# Created by: Matthew Lourenco
# this is a program the calculates factorials using a for loop
number = 1
while True:
    print('Enter an integer and I will find the factorial of that integer.')
    try:
        count = raw_input()
        count = int(count)+1
        for i in range(1, count):
            number = number * i
        print('The factorial of ' + str(count - 1) + ' is ' + str(number) + '.')
    except:
        print(str(count) + ' is not an integer.')
