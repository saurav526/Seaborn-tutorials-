import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

tips = sns.load_dataset("penguins")
# print(tips)
m = {"Male": "*", "Female": "o"}
sns.scatterplot(
    data=tips,
    x="bill_depth_mm",
    y="bill_length_mm",
    hue="sex",
    style="sex",
    size="flipper_length_mm",
    sizes=(20, 200),
    palette="Set2",
    alpha=0.7,
    marker=">",
    
)
plt.title("Scatter Plot of Bill Depth vs Bill Length")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True)
plt.show()


