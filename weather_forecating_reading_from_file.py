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
    array=[]
    input_file="/Users/shashwat/Desktop/software eng/checkit.txt"
    f = open(input_file, "r")
    file=f
    for line in file:
        line=line.strip()
        line=int(line)
        array.append(line)
    tempreture=array[0]
    humidity=array[1]
    wind=array[2]
    print(check(tempreture,humidity,wind))