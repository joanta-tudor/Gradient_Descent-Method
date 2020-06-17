from GD import *
from Citire import *
import warnings; warnings.simplefilter('ignore')
from Normalizare import *
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
from Deseneaza import *

features=['Economy..GDP.per.Capita.', 'Freedom']

#citire date din fisiere si splituire
input,output=procesare("file.csv", features, 'Happiness.Score')

trainI, trainO, testI, testO=splituire(input, output)

# normalizare
trainInputs, testInputs=normalizareIn(trainI, testI,features)
trainOutputs, testOutputs=statisticalNormalisation(trainO, testO)
#tool data normalisation
# toolTrainInputs=tool_normalisation(trainI)

myGD=GD(len(trainInputs[0]))
myGD.train(trainInputs, trainOutputs)
# myGD.train(trainI, trainO)
model="The MANUAL BATCH learnt model: "+str(myGD.intercept)
for i in range(len(myGD.coef)):
    model+=" + "+str(myGD.coef[i])+" * x"+str(i+1)
print(model)
computedTestOutputs=myGD.predict(testInputs)
err=myGD.eroare(computedTestOutputs, testOutputs)

#tool
toolRegressor=linear_model.SGDRegressor(alpha=0.01)
for ep in range(1000):
    toolRegressor.partial_fit(trainInputs, trainOutputs)

model="The TOOL learnt model: "+str(toolRegressor.intercept_[0])
for i in range(len(toolRegressor.coef_)):
    model+=" + "+str(toolRegressor.coef_[i])+" * x"+str(i+1)
print(model)

toolComputed=toolRegressor.predict(testInputs)
print("Eroare tool regresor:"+str(mean_squared_error(toolComputed,testOutputs)))
print("Eroare tool pentru regresorul meu:"+str(mean_squared_error(computedTestOutputs,testOutputs)))
print("Eroare fara tool:"+str(err))

plt.plot(myGD.erori)
plt.show()

#fig=plt.figure()
#xx=fig.add_subplot(111,projection='3d')
#xx.scatter(testInputs,computedTestOutputs,testOutputs,c='r',marker='o')
#xx.plot(testInputs,computedTestOutputs,testOutputs)
#plt.show()

draw(testInputs, computedTestOutputs, testOutputs)



