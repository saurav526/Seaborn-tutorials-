import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

tips = sns.load_dataset("tips")
print(tips.head())

sns.pairplot(
    data=tips[["total_bill", "tip", "size", "smoker", "day", "time", "sex"]],
    hue="sex",
    hue_order=["Male", "Female"],
    palette="coolwarm", 
    markers=["o", "s"],
    diag_kind="kde",
    # diag kind can be "hist" or "kde",REMARK: changed to "kde", or sccatter plot
    kind="scatter",
    height=2.5, 
    aspect=1.0,   
    plot_kws={"alpha":1.0, },
    diag_kws={"shade":False},
    
    x_vars=["total_bill", "tip"],
    y_vars=["size", "tip"]  



)
plt.title("Pair Plot of Tips Dataset")
plt.legend(title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True , linestyle='--', linewidth=0.5, color='gray', alpha=0.7)     
plt.show()