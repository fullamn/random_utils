import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 


data = pd.read_csv(".//files//D2.csv")

fig, ax = plt.subplots()

ax.plot(data['Frequency(ppm)'],data['Intensity'])

ax.set_xlim(20,-5)

plt.show()