import pickle
import pandas as pd
import collections


location = "12859_2018_2167_MOESM1_ESM.xlsx"
df = pd.read_excel(location, columns = ['Disease', 'Target', 'Drug'], usecols = [0,1,2])

#sxesh disease_target
df_disease = df['Disease']
df_disease.tolist()
df_disease_unique = []
for x in df_disease:
	if x not in df_disease_unique:
		df_disease_unique.append(x)

print("Total disease nodes",len(df_disease_unique))



disease_target = {}
for x in df_disease_unique:
	a=df.loc[(df["Disease"] == x), "Target"].tolist()
	new = []
	for s in a:
		if s not in new:
			new.append(s)
	disease_target[x] = new

sum_disease_target_edges = 0
#number_of_edges_disease_target = []
for k in disease_target:
	length_of_each_key = len(disease_target[k])
	sum_disease_target_edges = sum_disease_target_edges + length_of_each_key
	#print(disease_target[k])
	#final_lenth = length_of_each_key + 0
	#number_of_edges_disease_target.append(length_of_each_key)

print("total multiple edges of disease target", sum_disease_target_edges)


#sxesh drug->target
df_drug = df['Drug']
df_drug.tolist()
df_drug_unique = []
for x in df_drug:
	if x not in df_drug_unique:
		df_drug_unique.append(x)

print("Total drug nodes",len(df_drug_unique))

drug_target = {}
for x in df_drug_unique:
	b=df.loc[(df["Drug"] == x), "Target"].tolist()
	new_1 = []
	for y in b:
		if y not in new_1:
			new_1.append(y)
	drug_target[x] = new_1



sum_of_drug_target_edges = 0
for k in drug_target:
	length_of_each_drug_target = len(drug_target[k])
	sum_of_drug_target_edges = sum_of_drug_target_edges + length_of_each_drug_target


print("total multiple edges of drug target", sum_of_drug_target_edges)


#sxesh drug_disease

df_disease_1 = df['Disease']
df_disease_1.tolist()
df_disease_1_unique = []
for x in df_disease_1:
	if x not in df_disease_1_unique:
		df_disease_1_unique.append(x)


disease_drug = {}
for x in df_disease_1_unique:
	c = df.loc[(df["Disease"] == x), "Drug"].tolist()
	new_2 = []
	for z in c :
		if z not in new_2:
			new_2.append(z)
	disease_drug[x] = new_2


sum_of_disease_drug_edges = 0
for k in disease_drug:
	length_of_each_disease_drug = len(disease_drug[k])
	sum_of_disease_drug_edges = sum_of_disease_drug_edges + length_of_each_disease_drug

df_target = df['Target']
df_target.tolist()
df_target_unique = []
for x in df_target:
	if x not in df_target_unique:
		df_target_unique.append(x)

print("Total targe nodes", len(df_target_unique))



print("total multiple edges of disease drug",sum_of_disease_drug_edges)
print("total multiple edges for this data set", sum_of_disease_drug_edges+sum_of_drug_target_edges+sum_disease_target_edges)
#triplet me leksilogia
t = (disease_target, drug_target, disease_drug)
