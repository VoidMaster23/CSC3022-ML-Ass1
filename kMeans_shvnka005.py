import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#defining the data
x = [2, 2, 8, 5, 7, 6, 1, 4]
y = [10, 5, 4, 8, 5, 4, 2, 9]

dataDict = {
    "X": x, "Y": y
}

data = pd.DataFrame(dataDict)

#display data
print("Input Data")
print(data) 