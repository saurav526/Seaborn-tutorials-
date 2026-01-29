import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_style("whitegrid")
sns.boxplot(
    data=tips, 
    x="day", 
    y="total_bill", 
    hue="smoker", 
    order=["Thur", "Fri", "Sat", "Sun"],
    saturation=1.0,
    width=0.6,
    hue_order=["No", "Yes"],
    fliersize=5,
    linewidth=3,
    orient="v",
    gap=0.1,
    palette="plasma",
    meanprops={"marker":"D", "markerfacecolor":"red", "markeredgecolor":"black", "markersize":8},
    showmeans=True,
    flierprops={"marker":"o", "markerfacecolor":"green", "markeredgecolor":"black", "markersize":5},
    showfliers=True,
    
    
    )  

plt.title("Box Plot of Total Bill by Day and Smoker Status")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True , linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
plt.savefig("boxplot_total_bill_by_day_and_smoker.png", dpi=300, bbox_inches='tight')
plt.show()