# Homework 4 - pandas (YOUR NAME HERE)
### due 03/10/2021, to be turned on github  

<br>

Use this notebook and prompts to complete the homework. Throughout there will be hints and code provided to

### Things you will need:
- Install os, NumPy, pandas
- states_covid.csv
- Bloom_etal_2018_Reduced_Dataset.csv
- logfiles.tgz (or some other multiple file dataset)

**hint:** change your working directory to a directory for just this homework. Edit path below and run.


```python
hw_dir = "/data/gpfs/home/tfaske/g/DataScience/Data_Science_For_Biology_II/Part.II_PythonProgramming/pandas/" #"your/homework/path/here"
```


```python
cd $hw_dir
```

    /data/gpfs/assoc/parchmanlab/tfaske/DataScience/Data_Science_For_Biology_II/Part.II_PythonProgramming/pandas


**import packages & check required datasets**


```python
import os
import numpy as np
import pandas as pd
```


```python
assert os.path.exists(os.path.join(hw_dir,'states_covid.csv')), 'states_covid.csv does not exist' 
```


```python
assert os.path.exists(os.path.join(hw_dir,'Bloom_etal_2018_Reduced_Dataset.csv')), 'Bloom_etal_2018_Reduced_Dataset.csv does not exist'
```


```python
!tar -xvzf logfiles.tgz
log_dir = os.path.join(hw_dir,'logfiles')
assert os.path.exists(log_dir), 'log_dir does not exist' 
```

    logfiles/
    logfiles/1901302136_H15_D_14.txt.txt
    logfiles/1901302243_H5_S_14.txt.txt
    logfiles/1901302110_H13_S_14.txt.txt
    logfiles/1901302121_H8_S_14.txt.txt
    logfiles/1901302228_H4_D_14.txt.txt
    logfiles/1901302223_H16_S_14.txt.txt
    logfiles/1901302117_H15_S_14.txt.txt
    logfiles/1901302202_H16_S_14.txt.txt
    logfiles/1901302115_H1_S_14.txt.txt
    logfiles/1901302158_H9_S_14.txt.txt
    logfiles/1901302237_H10_D_14.txt.txt
    logfiles/1901302118_H1_D_14.txt.txt
    logfiles/1901302120_H5_D_14.txt.txt
    logfiles/1901302134_H13_D_14.txt.txt
    logfiles/1901302109_H7_S_14.txt.txt
    logfiles/1901302236_H17_D_14.txt.txt
    logfiles/1901302141_H19_S_14.txt.txt
    logfiles/1901302146_H14_D_14.txt.txt
    logfiles/1901302137_H18_S_14.txt.txt
    logfiles/1901302108_H7_D_14.txt.txt
    logfiles/1901302240_H8_D_14.txt.txt
    logfiles/1901302212_H9_D_14.txt.txt
    logfiles/1901302214_H19_D_14.txt.txt
    logfiles/1901302122_H3_D_14.txt.txt
    logfiles/1901302138_H11_D_14.txt.txt
    logfiles/1901302150_H14_S_14.txt.txt
    logfiles/1901302194_H10_S_14.txt.txt
    logfiles/1901302217_H18_D_14.txt.txt
    logfiles/1901302227_H11_S_14.txt.txt
    logfiles/1901302235_H6_S_14.txt.txt
    logfiles/1901302203_H7_S_14.txt.txt
    logfiles/1901302241_H2_D_14.txt.txt
    logfiles/1901302225_H12_D_14.txt.txt
    logfiles/1901302119_H4_S_14.txt.txt
    logfiles/1901302224_H3_S_14.txt.txt
    logfiles/1901302157_H12_S_14.txt.txt


### Task 1 - DataFrame manipulation

Using **states_covid.csv**, we are going to read the data in as a DataFrame to manipulate, subset, and filter in various ways. 

**1.1 Read in states_covid.csv with date as a "date" dtype, and only columns consisting of the hospitalization (4 col), ICU (2 col), and Ventilators (2 col)**


```python
covid_df = pd.read_csv('states_covid.csv',
                                 usecols=['date','state','hospitalized', 'hospitalizedCumulative',
                                          'hospitalizedCurrently', 'hospitalizedIncrease', 'inIcuCumulative',
                                          'inIcuCurrently','onVentilatorCumulative', 'onVentilatorCurrently',],
                                 parse_dates=['date'],infer_datetime_format=True)
covid_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>state</th>
      <th>hospitalized</th>
      <th>hospitalizedCumulative</th>
      <th>hospitalizedCurrently</th>
      <th>hospitalizedIncrease</th>
      <th>inIcuCumulative</th>
      <th>inIcuCurrently</th>
      <th>onVentilatorCumulative</th>
      <th>onVentilatorCurrently</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-02-23</td>
      <td>AK</td>
      <td>1260.0</td>
      <td>1260.0</td>
      <td>38.0</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-02-23</td>
      <td>AL</td>
      <td>45250.0</td>
      <td>45250.0</td>
      <td>762.0</td>
      <td>122</td>
      <td>2632.0</td>
      <td>NaN</td>
      <td>1497.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-02-23</td>
      <td>AR</td>
      <td>14617.0</td>
      <td>14617.0</td>
      <td>545.0</td>
      <td>47</td>
      <td>NaN</td>
      <td>204.0</td>
      <td>1505.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-02-23</td>
      <td>AS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-02-23</td>
      <td>AZ</td>
      <td>57072.0</td>
      <td>57072.0</td>
      <td>1515.0</td>
      <td>78</td>
      <td>NaN</td>
      <td>447.0</td>
      <td>NaN</td>
      <td>266.0</td>
    </tr>
  </tbody>
</table>
</div>



**1.2 List, in order, the 5 states with the highest numbers of people *currently* hospitalized, in the ICU, and on ventilation**  
hint: sort_values, uniqie


```python
topH = covid_df.sort_values(by='hospitalizedCurrently',ascending=False).state.unique()[:5]
print('Top 5 Hospital: ',topH)

topICU = covid_df.sort_values(by='inIcuCurrently',ascending=False).state.unique()[:5]
print('Top 5 ICU: ',topICU)

topV = covid_df.sort_values(by='onVentilatorCurrently',ascending=False).state.unique()[:5]
print('Top 5 Ventilation: ',topV)
```

    Top 5 Hospital:  ['CA' 'NY' 'TX' 'FL' 'NJ']
    Top 5 ICU:  ['NY' 'CA' 'TX' 'NJ' 'MI']
    Top 5 Ventilation:  ['NY' 'NJ' 'MI' 'OH' 'IL']


**1.3 Identify the date for each state where the cumulative hosipitalized was greater than or equal to 1000**


```python
covid_1000_df = covid_df[covid_df['hospitalizedCumulative'] >= 1000]
```


```python
covid_1000_df = covid_1000_df[['date','state','hospitalizedCumulative']]
covid_1000_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>state</th>
      <th>hospitalizedCumulative</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-02-23</td>
      <td>AK</td>
      <td>1260.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-02-23</td>
      <td>AL</td>
      <td>45250.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-02-23</td>
      <td>AR</td>
      <td>14617.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-02-23</td>
      <td>AZ</td>
      <td>57072.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2021-02-23</td>
      <td>CO</td>
      <td>23293.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
covid_1000_df.groupby('state').agg('min')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>hospitalizedCumulative</th>
    </tr>
    <tr>
      <th>state</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AK</th>
      <td>2020-12-29</td>
      <td>1004.0</td>
    </tr>
    <tr>
      <th>AL</th>
      <td>2020-05-01</td>
      <td>1008.0</td>
    </tr>
    <tr>
      <th>AR</th>
      <td>2020-06-15</td>
      <td>1003.0</td>
    </tr>
    <tr>
      <th>AZ</th>
      <td>2020-04-11</td>
      <td>1037.0</td>
    </tr>
    <tr>
      <th>CO</th>
      <td>2020-04-07</td>
      <td>1079.0</td>
    </tr>
    <tr>
      <th>CT</th>
      <td>2020-05-01</td>
      <td>7758.0</td>
    </tr>
    <tr>
      <th>FL</th>
      <td>2020-04-02</td>
      <td>1123.0</td>
    </tr>
    <tr>
      <th>GA</th>
      <td>2020-04-02</td>
      <td>1056.0</td>
    </tr>
    <tr>
      <th>HI</th>
      <td>2020-10-18</td>
      <td>1001.0</td>
    </tr>
    <tr>
      <th>ID</th>
      <td>2020-08-11</td>
      <td>1006.0</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>2020-05-08</td>
      <td>4389.0</td>
    </tr>
    <tr>
      <th>KS</th>
      <td>2020-06-17</td>
      <td>1011.0</td>
    </tr>
    <tr>
      <th>KY</th>
      <td>2020-04-18</td>
      <td>1008.0</td>
    </tr>
    <tr>
      <th>MA</th>
      <td>2020-04-04</td>
      <td>1370.0</td>
    </tr>
    <tr>
      <th>MD</th>
      <td>2020-04-06</td>
      <td>1059.0</td>
    </tr>
    <tr>
      <th>ME</th>
      <td>2020-12-23</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>MN</th>
      <td>2020-04-30</td>
      <td>1044.0</td>
    </tr>
    <tr>
      <th>MS</th>
      <td>2020-04-26</td>
      <td>1001.0</td>
    </tr>
    <tr>
      <th>MT</th>
      <td>2020-10-17</td>
      <td>1001.0</td>
    </tr>
    <tr>
      <th>ND</th>
      <td>2020-10-08</td>
      <td>1016.0</td>
    </tr>
    <tr>
      <th>NE</th>
      <td>2020-06-11</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>NH</th>
      <td>2021-01-24</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>NJ</th>
      <td>2020-05-26</td>
      <td>16373.0</td>
    </tr>
    <tr>
      <th>NM</th>
      <td>2020-05-20</td>
      <td>1139.0</td>
    </tr>
    <tr>
      <th>NY</th>
      <td>2020-03-21</td>
      <td>1531.0</td>
    </tr>
    <tr>
      <th>OH</th>
      <td>2020-04-04</td>
      <td>1006.0</td>
    </tr>
    <tr>
      <th>OK</th>
      <td>2020-06-03</td>
      <td>1003.0</td>
    </tr>
    <tr>
      <th>OR</th>
      <td>2020-06-25</td>
      <td>1006.0</td>
    </tr>
    <tr>
      <th>PA</th>
      <td>2020-04-04</td>
      <td>1004.0</td>
    </tr>
    <tr>
      <th>RI</th>
      <td>2020-05-03</td>
      <td>1013.0</td>
    </tr>
    <tr>
      <th>SC</th>
      <td>2020-04-29</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>SD</th>
      <td>2020-08-29</td>
      <td>1006.0</td>
    </tr>
    <tr>
      <th>TN</th>
      <td>2020-04-29</td>
      <td>1013.0</td>
    </tr>
    <tr>
      <th>UT</th>
      <td>2020-06-13</td>
      <td>1012.0</td>
    </tr>
    <tr>
      <th>VA</th>
      <td>2020-04-16</td>
      <td>1048.0</td>
    </tr>
    <tr>
      <th>WA</th>
      <td>2020-05-21</td>
      <td>3125.0</td>
    </tr>
    <tr>
      <th>WI</th>
      <td>2020-04-14</td>
      <td>1049.0</td>
    </tr>
    <tr>
      <th>WY</th>
      <td>2020-12-18</td>
      <td>1001.0</td>
    </tr>
  </tbody>
</table>
</div>



## Task 2 - DataFrame summarizing

Using **Bloom_etal_2018_Reduced_Dataset.csv**, we are going to do more dataframe manipulation and subsetting and summarizing  

**2.1 Read in Bloom_etal_2018_Reduced_Dataset.csv and create two new columns ('genus','species') that consists of the column *taxa* split at the underscore. Print out the head of this new dataframe and the number of unique genera**   

*hint:* pd.str.split(,expand=True)

for example:

| taxa | genus | species 
| :------ | :-- | :--- 
| Alosa_alabamae | Alosa | alabamae


```python
bloom_df = pd.read_csv('Bloom_etal_2018_Reduced_Dataset.csv')
bloom_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>taxa</th>
      <th>logbodysize</th>
      <th>trophic_position</th>
      <th>Reg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alosa_alabamae</td>
      <td>1.707570</td>
      <td>0.431364</td>
      <td>diadromous</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alosa_alosa</td>
      <td>1.778151</td>
      <td>0.556303</td>
      <td>diadromous</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alosa_fallax</td>
      <td>1.778151</td>
      <td>0.556303</td>
      <td>diadromous</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alosa_mediocris</td>
      <td>1.778151</td>
      <td>0.612784</td>
      <td>diadromous</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alosa_pseudoharengus</td>
      <td>1.602060</td>
      <td>0.544068</td>
      <td>diadromous</td>
    </tr>
  </tbody>
</table>
</div>




```python
bloom_df['genus'] = bloom_df['taxa'].str.split('_',expand=True)[0]
bloom_df['species'] = bloom_df['taxa'].str.split('_',expand=True)[1]
len(bloom_df['genus'].unique())
```




    34



**2.2 Create a new dataframe with the mean *logbodysize* and *trophicposition* of each genera. Sort this data frame by the largest body size. Print the head of this dataframe. Which genera is the smallest and largest? What is the trophic position of the smallest and largest?**


```python
bloom_gen_df = bloom_df.groupby('genus',as_index=False).agg('mean')
bloom_gen_df.sort_values(by='logbodysize',ascending=False,inplace=True)
bloom_gen_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>genus</th>
      <th>logbodysize</th>
      <th>trophic_position</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32</th>
      <td>Tenualosa</td>
      <td>1.778151</td>
      <td>0.462398</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Alosa</td>
      <td>1.739062</td>
      <td>0.540815</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Coilia</td>
      <td>1.544068</td>
      <td>0.477121</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Ethmalosa</td>
      <td>1.544068</td>
      <td>0.397940</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Potamalosa</td>
      <td>1.505150</td>
      <td>0.518514</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('Largest:',
      bloom_gen_df['genus'][bloom_gen_df['logbodysize'] == bloom_gen_df['logbodysize'].max()])

print('Smallest:',
     bloom_gen_df['genus'][bloom_gen_df['logbodysize'] == bloom_gen_df['logbodysize'].min()])
```

    Largest: 32    Tenualosa
    Name: genus, dtype: object
    Smallest: 1    Amazonsprattus
    Name: genus, dtype: object



```python
print('Largest:',
      bloom_gen_df['trophic_position'][bloom_gen_df['logbodysize'] == bloom_gen_df['logbodysize'].max()])

print('Smallest:',
     bloom_gen_df['trophic_position'][bloom_gen_df['logbodysize'] == bloom_gen_df['logbodysize'].min()])
```

    Largest: 32    0.462398
    Name: trophic_position, dtype: float64
    Smallest: 1    0.531479
    Name: trophic_position, dtype: float64


## Task 3 - Read in muliple files to a dictionary and make a DataFrame

### This is not an easy excersize. You will have some example code to start but the rest is up to you. You have done all these parts before so should just be linking them together

Using **logfiles**: we are going to do read in each file, get some data, append it to a dictionary to later make into a dataframe. 

First step is to find the necessary files. The number of files in the log files is 36, make sure you have that many as well


```python
!ls -l logfiles/*txt | wc -l 
```

    ls: cannot access logfiles/*txt: No such file or directory
    0



```python
logfiles = !find ./logfiles -name *txt #unix command to find files
logfiles = [os.path.abspath(x) for x in logfiles] #this finds the full path to the file
print(logfiles[0])
```

    /data/gpfs/assoc/parchmanlab/tfaske/DataScience/Data_Science_For_Biology_II/Part.II_PythonProgramming/pandas/logfiles/1901302136_H15_D_14.txt.txt



```python
assert(len(logfiles)==36), 'Do not have correct number of logfiles'
```

### Getting a little tricky here

Read in each of the logfiles, for each file extract:
- minimum temperature
- maximum temperature
- date of minimum temp 
- date of maximum temp 
- mean temp for each file. 

This data should all be appended for a dictionary within a for loop:    
Key should be the file name without the path or .txt extension  
Values should be (minTemp,maxTemp,minDate,maxDate,meanTemp)

I recommend making this work for one file first, then putting the rest in a for loop to do the rest.  

Below is an example of how to read in one file

*hint:* do not read date in as date object


```python
### set up data frame as you read in each file
infile = pd.read_csv(logfiles[0],sep='\t',engine='python')
infile.columns = ['Index','Date','Time','Temp','Type']
infile = infile[['Date','Time','Temp']]
infile.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Time</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9/29/2013</td>
      <td>8:00:00 AM</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9/29/2013</td>
      <td>8:35:00 AM</td>
      <td>34.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9/29/2013</td>
      <td>9:10:00 AM</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9/29/2013</td>
      <td>9:45:00 AM</td>
      <td>35.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9/29/2013</td>
      <td>10:20:00 AM</td>
      <td>37.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
infile.dtypes
```




    Date     object
    Time     object
    Temp    float64
    dtype: object




```python
infile['Date'][infile['Temp'] == infile['Temp'].min()].unique()[0] #use this for minDate,maxDate
```




    '10/28/2013'



Do everything in steps, calculate summaries with this one file:

`minTemp =   
maxTemp =  
minDate = infile['Date'][infile['Temp'] == infile['Temp'].min()].unique()[0] #use this for minDate,maxDate  
maxDate =   
meanTemp =   `

To get you started, I suggest writing some dummy code in plain words to help outline your for loop:


```python
logfiles_dict = {}  
for f in logfiles:  
    #do something   
    #do not read date in as date object  
    #do more something   
    #do other stuff  
    #make print statements EVERYWHERE  
    #append to dict  
    #blahbahblah
```


```python
logfiles_dict = {}
for file in logfiles:
    file_name = file.split('/')[11]
    file_name = file_name.split('.')[0]
    print('parsing...... ',file_name)
    
    infile = pd.read_csv(file,sep='\t',engine='python')
        
    infile.columns = ['Index','Date','Time','Temp','Type']
    infile = infile[['Date','Time','Temp']]
    
    minTemp = infile['Temp'].min()
    maxTemp = infile['Temp'].max()
    minDate = infile['Date'][infile['Temp'] == infile['Temp'].min()].unique()[0]
    maxDate = infile['Date'][infile['Temp'] == infile['Temp'].max()].unique()[0]
    meanTemp = infile['Temp'].mean()

    logfiles_dict[file_name] = [minTemp,maxTemp,minDate,maxDate,meanTemp]
print('\n\nDone parsing',len(logfiles),'files....... ')
```

    parsing......  1901302136_H15_D_14
    parsing......  1901302243_H5_S_14
    parsing......  1901302110_H13_S_14
    parsing......  1901302121_H8_S_14
    parsing......  1901302228_H4_D_14
    parsing......  1901302223_H16_S_14
    parsing......  1901302117_H15_S_14
    parsing......  1901302202_H16_S_14
    parsing......  1901302115_H1_S_14
    parsing......  1901302158_H9_S_14
    parsing......  1901302237_H10_D_14
    parsing......  1901302118_H1_D_14
    parsing......  1901302120_H5_D_14
    parsing......  1901302134_H13_D_14
    parsing......  1901302109_H7_S_14
    parsing......  1901302236_H17_D_14
    parsing......  1901302141_H19_S_14
    parsing......  1901302146_H14_D_14
    parsing......  1901302137_H18_S_14
    parsing......  1901302108_H7_D_14
    parsing......  1901302240_H8_D_14
    parsing......  1901302212_H9_D_14
    parsing......  1901302214_H19_D_14
    parsing......  1901302122_H3_D_14
    parsing......  1901302138_H11_D_14
    parsing......  1901302150_H14_S_14
    parsing......  1901302194_H10_S_14
    parsing......  1901302217_H18_D_14
    parsing......  1901302227_H11_S_14
    parsing......  1901302235_H6_S_14
    parsing......  1901302203_H7_S_14
    parsing......  1901302241_H2_D_14
    parsing......  1901302225_H12_D_14
    parsing......  1901302119_H4_S_14
    parsing......  1901302224_H3_S_14
    parsing......  1901302157_H12_S_14
    
    
    Done parsing 36 files....... 



```python
list(logfiles_dict.items())[:5] #print first 5 items of dict
```




    [('1901302136_H15_D_14',
      [23.0, 91.4, '10/28/2013', '7/27/2014', 35.2911872615204]),
     ('1901302243_H5_S_14',
      [21.5, 68.4, '10/28/2013', '7/13/2014', 35.30480789716639]),
     ('1901302110_H13_S_14',
      [22.8, 60.9, '10/4/2013', '7/13/2014', 32.240032483581665]),
     ('1901302121_H8_S_14',
      [17.9, 73.4, '10/28/2013', '7/13/2014', 34.69886589586862]),
     ('1901302228_H4_D_14',
      [23.6, 64.1, '11/5/2013', '7/13/2014', 34.80269176136363])]




```python
logfiles_df = pd.DataFrame.from_dict(logfiles_dict,orient='index',columns=['minTemp','maxTemp','minDate','maxDate','meanTemp'])

```

**Once you have created a DataFrame with all the logfiles, print the head and save it to an outfile using pd.to_csv() as logfiles_df.csv** 


```python
logfiles_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>minTemp</th>
      <th>maxTemp</th>
      <th>minDate</th>
      <th>maxDate</th>
      <th>meanTemp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1901302136_H15_D_14</th>
      <td>23.0</td>
      <td>91.4</td>
      <td>10/28/2013</td>
      <td>7/27/2014</td>
      <td>35.291187</td>
    </tr>
    <tr>
      <th>1901302243_H5_S_14</th>
      <td>21.5</td>
      <td>68.4</td>
      <td>10/28/2013</td>
      <td>7/13/2014</td>
      <td>35.304808</td>
    </tr>
    <tr>
      <th>1901302110_H13_S_14</th>
      <td>22.8</td>
      <td>60.9</td>
      <td>10/4/2013</td>
      <td>7/13/2014</td>
      <td>32.240032</td>
    </tr>
    <tr>
      <th>1901302121_H8_S_14</th>
      <td>17.9</td>
      <td>73.4</td>
      <td>10/28/2013</td>
      <td>7/13/2014</td>
      <td>34.698866</td>
    </tr>
    <tr>
      <th>1901302228_H4_D_14</th>
      <td>23.6</td>
      <td>64.1</td>
      <td>11/5/2013</td>
      <td>7/13/2014</td>
      <td>34.802692</td>
    </tr>
  </tbody>
</table>
</div>




```python
logfiles_out = hw_dir + 'logfiles_df.csv'
logfiles_df.to_csv(logfiles_out)
```
