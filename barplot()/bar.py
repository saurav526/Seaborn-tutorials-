import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

tips = sns.load_dataset("penguins")
# print(tips)

sns.barplot(
    data=tips,
    x="island",
    y="bill_length_mm",
    hue="sex",
    ci=100,
    legend="full",
    n_boot=1000,
    palette="autumn",
    estimator=sum,
    alpha=0.7,
    order=["Biscoe", "Dream", "Torgersen"],
    
)
plt.title("bar Plot of Bill Depth vs Bill Length")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True , linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
plt.show()