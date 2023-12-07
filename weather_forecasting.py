import math

def check(temp,humid,wind):
    prediction=(0.5*(temp*temp))-(0.2*(humid))+(0.1*(wind))-15
    print(prediction)
    if prediction>=300:
        print("It is Sunny")
    elif prediction>200 and prediction<=300:
        print("It is Cloudy")
    elif prediction>100 and prediction<200:
        print("It is Rainy")
    elif prediction<=100:
        print("It is Stormy")


#driver 
temp=int(input("Enter temp :"))
humid=int(input("Enter humidity:"))
wind=int(input("Enter wind speed:"))
check(temp,humid,wind)