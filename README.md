# Single Cell RNA-Seq Analysis (20440_Pset4)
This is a repository containing single cell RNA seq dataset and corresponding python scripts for analysis of gene expression patterns. The purpose of this repo is to analyze the differential gene expression across different cell types and utilize gene expression profiles to classify cell types and inform key driver genes to influence cell type transition. 

# Data
The data used in this repo is obtained from the human protein atlas (https://www.proteinatlas.org/download/rna_single_cell_type.tsv.zip). The data contains transcript expression levels summarized per gene in 76 cell types from 26 datasets. The data is store in the csv format, which includes Ensembl gene identifier ("Gene"), gene name ("Gene name"), analysed sample ("Cell type") and normalized expresion ("nTPM"). 
The data is stored in the Data sub-directory, where a csv file named rna_single_cell_type.csv contains the gene expression count for all genes across 34 cell types. 

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
