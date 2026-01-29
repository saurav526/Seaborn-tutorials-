import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

var =np.linspace(0,10,100).reshape(10,10)
print(var)

sns.heatmap(var, annot=True,vmin=0,vmax=30, cmap="plasma",fmt=".1f",
            annot_kws={"size":10, "weight":"light", "color":"white"}, linewidth=3,linecolor='red', 
            cbar=True, cbar_kws={"orientation":"vertical", "shrink":0.5, "label":"Color Bar"}, square=True,xticklabels=True, yticklabels=True ,
            cbar_ax=None, robust=False, mask=None)

plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Heatmap Example")
plt.show()

