import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('rna_single_cell_type.csv')
fig, ax = plt.subplots(figsize=(20, 10))  # generate a figure and return figure and axis handle
df_u2af2=df[df['Gene name']=='U2AF2'].reset_index(drop=True)
sns.barplot(x='Cell type',y='nTPM',data=df_u2af2,ax=ax)
plt.yscale('log')
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()