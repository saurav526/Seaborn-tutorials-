import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

tips = sns.load_dataset("tips")
sns.countplot(
    data=tips,
    x="day",
    hue= "sex",
    color="lightblue",
    
    saturation=1.0,

)
plt.title("Count Plot of Total Bill by Day and Sex")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)                    
plt.grid(True , linestyle='--', linewidth=1, color='red', alpha=0.7)
plt.show()