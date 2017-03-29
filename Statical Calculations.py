import math
import matplotlib.pyplot as plt

def average(val):
    sum_value = 0
    for i in range(len(val)):
        sum_value += val[i]
    mean = sum_value/len(val)
    return mean


def standard_deviation(mean,val):
    sum_value = 0
    for i in range(len(val)):
        sum_value += (val[i] - mean)**2
    sum_value = math.sqrt(sum_value/(len(val)-1))
    return sum_value


def standard_deviation2(val,mean):
    sum_value = 0
    for i in range(len(val)):
        sum_value += (val[i] - mean)**2
    sum_value = math.sqrt(sum_value/(len(val)))
    return sum_value


def q_test_last(val, q_crit):
    q_calculated = (val[len(val)-1] - val[len(val)-2])/(val[len(val)-1]-val[0])
    if q_crit < q_calculated:
        return True


def q_test_first(val, q_crit):
    q_calculated = (val[1]-val[0])/(val[len(val)-1]-val[0])
    if q_crit < q_calculated:
        return True


def gaussian_dist(mean,val):
    std = standard_deviation2(val,mean)
    x = mean - 4 * round(std, 2)
    counter = int(100*8*round(std, 2))
    ver = []
    hor = []
    for i in range(counter):
        f = (1 / ((2 * math.pi * (0.11595 ** 2)) ** 0.5)) * (
        math.exp((-(round(x, 2) - 2.47) ** 2) / (2 * 0.11595 * 0.11595)))
        ver.append(f)
        hor.append(x)
        x += 0.01

    plt.plot(hor, ver)
    plt.ylabel("Gaussian Distribution")
    plt.xlabel("Length - cm")
    plt.show()

f = open('input.txt')
all_values = [list(map(float, line.split(" "))) for line in iter(f)]  #read each line an creates a matrix
f.close()
for i in range(len(all_values)):
    orj_values = all_values[i]
    orj_values.sort()
    q_crit = 0.829
    if len(orj_values) > 3:
        if q_test_last(orj_values, q_crit):
            del orj_values[len(orj_values)-1]
            print("Last value removed.")
        elif q_test_first(orj_values, q_crit):
            del orj_values[0]
            print("First value removed.")

    mean = average(orj_values)
    std = standard_deviation(mean,orj_values)

    #gaussian_dist(mean, orj_values) #To see gaussian distribution curve romevo first #

    with open('file.txt', 'a') as f:
        print("Mean of data set is " + str(round(mean,3)), file=f)
        print("Standart Deviation of data set is " + str(round(std,3)), file=f)
        print("Last form of data set is " + str(orj_values), file=f)
