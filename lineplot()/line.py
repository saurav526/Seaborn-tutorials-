import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

tips = sns.load_dataset("penguins")
# print(tips)

sns.lineplot(
    data=tips,
    x="bill_depth_mm",
    y="bill_length_mm",
    hue="sex",
    dashes= True,
    style="sex",
    legend="full",
    ci="sd",
    
    palette="autumn",
    alpha=0.7,
    markers=[">", "^"],
    
)
plt.title("line Plot of Bill Depth vs Bill Length")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True , linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
plt.show()