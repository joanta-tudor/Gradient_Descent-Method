import numpy as np
import csv

def procesare(filename,input,output):
        data=[]
        nume=[]
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            ct = 0
            for row in csv_reader:
                if ct == 0:
                    nume = row
                else:
                    data.append(row)
                ct += 1
        selectat=[]
        for x in input:
            selectat.append(nume.index(x))
        intrare=[]
        for i in range(len(data)):
            v=[]
            for j in range(len(selectat)):
                v.append(float(data[i][selectat[j]]))
            intrare.append(v)
        outt=nume.index(output)
        iesire = [float(data[i][outt]) for i in range(len(data))]
        return intrare,iesire

def splituire(input,output):
        index = [i for i in range(len(input))]
        antrs = np.random.choice(index, int(0.8 * len(input)), replace=False)
        tests = [i for i in index if not i in antrs]

        antrI = [input[i] for i in antrs]
        antrO = [output[i] for i in antrs]

        testI = [input[i] for i in tests]
        testO = [output[i] for i in tests]
        return antrI, antrO, testI, testO