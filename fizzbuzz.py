#!usr/bin/python3
#simple fizzbuzz.py
# Author: @fr4nkl1n-1k3h

for num in range(101):
    if num%5 == 0 and num%3 == 0:
        print('fizzbuzz',num)
    elif num%5 == 0:
        print('buzz',num)
    elif num%3 == 0:
        print('fizz',num)
    else:
        print(num)
        
print("Simple FizzBuzz by Franklin Ikeh")