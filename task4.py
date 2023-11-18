from matplotlib import pyplot
import numpy
list_oddnum=[]
list_evennum=[]
count=0
with open("sequence.txt","r") as file :
    for line in file:
        count+=1
        if count % 2==0:
            list_evennum.append(float(line.rstrip()))
        else:
            list_oddnum.append(float(line.rstrip()))
average_even=0
for i in list_evennum:
    average_even+=i/125
average_odd=0
for i in list_oddnum:
    average_odd+=i/125
number=numpy.array(["среднее чётных чисел","среднее нечётных чисел"])
value=numpy.array([average_even,  average_odd])
pyplot.bar(number, value)
pyplot.xlabel("виды чисел")
pyplot.ylabel("значения")
pyplot.show()
