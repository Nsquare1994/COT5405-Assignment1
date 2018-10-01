import time
import random
import os
import psutil



# decide the size of the input numbers
size = input("Please input size: ")

#start counting
startTime = time.time()

#run 1000 times
for t in range(1000):

    # generate 2 random numbers
    number1 = []
    for n1 in range(int(size)):
        number1.extend(str(random.randint(0,9)))

    if(number1[-1] == '0'):
        number1 = number1[:-1]
        number1.append(str(random.randint(1,9)))

    #decide the sign, 0 for - , 1 for +
    number1Sign = random.randint(0,1)


    number2 = []
    for n2 in range(int(size)):
        number2.extend(str(random.randint(0,9)))

    if(number2[-1] == '0'):
        number2 = number2[:-1]
        number2.append(str(random.randint(1,9)))

    number2Sign = random.randint(0,1)

    #start of mulitplication
    multi = [0]*(len(number1)+len(number2)+1)
    #print(len(multi))
    for i in range(len(number1)):
        for j in range(len(number2)):
            multi[i+j] += int(number1[i])*int(number2[j])


    for d in range(len(multi)):
        if(multi[d]>9):
            multi[d+1]+=int(multi[d]/10)
            multi[d] = int(multi[d]%10)

    resultMulti = [str(item) for item in multi]


    # number1 = list(reversed(number1))
    # number2 = list(reversed(number2))
    resultMulti = list(reversed(resultMulti))


    # print(number1)
    # print(number2)
    # print(resultMulti)

    result = int(''.join(resultMulti))
    if((number1Sign+number2Sign) == 1):
        result = (-1)*result

    # print(result)

process = psutil.Process(os.getpid())
print('Memory used in bytes:')
print(process.memory_info().rss)

endTime = time.time()

print('Used time:')
print(endTime-startTime)
