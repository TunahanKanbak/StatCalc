import math
import matplotlib.pyplot as plt
import numpy as np


def average(val):
    sum_value = 0
    for i in range(len(val)):
        sum_value += val[i]
    mean = sum_value/len(val)
    return mean


def standard_deviation(mean, val):
    sum_value = 0
    for i in range(len(val)):
        sum_value += (val[i] - mean)**2
    sum_value = math.sqrt(sum_value/(len(val)-1))
    return sum_value


def standard_deviation2(val, mean):
    sum_value = 0
    for i in range(len(val)):
        sum_value += (val[i] - mean)**2
    sum_value = math.sqrt(sum_value/(len(val)))
    return sum_value


def q_critical(data_set,conf_level):
    Q_test_confidence = {"90": [0.941, 0.765, 0.642, 0.560, 0.507, 0.468, 0.437, 0.412, 0.338, 0.3, 0.277, 0.26],
                         "95": [0.970, 0.829, 0.710, 0.625, 0.568, 0.526, 0.493, 0.466, 0.384, 0.342, 0.317, 0.298],
                         "99": [0.994, 0.926, 0.821, 0.740, 0.680, 0.634, 0.598, 0.568, 0.475, 0.425, 0.393, 0.372]}
    selected_conf_level = str(int(conf_level))
    Q_test_nums = Q_test_confidence[selected_conf_level]
    if len(data_set) <= 10:
        q_crit = Q_test_nums[len(data_set)-3]
        return q_crit
    elif len(data_set) <= 15:
        q_crit = Q_test_nums[8]
        return q_crit
    elif len(data_set) <= 20:
        q_crit = Q_test_nums[9]
        return q_crit
    elif len(data_set) <= 25:
        q_crit = Q_test_nums[10]
        return q_crit
    elif len(data_set) <= 30:
        q_crit = Q_test_nums[11]
        return q_crit

def q_test_last(val, q_crit):
    val.sort()
    q_calculated = (val[len(val)-1] - val[len(val)-2])/(val[len(val)-1]-val[0])
    if q_crit < q_calculated:
        return True


def q_test_first(val, q_crit):
    val.sort()
    q_calculated = (val[1]-val[0])/(val[len(val)-1]-val[0])
    if q_crit < q_calculated:
        return True


def gaussian_dist(mean, std, x):
    return np.exp(-np.power(x - mean, 2.) / (2 * np.power(std, 2.)))


def gaussian_plot(mean, name, std):
    x = np.linspace(round((mean - 3*std)), round((mean + 3*std)), num=60)
    y = gaussian_dist(mean, std, np.linspace(round((mean - 3*std)), round((mean + 3*std)), num=60))
    fig = plt.figure()
    plt.plot(x, y)
    plt.ylabel("Gaussian Distribution")
    plt.xlabel("Length - cm")
    fig.savefig(name)
    plt.close()
    print(name)


f_var = open('input.txt')
all_values = [list(map(float, line.split(" "))) for line in f_var]  #read each line an creates a data matrix
f_var.close()
f_name = open('names.txt')
names = [str(line.strip("\n")) for line in f_name]  #read each line an creates a name matrix
f_name.close()
for i in range(1, len(all_values)):
    count_q_last = 0
    count_q_first = 0
    q_crit = q_critical(all_values[i],all_values[0][0])

    while q_test_first(all_values[i], q_crit) or q_test_last(all_values[i], q_crit):
        if len(all_values[i]) > 2:
            if q_test_last(all_values[i], q_crit):
                del all_values[i][len(all_values[i])-1]
                count_q_last += 1
            elif q_test_first(all_values[i], q_crit):
                del all_values[i][0]
                count_q_first += 1

    mean = average(all_values[i])
    sample_std = standard_deviation(mean, all_values[i])
    population_std = standard_deviation2(all_values[i], mean)
    gaussian_plot(mean, names[i-1], population_std)

    f = open("output.txt", 'a')
    f.write("\n" + names[i-1] + "\n")
    f.write("Mean of data set is " + str(round(mean,3)) + "\n")
    f.write("Sample Standard Deviation(N-1) of data set is " + str(round(sample_std,3))+ "\n")
    f.write("Population Standard Deviation(N) of data set is " + str(round(population_std, 3))+ "\n")
    f.write("Number of successive Q-Test for right end of the data set is " + str(count_q_last)+ "\n")
    f.write("Number of successive Q-Test for left end of the data set is " + str(count_q_first)+ "\n")
    f.write("Last form of data set is " + str(all_values[i])+ "\n")
    f.close()
