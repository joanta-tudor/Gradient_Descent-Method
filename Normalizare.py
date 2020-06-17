from sklearn.preprocessing import StandardScaler

# statistical normalisation (centered around meand and standardisation)
def statisticalNormalisation(antr, test):
    meann = sum(antr) / len(antr)
    #standard deviation to the mean of some data
    stdDev = (1 / len(antr) * sum([(feat - meann) ** 2 for feat in antr])) ** 0.5
    normalisedTrain = [(feat - meann) / stdDev for feat in antr]
    normalisedTest = [(feat - meann) / stdDev for feat in test]
    return normalisedTrain, normalisedTest


    # extract a particular feature (column)
def extractF(data,nume,numeF):
        pos = nume.index(numeF)
        return [float(x[pos]) for x in data]

def normalizareTool(data):
        scaler=StandardScaler()

        if isinstance(data[0], list):
            scaler.fit(data)
            normalizat = scaler.transform(data)
        else:
            data_train = [[d] for d in data]
            scaler.fit(data_train)
            normalizat = scaler.transform(data_train)
            normalizat = [el[0] for el in normalizat]

        return normalizat

def normalizareIn(antr,test,numeF):
        normalizareIn_train = [[] for _ in range(len(antr))]
        normalizareIn_test = [[] for _ in range(len(test))]

        j = 0

        while (j < len(numeF)):
            antrF = extractF(antr, numeF, numeF[j])
            testF = extractF(test, numeF, numeF[j])
            normalizareIn_trainF, normalizareIn_testF = statisticalNormalisation(antrF, testF)
            for i in range(len(normalizareIn_trainF)):
                normalizareIn_train[i].append(normalizareIn_trainF[i])
            for i in range(len(normalizareIn_testF)):
                normalizareIn_test[i].append(normalizareIn_testF[i])
            j += 1
        return normalizareIn_train, normalizareIn_test