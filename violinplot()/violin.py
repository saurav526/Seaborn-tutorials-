import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

tips = sns.load_dataset("tips")
sns.violinplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    split=True,     
    palette="Set2",
    scale="count",  
    linewidth=0.5,
    inner="quartiles",
    linecolor="black",
    alpha=1.0,
    order=["Thur", "Fri", "Sat", "Sun"],
    saturation=1.0,
    scale_hue=True,
)
plt.title("Violin Plot of Total Bill by Day and Sex")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True , linestyle='--', linewidth=0.5, color='gray', alpha=0.7)     


plt.show()