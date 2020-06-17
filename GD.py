from random import random

class GD:
    def __init__(self,n,epoci=100,rata_inv=0.01):
        self.epoci=epoci
        self.rata_inv = rata_inv
        self.n = n
        self.erori=[]

    def predict(self, input):
        return [self.compute(x) for x in input]

    def compute(self, input):
        output = self.intercept
        for i in range(len(input)):
            output += self.coef[i] * input[i]
        return output

    def eroare(self, computed, real):
        eroare = 0.0
        for x, y in zip(computed, real):
            eroare += (x - y) ** 2
        eroare /= len(computed)
        return eroare

    def train(self, input, output):
        self.coef = [random() for _ in range(self.n)]
        self.intercept = random()
        for ep in range(0, self.epoci):
            #coeficient de eroare
            coeficient = 0.0
            error_intercept = 0.0
            for i in range(len(input)):
                computed = self.compute(input[i])
                for j in range(len(input[0])):
                    coeficient += (computed - output[i]) * input[i][j]
                    error_intercept += (computed - output[i])
            self.erori.append(error_intercept)

            for j in range(0, len(input[0])):
                self.coef[j] = self.coef[j] - self.rata_inv * coeficient / len(input)
            self.intercept -= self.rata_inv * error_intercept / len(input)