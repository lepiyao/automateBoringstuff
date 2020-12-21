print('Hello World!')
print('What is your name?') #ask for the user name
myName = input()
print('It is good to meet you, ' + myName)
print('What is your age?') #ask for the user age
myAge = input()
if int(myAge) > 17 and int(myAge) < 60:
    print('Hi ' + myName + ', Welcome!')
elif int(myAge) > 60:
    print('You are too old!')
else:
    print('You are not old enough!')
