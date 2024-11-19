import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib.pyplot import figure
tip_df=pd.read_csv("tips.csv")
print(tip_df.head())
fig=plt.figure(figsize=(5,5))
plt.title("gender wise count plot graph")
sb.countplot(x="sex",data=tip_df,hue="sex")
plt.show()

