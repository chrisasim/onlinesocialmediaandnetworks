import pickle
import pandas as pd
import collections


location = "normal_tissue_xls_2.xlsx"
df = pd.read_excel(location, columns = ['Gene', 'Gene name', 'Tissue', 'Cell type'], usecols = [0,1,2,3])


#sxesh gene_name_tissue
df_gene = df['Gene name']
df_gene.tolist()
df_gene_unique = []
for x in df_gene:
	if x not in df_gene_unique:
		df_gene_unique.append(x)
print("Total gene nodes", len(df_gene_unique))

gene_name_tissue = {}
for x in df_gene_unique:
	a = df.loc[(df["Gene name"] == x), "Tissue"].tolist()
	new = []
	for s in a:
		if s not in new:
			new.append(s)
	gene_name_tissue[x] = new

sum_of_gene_name_tissue_edges = 0

for k in gene_name_tissue:
	length_gene_name_tissue = len(gene_name_tissue[k])
	sum_of_gene_name_tissue_edges = sum_of_gene_name_tissue_edges + length_gene_name_tissue

print("total multiple edges gene name tissue", sum_of_gene_name_tissue_edges)

#sxesh tissue_cell type
df_tissue = df['Tissue']
df_tissue.tolist()
df_tissue_unique = []
for y in df_tissue:
	if y not in df_tissue_unique:
		df_tissue_unique.append(y)

print("total tissue nodes",len(df_tissue_unique))

tissue_celltype = {}
for y in df_tissue_unique:
	b = df.loc[(df["Tissue"] == y), "Cell type"].tolist()
	new_1 = []
	for s in b:
		if s not in new_1:
			new_1.append(s)
	tissue_celltype[y] = new_1


sum_of_tissue_celltype = 0
for k in tissue_celltype:
	length_tissue_celltype = len(tissue_celltype[k])
	sum_of_tissue_celltype = sum_of_tissue_celltype + length_tissue_celltype
print("total multiple edges tissue cell type", sum_of_tissue_celltype)


#sxesh celltype_gene
df_celltype = df['Cell type']
df_celltype.tolist()
df_celltype_unique = []
for z in df_celltype:
	if z not in df_celltype_unique:
		df_celltype_unique.append(z)

print("total cell type nodes", len(df_celltype_unique))


celltype_gene = {}
for z in df_celltype_unique:
	c = df.loc[(df["Cell type"] == z), "Gene name"].tolist()
	new_2 = []
	for s in c:
		if s not in new_2:
			new_2.append(s)
	celltype_gene[z] = new_2


sum_of_celltype_gene = 0

for k in celltype_gene:
	length_celltype_gene = len(celltype_gene[k])
	sum_of_celltype_gene = sum_of_celltype_gene + length_celltype_gene

print("total multiple edges of celltype gene",sum_of_celltype_gene)

print("total edges", sum_of_celltype_gene+sum_of_tissue_celltype+sum_of_gene_name_tissue_edges)

t1 = (gene_name_tissue,tissue_celltype, celltype_gene)



'''
disease_target = {}
for x in df_disease_unique:
	a=df.loc[(df["Disease"] == x), "Target"].tolist()
	new = []
	for s in a:
		if s not in new:
			new.append(s)
	disease_target[x] = new



#sxesh drug->target
df_drug = df['Drug']
df_drug.tolist()
df_drug_unique = []
for x in df_drug:
	if x not in df_drug_unique:
		df_drug_unique.append(x)

drug_target = {}
for x in df_drug_unique:
	b=df.loc[(df["Drug"] == x), "Target"].tolist()
	new_1 = []
	for y in b:
		if y not in new_1:
			new_1.append(y)
	drug_target[x] = new_1


#sxesh drug_disease

df_drug = df['Drug']
df_drug.tolist()
df_drug_unique = []
for x in df_drug:
	if x not in df_drug_unique:
		df_drug_unique.append(x)
drug_disease = {}
for x in df_drug_unique:
	c = df.loc[(df["Drug"] == x), "Disease"].tolist()
	new_2 = []
	for z in c :
		if z not in new_2:
			new_2.append(z)
	drug_disease[x] = new_2



#triplet me leksilogia
t = disease_target, drug_target, drug_disease
'''
