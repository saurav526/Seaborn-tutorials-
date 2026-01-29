import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

tips = sns.load_dataset("tips")
print(tips.head())

sns.stripplot(
    data=tips,
    x="day",    
    y="total_bill",
    hue="sex",
    hue_order   =["Male", "Female"],
    palette="plasma",         
    dodge=True,
    jitter=0.2,
    size=10,
    marker="o",
    alpha=1.0,
    edgecolor="r",
    linewidth=0.5,  
    
    orient="v",



)
plt.title("strip Plot of Tips Dataset")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True , linestyle='--', linewidth=0.5, color='gray', alpha=0.7)     
plt.show()