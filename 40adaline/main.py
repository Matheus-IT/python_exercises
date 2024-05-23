"""
Um sistema de gerenciamento automático de duas válvulas, situado a 500 metros de
um processo industrial, envia sinal codificado constituído de 4 grandezas {x1, x2, x3 e x4}, as quais
são necessárias para seus acionamentos. Uma mesma via de comunicação é utilizada para acionar
ambas as válvulas, sendo que existe um comutador localizado próximo a estas que deve decidir
se o sinal é para a válvula A ou B.
Utilizando-se o algoritmo de aprendizado regra Delta visando classificação de padrões
pelo Adaline, realize as seguintes atividades:
 Execute 5 treinamentos para a rede Adaline, iniciando-se os vetores de pesos (w) em
cada treinamento com valores aleatórios entre zero e um.
 Utilize um valor de taxa de aprendizado η = 0,0025 e uma precisão ε = 10-6
 Registre os resultados dos cinco treinamentos em uma tabela contendo:
o Pesos iniciais
o Pesos finais
o Número de épocas
"""

from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


class AdalineNeuron:
    def __init__(self, input_size, learning_rate=0.0025, max_epochs=1000):
        self.weights = np.random.uniform(0, 1, input_size)
        self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = 0
        self.max_epochs = max_epochs

    def train(self, X, y):
        cost = 0
        for _ in range(self.max_epochs):
            self.epochs += 1

            err = y - self.activation_function(X)

            # Update weights and bias using gradient descent
            self.bias += self.learning_rate * err.sum()
            self.weights += self.learning_rate * X.T.dot(err)

            cost = 1.0 / 2 * (err**2).sum()
            if cost < 4.26:
                break

    def predict(self, X):
        return np.where(self.activation_function(X) >= 0, 1, -1)

    def activation_function(self, X):
        return self.net_input(X)

    def net_input(self, X):
        return np.dot(X, self.weights) + self.bias


def calculate_accuracy(model, X, y):
    predictions = np.array([model.predict(x) for x in X])
    accuracy = np.mean(predictions == y)
    return accuracy


df = pd.read_csv("40adaline/training_data.txt")

train_df, test_df = train_test_split(df, test_size=0.2, random_state=2)

validation_df = pd.read_csv("40adaline/validation_data.txt")


for i in range(5):
    p = AdalineNeuron(input_size=4, learning_rate=0.0025)

    stats = {"pesos iniciais": p.weights.copy()}

    # train perceptron
    X = train_df[["x1", "x2", "x3", "x4"]].values
    y = train_df["d"].values
    p.train(X, y)

    stats["pesos finais"] = p.weights.copy()
    stats["épocas"] = p.epochs

    # test and calculate accuracy
    X = test_df[["x1", "x2", "x3", "x4"]].values
    y = test_df["d"].values
    accuracy = calculate_accuracy(p, X, y)
    stats["acurácia"] = accuracy

    # predict validation data values of "d"

    result = np.array(
        [p.predict(x) for x in validation_df[["x1", "x2", "x3", "x4"]].values]
    )
    validation_df[f"d{i+1}"] = result

    print("{")
    for e in stats.items():
        print(f"{e[0]}: {e[1]},")
    print("}")

print(validation_df)
