import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

tips = sns.load_dataset("penguins")
# print(tips)

sns.histplot(
    data=tips,
    x="bill_depth_mm",
    bins=30,
    kde=True,
    hue="sex",
    multiple="stack",
   
    palette="Set2",
    log_scale=True,
    alpha=0.7,
    element="poly",
   
    #  The value for `element` must be one of ['bars', 'step', 'poly'],
)
plt.title("histogram Plot ")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True , linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
plt.show()