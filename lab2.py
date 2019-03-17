from functools import reduce
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def sumProizv(xCollection, yCollection):
    return reduce(lambda x, y: x + y, [xCollection[i] * yCollection[i] for i in range(0, len(xCollection) if (len(xCollection) <= len(yCollection)) else len(yCollection))])

def sumQuard(collection):
    return sum(map(lambda x: x**2, collection))

def average(collection):
    sum = 0
    for i in collection:
        sum += i
    return sum/len(collection)

if __name__ == "__main__":

    data = pd.read_csv('forestfires.csv', index_col=False, header=0)
    x = data.wind.values
    y = data.ISI.values

    tTabl = 2.0
    COUNT = len(x)

    MATOZHX = sum(x) / COUNT
    DISPERSX = sum([(i - MATOZHX) ** 2 for i in x]) / COUNT
    print(DISPERSX)
    STANDOTKLX = sum([(i - MATOZHX) ** 2 for i in x]) / (COUNT - 1)
    QUARDOTKLX = math.sqrt(DISPERSX)
    print("quardotkl = " + str(QUARDOTKLX))
    MARKQUARDOTKLX = math.sqrt(STANDOTKLX)
    DELTAX = tTabl * (MARKQUARDOTKLX / math.sqrt(COUNT))

    MATOZHY = sum(y) / COUNT
    DISPERSY = sum([(i - MATOZHY) ** 2 for i in y]) / COUNT
    STANDOTKLY = sum([(i - MATOZHY) ** 2 for i in y]) / (COUNT - 1)

    Tn = (MATOZHX - MATOZHY)/math.sqrt(DISPERSX/COUNT + DISPERSY/COUNT)
    print("Tn = " + str(Tn))

    #level of important
    a = 0.95
    print("Известная дисперсия:")
    if abs(Tn) > DISPERSX/DISPERSY : # Fisher
        print("Гипотеза опровергнута")
    else:
        print("Гипотеза подтверждена")

    Ssmesh = (((COUNT - 1) * STANDOTKLX + (COUNT - 1) * STANDOTKLY) / (COUNT + COUNT - 2)) * (2 / COUNT)

    Tun = (MATOZHX - MATOZHY) / math.sqrt(Ssmesh)

    Tkr = math.sqrt(-2 * math.log(math.sqrt(2*math.pi) * (1 - a)))

    print("Неизвестная дисперсия:")

    print("T = " + str(Tun))
    print("Tkrit = " + str(Tkr))

    if (abs(Tun) > Tkr) :
        print("Гипотеза опровергнута")
    else:
        print("Гипотеза подтверждена")
print("INTERVAL: ( " + str(MATOZHX) + " - " + str(DELTAX) + "; " + str(MATOZHX) + " + " + str(DELTAX) + ")")