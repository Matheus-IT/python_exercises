import graphviz
from C45 import C45Classifier
import pandas as pd

data = pd.read_csv("38decision_tree/data.csv")
x = data.drop(["outcome"], axis="columns")
y = data["outcome"]

model = C45Classifier()
model.fit(x, y)
model.generate_tree_diagram(graphviz, "38decision_tree/graph")
