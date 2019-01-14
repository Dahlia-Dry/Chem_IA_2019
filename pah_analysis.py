import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_txt(filename):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "E", "-", "."]
    f = open(filename, mode = "r")
    f.readline()
    f.readline()
    f.readline()
    valid = False
    prevValid = False
    c = ""
    data = ""
    secondPart = False
    secondThing = False
    fulldata = {'freq':[], 'intensity': [], 'other-freq': [], 'abs': []}
    while True:
        c = f.readline()
        for i in c:
            for j in numbers:
                if j == i:
                    valid = True
                    break
            if valid:
                data = data + i
            elif not valid and prevValid and not secondThing and not secondPart:
                fulldata['freq'].append(data)
                secondThing = True
                data = ""
            elif not valid and prevValid and secondThing and not secondPart:
                fulldata['intensity'].append(data)
                secondThing = False
                data = ""
            elif not valid and prevValid and not secondThing and secondPart:
                fulldata['abs'].append(data)
                secondThing = True
                data = ""
            elif not valid and prevValid and secondThing and secondPart:
                fulldata['other-freq'].append(data)
                secondThing = False
                data = ""
            if i == ")":
                secondPart = True
            prevValid = valid
            valid = False
        if not c:
            break
    return fulldata


anthracene = read_txt("phenanthrene.txt")
print(anthracene['freq'])
x = np.array(anthracene['other-freq'])
y = np.array(anthracene['abs'])
new_x = []
new_y = []
for i in range(len(anthracene['other-freq'])):
    if i % 2 == 0:
        new_x.append(x[i])
        new_y.append(y[i])
plt.bar(new_x,height = new_y)

plt.show()



