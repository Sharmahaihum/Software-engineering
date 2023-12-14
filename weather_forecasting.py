import math
def call(prediction):
    if prediction>=300:
        return "It is Sunny"
    elif prediction>200 and prediction<=300:
        return "It is Cloudy"
    elif prediction>100 and prediction<200:
        return "It is Rainy"
    elif prediction<=100:
        return "It is Stromy"
def check(temp,humid,wind):
    prediction=(0.5*math.pow(temp,2))-(0.2*(humid))+(0.1*(wind))-15
    result=call(prediction)
    return result
        
#driver
if __name__ == "__main__":
    temp=int(input("Enter temp :"))
    humid=int(input("Enter humidity:"))
    wind=int(input("Enter wind speed:"))
    final=check(temp,humid,wind)
    input_file="/Users/shashwat/Desktop/practice problems /check.txt"
    f = open(input_file, "r")
    print(f.read(),final)
    