# x = input("Please enter your first number: ")
# y = input("Second number please: ")
# print(x + y)

height = int(input('Enter your height in inches: '))
weight = int(input('Enter your weight in lbs: '))

bmi = (weight/(height**2))*703
print('Your BMI is: ' + str(bmi))

if(bmi < 20):
    print("Awsome.")
elif(bmi <30):
    print("I'd work out a bit if I were you.")
elif(bmi < 40):
    print("Uh oh... better see a doctor.")
elif(bmi < 50):
    print("Yeah, that's uhh, that's not good homie.")
else:
    print("Yo you got issues, seek help!")

