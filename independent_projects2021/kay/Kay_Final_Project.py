#!/usr/bin/env python

import numpy as np
import pandas as pd
import re

#set working directory
cd /Users/erickarkay/Desktop/dissertation /data spreadsheets/chem spectra/alex_11_23_2021

#read in csv file
GC_df = pd.read_csv('HempNE_total GC ammended_ready for R.csv')

GC_df.head()

#select only plant info and compounds (not insects) column 2 (Field.type) and 13-79 
# using iloc and np.r_ to select both individ columns in addition to a range of columns
#np.r_ Translates slice objects to concatenation along the first axis.
chem_div_df = GC_df.iloc[:, np.r_[0, 2, 3, 13:68]]
chem_div_df.head()	#went from 79 columns to 58

#Convert intergers to float: compound values are abundance or area under the peaks
#couldnt figure out how to convert dtypes of multiple columns at once w/out specifying
#each column separately, stackoverflow post said no way to specify contiguos columns to astype (2020)
chem_div_df.dtypes

#see which columns are dtypes: some float and some int
chem_div_df.info()

#convert all int to float with.astypes
chem_div_df = chem_div_df.astype({'41': 'float64', 
'43': 'float64', '45': 'float64', '48': 'float64',
'49': 'float64', '50': 'float64', '51': 'float64',
'52':'float64','53': 'float64','55': 'float64'})
chem_div_df.info()

#Both hexane and MeOH extracts for GC, sometimes same compound in both extractions
#sum same cmpd_species for each Rand.ID for MeOH and Hexane
chem_div_df=chem_div_df.groupby(['Rand.ID','Location','Field.type'], as_index = False).sum()

#add additional column for total cmpd abund. for each row/plant use in alpha div. calcs
#N in denominator of pi variable
chem_div_df['cmpd_abund_tot']=chem_div_df.iloc[:,2:58].sum(axis=1)
#check for new column
chem_div_df.head()

#check for typos in Field_type and Location columns
chem_div_df['Field.type'].unique()
chem_div_df['Location'].unique()

#add column for total individ species for each plant
#subset only cmpd columns to get a count of the number of species per plant
#this took me forever for some reason. sure theres a better way to do it
sp_ct_df= chem_div_df.iloc[:, np.r_[3:58]]
#count numbers greater than 0 in columns row wise and save to column named 'count'
#ne means not equal
columns = ['1','2','3','4','5','6','7','8','9','10','11',
'12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28',
'29','30','31','32','33','34','35','36','37', '38','39','40','41','42','43','44','45',
'46','47','48','49','50','51','52','53', '54','55']

sp_ct_df['count'] = sp_ct_df[columns].ne(0).sum(axis=1)
#extract 'count' column and join with chem_div_df
#create object of just count column from sp_ct_df
count=sp_ct_df["count"]
count
#join count object to chem_div_df
chem_div_df = chem_div_df.join(count)
chem_div_df

#change format from wide to long using pd.melt
#var_name=new column for long format and value_name for its associated values
chem_div_lg_df = pd.melt(chem_div_df, id_vars=['Rand.ID', 'Field.type', 'Location',
'cmpd_abund_tot', 'count'],value_vars=['1', '2', '3','4','5','6','7','8','9','10','11',
'12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28',
'29','30','31','32','33','34','35','36','37', '38','39','40','41','42','43','44','45',
'46','47','48','49','50','51','52','53','54','55'], 
var_name = 'cmpd_species', value_name = 'cmpd_spec_abundance')
chem_div_lg_df

#reorder columns for more logical order
chem_div_lg_df = chem_div_lg_df[['Rand.ID', 'Field.type', 'Location', 'cmpd_species', 
'cmpd_spec_abundance', 'cmpd_abund_tot', 'count']]
#rename count column to numb_spec_per_plant which is number of cmpd species per plant
chem_div_lg_df.rename(columns={'count':'numb_spec_per_plant'}, inplace=True)
chem_div_lg_df.head()
chem_div_lg_df.info() #have 2200 rows now

#make columns for div indexes
#left of equal sign creates column and to the right calcs values for new column
chem_div_lg_df["Pi"]=chem_div_lg_df["cmpd_spec_abundance"] / chem_div_lg_df["cmpd_abund_tot"]
chem_div_lg_df["Pi2"]=chem_div_lg_df["Pi"]*chem_div_lg_df["Pi"]
chem_div_lg_df["Ln_Pi"]=np.log(chem_div_lg_df["Pi"])
chem_div_lg_df["Pi_Ln_Pi"]=chem_div_lg_df["Ln_Pi"]*chem_div_lg_df["Pi"]
chem_div_lg_df.head()

#create summary table for each plant to be used in H and D calcs
#groups rows by plant ID (Rand.ID) and sums their totals using sum in reset_index()
# Simpsons: grouping by Rand.ID means I can get the sum abundance of each cmpd fro Pi2
Div_summary_df = chem_div_lg_df.groupby(['Rand.ID', 'Location', 'Field.type',
'numb_spec_per_plant'])['Pi2'].sum().reset_index()
Div_summary_df
#rename Pi2 column to Sum_Pi2 to reflect the above summation of the values 
Div_summary_df.rename(columns={'Pi2': "Sum_Pi2"}, inplace=True)


Div_summary_df.head()

#Shannons: sum of Pi_Ln_Pi for each plant for use in Shannon calcs 
#Sum_Pi_Ln_Pi = chem_div_lg_df.groupby(['Rand.ID'])['Pi_Ln_Pi'].sum().reset_index()
#initially used above line but instead am just creating column to be added to the above df
#using below code because I need to take the negative of the values
Sum_Pi_Ln_Pi = chem_div_lg_df.groupby(['Rand.ID'])['Pi_Ln_Pi'].sum().reset_index()
Sum_Pi_Ln_Pi

#H calc
#Sum_Pi2["H"] = Sum_Pi_Ln_Pi[:,1] *= -1
#above returned syntax error for use of asterick
#do to natura log values are negative
H_Sum_Pi_Ln_Pi = np.negative(Sum_Pi_Ln_Pi)
H_Sum_Pi_Ln_Pi
#this made all column values negative which is ok since I'm just 
#going to extract Pi_Ln_Pi column

#1st extract Shannon column (2nd column) from H_Sum_Pi_Ln_Pi df
H_Sum_Pi_Ln_Pi=H_Sum_Pi_Ln_Pi["Pi_Ln_Pi"]
H_Sum_Pi_Ln_Pi

# & add to Div_Summary_df 
Div_summary_df = Div_summary_df.join(H_Sum_Pi_Ln_Pi)
Div_summary_df	#Shannons column still name Pi_Ln_Pi so rename
#rename extracted column
Div_summary_df.rename(columns={'Pi_Ln_Pi':'H_Sum_Pi_Ln_Pi'}, inplace=True)
Div_summary_df

#create new columns H_max and Equitability
Div_summary_df["H_max"]=np.log(Div_summary_df["numb_spec_per_plant"])
#Equitab column shows us how diverse the plant is with 1 the most diverse and 0 no diversity
Div_summary_df["Equitab"]=Div_summary_df["H_Sum_Pi_Ln_Pi"]/Div_summary_df["H_max"]

#Simpsons create new column in Div_summary_df and add Simpsons calcs
#using data previously calc-ed in Pi2 column in Sum-Pi2 df
Div_summary_df["Simpsons"]=1/Div_summary_df["Sum_Pi2"]
Div_summary_df

#save df's to computer
Div_summary_df.to_csv('NE_GC_hemp.Diversity_summary_df.csv', index=False)
chem_div_lg_df.to_csv('NE_GC_hemp.longformat.csv', index=False)

import matplotlib.pyplot as plt 



#run shannon and simpson in R and compar values

#run stats to see if treatment affects diverstiy

#box plots using matplot
	



###################junk##############################
#Simpsons create new column in Div_summary_df and add Simpsons calcs
#using data previously calc-ed in Pi2 column in Sum-Pi2 df


#calc shannons hill number which is the exp(Shannons) 
Div_summary_df["Hills_Shannon"]=np.exp(Div_summary_df["Shannons"])

#calc Simpsons Hill number

Div_summary_df["Hills_Simpsons"]=1/(1-Div_summary_df["Simpsons"])

		























