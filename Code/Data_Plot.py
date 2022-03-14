# Load Packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the dataset
df=pd.read_csv('../Data/rna_single_cell_type.csv')
fig, ax = plt.subplots(figsize=(20, 10))  # generate a figure and return figure and axis handle
#Obtain U2AF2 Gene Expression Patterns
df_u2af2=df[df['Gene name']=='U2AF2'].reset_index(drop=True)
#Generate Bar Plot
sns.barplot(x='Cell type',y='nTPM',data=df_u2af2,ax=ax)
#Plot the data
plt.yscale('log')
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.title('U2AF2 Gene Expression by Cell Type')
plt.tight_layout()
plt.savefig('../Figure/U2AF2 Gene Distribution by Cell Type.jpg')
