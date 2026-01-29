📊 Seaborn Functions vs Data Type
🔢 Numerical Data

(Used when values are numbers like marks, salary, age)

Function	Works On	One-line Use
histplot()	Numerical	Shows distribution using histogram

kdeplot()	Numerical	Shows smooth density curve

ecdfplot()	Numerical	Shows cumulative distribution
rugplot()	Numerical	Shows individual data points
lineplot()	Numerical vs Numerical	Shows trend over continuous data
scatterplot()	Numerical vs Numerical	Shows relationship between two numeric variables
regplot()	Numerical vs Numerical	Scatter plot with regression line
lmplot()	Numerical vs Numerical	Regression plot with grouping
heatmap()	Numerical matrix	Shows correlation or matrix values
pairplot()	Numerical (mainly)	Pairwise relationships
🏷️ Categorical Data

(Used when data has categories like gender, day, class)

Function	Works On	One-line Use
countplot()	Categorical	Counts frequency of categories
barplot()	Categorical vs Numerical	Shows mean or aggregate value
boxplot()	Categorical vs Numerical	Shows data spread and outliers
violinplot()	Categorical vs Numerical	Distribution + density
stripplot()	Categorical vs Numerical	Scatter for categorical data
swarmplot()	Categorical vs Numerical	Non-overlapping categorical scatter
pointplot()	Categorical vs Numerical	Shows mean with confidence interval
catplot()	Categorical	Figure-level categorical plots
🔁 Mixed Data (Numerical + Categorical)

(These handle both together)

Function	Input Type	One-line Use
scatterplot()	Num vs Num (+ category via hue)	Relationship with grouping
lineplot()	Num vs Num (+ category)	Trend comparison
barplot()	Cat vs Num	Aggregate comparison
boxplot()	Cat vs Num	Distribution by category
violinplot()	Cat vs Num	Density by category
pairplot()	Num (+ category hue)	Multi-variable comparison
jointplot()	Num vs Num	Relationship + distribution

🧮 Matrix / Multi-Variable Data

Function	Data Type	One-line Use
heatmap()	Numerical matrix	Correlation visualization
clustermap()	Numerical matrix	Heatmap with clustering
pairplot()	Numerical	Pairwise comparison
FacetGrid()	Any	Multiple plots by category

🎨 Styling / Utility (Any Data)

Function	Works On	Purpose
set()	Any	Set default theme
set_style()	Any	Background style
set_context()	Any	Scale for presentation
color_palette()	Any	Color selection
despine()	Any	Remove plot borders