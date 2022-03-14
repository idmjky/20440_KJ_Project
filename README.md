# 20.440 Problem Set 4 Repository
This is a repository containing single cell RNA seq dataset and corresponding python scripts for analysis of gene expression patterns. 

# Data
The data is stored in the Data sub-directory, where a csv file named rna_single_cell_type.csv contains the gene expression count for all genes across 34 cell types. The data is obtained from the human protein atlas (https://www.proteinatlas.org/about/download)
# Folder Structure 
The master folder contains the README file, installation files, github attribute files and sub-folders. There are three sub folers named Data, Figure and Code. Data Folder Contains the csv file for the rna single cell gene expression data. Code folder contains the analysis code to reproduce the figure. Figure folder stores the output figure files. 
# Installation 
The packages can be installed by creating a fresh environment and running the following command
```
pip install -r requirements.txt

```
Alternatively, individual packages can be installed using anaconda with the following specifications:
matplotlib==3.3.2
pandas==1.1.3
seaborn==0.11.0

# Production
Clone the repository to local folder. Navigate to the corresponding folder by running cd 20440_KJ_Project/. Then navigate to the code folder by running cd Code/. Lastly, make sure you are in the right virtual python environment and running python Data_Plot.py
```
git clone https://github.com/idmjky/20440_KJ_Project.git
cd 20440_KJ_Project/
pip install -r requirements.txt
cd Code/
python Data_Plot.py

```