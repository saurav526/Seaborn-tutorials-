import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Set style
sns.set_style("whitegrid")

# Swarm plot
sns.swarmplot(
    data=tips,
    x="day",                 # categorical variable
    y="total_bill",          # numerical variable
    hue="sex",               # grouping by category
    hue_order=["Male", "Female"],
    palette="plasma",        # color palette
    dodge=True,              # separate hue categories
    size=6,                # size of points
    marker="o",              # marker shape
    alpha=1.0,               # transparency
    edgecolor="red",       # marker border color
    linewidth=1,           # marker border width
   
    orient="v"               # vertical orientation
)


plt.title("Swarm Plot of Total Bill by Day and Sex")
plt.legend(title="Sex", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.show()
