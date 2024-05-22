"""
Pela análise do processo de destilação fracionada do petróleo observou-se que determinado óleo
poderia ser classificado em duas classes de pureza (P1 e P2)
Utilizando o algoritmo supervisionado de Hebb para classificação de padrões, e assumindo-se a
taxa de aprendizagem como 0,01, faça as seguintes atividades:
 Execute 5 treinamentos para a rede Perceptron, iniciando-se os vetores de pesos (w)
em cada treinamento com valores aleatórios entre zero e um.
 Registre os resultados dos cinco treinamentos em uma tabela contendo:
o Pesos iniciais
o Pesos finais
o Número de épocas
"""

from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, max_epochs=500):
        self.weights = np.random.uniform(0, 1, input_size)
        self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = 0
        self.max_epochs = max_epochs

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        z = np.dot(x, self.weights) + self.bias
        # translate the activation function to the actual value
        return np.where(self.activation_function(z) == 1, 1, -1)

    def train(self, X, y):
        for _ in range(self.max_epochs):
            ready_to_stop = True
            self.epochs += 1

            for i in range(len(X)):
                error = y[i] - self.predict(X[i])
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

                if error != 0:
                    ready_to_stop = False
            if ready_to_stop:
                break


def calculate_accuracy(model, X, y):
    predictions = np.array([model.predict(x) for x in X])
    accuracy = np.mean(predictions == y)
    return accuracy


df = pd.read_csv("39perceptron/training_data.txt")

train_df, test_df = train_test_split(df, test_size=0.2, random_state=1)

p = Perceptron(input_size=3, learning_rate=0.01)

stats = {"initial_weights": p.weights.copy()}

# train perceptron
X = train_df[["x1", "x2", "x3"]].values
y = train_df["d"].values
p.train(X, y)

stats["final_weights"] = p.weights.copy()
stats["epochs"] = p.epochs

# test and calculate accuracy
X = test_df[["x1", "x2", "x3"]].values
y = test_df["d"].values
accuracy = calculate_accuracy(p, X, y)
stats["accuracy"] = accuracy

# predict validation data values of "d"
validation_df = pd.read_csv("39perceptron/validation_data.txt")
result = np.array([p.predict(x) for x in validation_df.values])
validation_df["d"] = result

print(validation_df)
print()

print("{")
for e in stats.items():
    print(f"{e[0]}: {e[1]},")
print("}")
