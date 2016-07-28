
## Import Libraries


    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns 
    %matplotlib inline
    
    # Set default matplot figure size
    pylab.rcParams['figure.figsize'] = (10.0, 8.0)

## Reading Data Set using Pandas


    titanic_df = pd.read_csv('train.csv')

## Analysis


    # Check the first 5 rows of the data frame
    titanic_df.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




    # Column names
    titanic_df.columns




    Index([u'PassengerId', u'Survived', u'Pclass', u'Name', u'Sex', u'Age',
           u'SibSp', u'Parch', u'Ticket', u'Fare', u'Cabin', u'Embarked'],
          dtype='object')




    # Information about the data set
    titanic_df.info()

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 891 entries, 0 to 890
    Data columns (total 12 columns):
    PassengerId    891 non-null int64
    Survived       891 non-null int64
    Pclass         891 non-null int64
    Name           891 non-null object
    Sex            891 non-null object
    Age            714 non-null float64
    SibSp          891 non-null int64
    Parch          891 non-null int64
    Ticket         891 non-null object
    Fare           891 non-null float64
    Cabin          204 non-null object
    Embarked       889 non-null object
    dtypes: float64(2), int64(5), object(5)
    memory usage: 73.1+ KB



    # Number of passengers in each class
    titanic_df.groupby('Pclass')['Pclass'].count()




    Pclass
    1    216
    2    184
    3    491
    Name: Pclass, dtype: int64




    # Instead of a group by, use seaborn to plot the count of passengers in each class
    fg = sns.factorplot('Pclass', data=titanic_df, kind='count', aspect=1.5)
    fg.set_xlabels('Class')




    <seaborn.axisgrid.FacetGrid at 0xa59e34ec>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_9_1.png)



    titanic_df.groupby('Sex')['Sex'].count()




    Sex
    female    314
    male      577
    Name: Sex, dtype: int64




    # Instead of a group by, use seaborn to plot the number of males and females
    sns.factorplot('Sex', data=titanic_df, kind='count', aspect=1.5)




    <seaborn.axisgrid.FacetGrid at 0xa5b785ec>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_11_1.png)


There are almost two times males as much as there were females. 


    # Number of men and women in each of the passenger class
    titanic_df.groupby(['Sex', 'Pclass'])['Sex'].count()




    Sex     Pclass
    female  1          94
            2          76
            3         144
    male    1         122
            2         108
            3         347
    Name: Sex, dtype: int64




    # Again use saeborn to group by Sex and class
    g = sns.factorplot('Pclass', data=titanic_df, hue='Sex', kind='count', aspect=1.75)
    g.set_xlabels('Class')




    <seaborn.axisgrid.FacetGrid at 0xa560c10c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_14_1.png)


As shown in the figure above, there are more than two times males than females in class 3. However, in classes 1
and 2, the ratio of male to female is almost 1.


    # Number of passengers who survived in each class grouped by sex. Also total was found for each class grouped by sex.
    titanic_df.pivot_table('Survived', 'Sex', 'Pclass', aggfunc=np.sum, margins=True)




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Pclass</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>All</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>91</td>
      <td>70</td>
      <td>72</td>
      <td>233</td>
    </tr>
    <tr>
      <th>male</th>
      <td>45</td>
      <td>17</td>
      <td>47</td>
      <td>109</td>
    </tr>
    <tr>
      <th>All</th>
      <td>136</td>
      <td>87</td>
      <td>119</td>
      <td>342</td>
    </tr>
  </tbody>
</table>
</div>




    not_survived = titanic_df[titanic_df['Survived']==0]


    # Factor plot of those who survived vs. who didn't
    sns.factorplot('Survived', data=titanic_df, kind='count')




    <seaborn.axisgrid.FacetGrid at 0x9e2f9bac>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_18_1.png)



    # Total number of passengers who didn't survive 
    len(not_survived)




    549




    # Number of passengers who did not survive in each class grouped by sex.
    not_survived.pivot_table('Survived', 'Sex', 'Pclass', aggfunc=len, margins=True)




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Pclass</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>All</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>3</td>
      <td>6</td>
      <td>72</td>
      <td>81</td>
    </tr>
    <tr>
      <th>male</th>
      <td>77</td>
      <td>91</td>
      <td>300</td>
      <td>468</td>
    </tr>
    <tr>
      <th>All</th>
      <td>80</td>
      <td>97</td>
      <td>372</td>
      <td>549</td>
    </tr>
  </tbody>
</table>
</div>




    # Passengers who survived and who didn't survive grouped by class and sex
    table = pd.crosstab(index=[titanic_df.Survived,titanic_df.Pclass], columns=[titanic_df.Sex,titanic_df.Embarked])


    table.unstack()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Sex</th>
      <th colspan="9" halign="left">female</th>
      <th colspan="9" halign="left">male</th>
    </tr>
    <tr>
      <th>Embarked</th>
      <th colspan="3" halign="left">C</th>
      <th colspan="3" halign="left">Q</th>
      <th colspan="3" halign="left">S</th>
      <th colspan="3" halign="left">C</th>
      <th colspan="3" halign="left">Q</th>
      <th colspan="3" halign="left">S</th>
    </tr>
    <tr>
      <th>Pclass</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
    <tr>
      <th>Survived</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2</td>
      <td>6</td>
      <td>55</td>
      <td>25</td>
      <td>8</td>
      <td>33</td>
      <td>1</td>
      <td>1</td>
      <td>36</td>
      <td>51</td>
      <td>82</td>
      <td>231</td>
    </tr>
    <tr>
      <th>1</th>
      <td>42</td>
      <td>7</td>
      <td>15</td>
      <td>1</td>
      <td>2</td>
      <td>24</td>
      <td>46</td>
      <td>61</td>
      <td>33</td>
      <td>17</td>
      <td>2</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>28</td>
      <td>15</td>
      <td>34</td>
    </tr>
  </tbody>
</table>
</div>




    table.columns, table.index




    (MultiIndex(levels=[[u'Female', u'Male'], [u'Cherbourg', u'Queenstown', u'Southampton']],
                labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
                names=[u'Sex', u'Embarked']),
     MultiIndex(levels=[[0, 1], [1, 2, 3]],
                labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
                names=[u'Survived', u'Pclass']))




    # Change name of columns
    table.columns.set_levels(['Female', 'Male'], level=0, inplace=True)
    table.columns.set_levels(['Cherbourg','Queenstown','Southampton'], level=1, inplace=True)
    table




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>Sex</th>
      <th colspan="3" halign="left">Female</th>
      <th colspan="3" halign="left">Male</th>
    </tr>
    <tr>
      <th></th>
      <th>Embarked</th>
      <th>Cherbourg</th>
      <th>Queenstown</th>
      <th>Southampton</th>
      <th>Cherbourg</th>
      <th>Queenstown</th>
      <th>Southampton</th>
    </tr>
    <tr>
      <th>Survived</th>
      <th>Pclass</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">0</th>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>25</td>
      <td>1</td>
      <td>51</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>8</td>
      <td>1</td>
      <td>82</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>9</td>
      <td>55</td>
      <td>33</td>
      <td>36</td>
      <td>231</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">1</th>
      <th>1</th>
      <td>42</td>
      <td>1</td>
      <td>46</td>
      <td>17</td>
      <td>0</td>
      <td>28</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>2</td>
      <td>61</td>
      <td>2</td>
      <td>0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>24</td>
      <td>33</td>
      <td>10</td>
      <td>3</td>
      <td>34</td>
    </tr>
  </tbody>
</table>
</div>




    print('Average and median age of passengers are %0.f and %0.f years old, respectively'%(titanic_df.Age.mean(), 
                                                                              titanic_df.Age.median()))

    Average and median age of passengers are 30 and 28 years old, respectively



    titanic_df.Age.describe()




    count    714.000000
    mean      29.699118
    std       14.526497
    min        0.420000
    25%       20.125000
    50%       28.000000
    75%       38.000000
    max       80.000000
    Name: Age, dtype: float64




    # Drop missing values for the records in which age passenger is missing
    age = titanic_df['Age'].dropna()


    # Distribution of age, with an overlay of a density plot
    age_dist = sns.distplot(age)
    age_dist.set_title("Distribution of Passengers' Ages")




    <matplotlib.text.Text at 0x9ff81f2c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_28_1.png)



    # Another way to plot a histogram of ages is shown below
    titanic_df['Age'].hist(bins=50)




    <matplotlib.axes._subplots.AxesSubplot at 0x9fe3140c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_29_1.png)



    titanic_df['Parch'].dtype, titanic_df['SibSp'].dtype, len(titanic_df.Cabin.dropna())




    (dtype('int64'), dtype('int64'), 204)




    # Create a function to define those who are children (less than 16)
    def male_female_child(passenger):
        age, sex = passenger
        
        if age < 16:
            return 'child'
        else:
            return sex


    titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child, axis=1)


    # Lets have a look at the first 10 rows of the data frame
    titanic_df[:10]




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>person</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>female</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>female</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>male</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>Moran, Mr. James</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>330877</td>
      <td>8.4583</td>
      <td>NaN</td>
      <td>Q</td>
      <td>male</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>McCarthy, Mr. Timothy J</td>
      <td>male</td>
      <td>54</td>
      <td>0</td>
      <td>0</td>
      <td>17463</td>
      <td>51.8625</td>
      <td>E46</td>
      <td>S</td>
      <td>male</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>male</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>349909</td>
      <td>21.0750</td>
      <td>NaN</td>
      <td>S</td>
      <td>child</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)</td>
      <td>female</td>
      <td>27</td>
      <td>0</td>
      <td>2</td>
      <td>347742</td>
      <td>11.1333</td>
      <td>NaN</td>
      <td>S</td>
      <td>female</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2</td>
      <td>Nasser, Mrs. Nicholas (Adele Achem)</td>
      <td>female</td>
      <td>14</td>
      <td>1</td>
      <td>0</td>
      <td>237736</td>
      <td>30.0708</td>
      <td>NaN</td>
      <td>C</td>
      <td>child</td>
    </tr>
  </tbody>
</table>
</div>




    # Lets do a factorplot of passengers splitted into sex, children and class
    sns.factorplot('Pclass', data=titanic_df, kind='count', hue='person', order=[1,2,3], 
                   hue_order=['child','female','male'], aspect=2)




    <seaborn.axisgrid.FacetGrid at 0x9a2dbd8c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_34_1.png)



    # Count number of men, women and children
    titanic_df['person'].value_counts()




    male      537
    female    271
    child      83
    dtype: int64




    # Do the same as above, but split the passengers into either survived or not
    sns.factorplot('Pclass', data=titanic_df, kind='count', hue='person', col='Survived', order=[1,2,3], 
                   hue_order=['child','female','male'], aspect=1.25, size=5)




    <seaborn.axisgrid.FacetGrid at 0x9eb75ecc>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_36_1.png)


There are much more children in third class than there are in first and second class. However, one may expect that
there woould be more children in 1st and 2nd class than there are in 3rd class.

### kde plot, Distribution of Passengers' Ages

#### Grouped by Gender


    fig = sns.FacetGrid(titanic_df, hue='Sex', aspect=4)
    fig.map(sns.kdeplot, 'Age', shade=True)
    oldest = titanic_df['Age'].max()
    fig.set(xlim=(0,oldest))
    fig.set(title='Distribution of Age Grouped by Gender')
    fig.add_legend()




    <seaborn.axisgrid.FacetGrid at 0x9abecacc>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_40_1.png)



    fig = sns.FacetGrid(titanic_df, hue='person', aspect=4)
    fig.map(sns.kdeplot, 'Age', shade=True)
    oldest = titanic_df['Age'].max()
    fig.set(xlim=(0,oldest))
    fig.add_legend()




    <seaborn.axisgrid.FacetGrid at 0x9abd4bac>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_41_1.png)


#### Grouped by Class


    fig = sns.FacetGrid(titanic_df, hue='Pclass', aspect=4)
    fig.map(sns.kdeplot, 'Age', shade=True)
    oldest = titanic_df['Age'].max()
    fig.set(xlim=(0,oldest))
    fig.set(title='Distribution of Age Grouped by Class')
    fig.add_legend()




    <seaborn.axisgrid.FacetGrid at 0x9a76c18c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_43_1.png)


From the plot above, class 1 has a normal distribution. However, classes 2 and 3 have a skewed distribution towards
20 and 30-year old passengers.

#### What cabins did the Passengers stay in?


    deck = titanic_df['Cabin'].dropna()
    deck.head()




    1      C85
    3     C123
    6      E46
    10      G6
    11    C103
    Name: Cabin, dtype: object




    # Grab the first letter of the cabin letter
    d = []
    for c in deck:
        d.append(c[0])


    d[0:10]




    ['C', 'C', 'E', 'G', 'C', 'D', 'A', 'C', 'B', 'D']




    from collections import Counter
    Counter(d)




    Counter({'C': 59, 'B': 47, 'D': 33, 'E': 32, 'A': 15, 'F': 13, 'G': 4, 'T': 1})




    # Now lets factorplot the cabins. First transfer the d list into a data frame. Then rename the column Cabin 
    cabin_df = DataFrame(d)
    cabin_df.columns=['Cabin']
    sns.factorplot('Cabin', data=cabin_df, kind='count', order=['A','B','C','D','E','F','G','T'], aspect=2, 
                  palette='winter_d')




    <seaborn.axisgrid.FacetGrid at 0x99e810cc>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_50_1.png)



    # Drop the 'T' cabin
    cabin_df = cabin_df[cabin_df['Cabin'] != 'T']


    # Then replot the Cabins factorplot as above
    sns.factorplot('Cabin', data=cabin_df, kind='count', order=['A','B','C','D','E','F','G'], aspect=2, 
                  palette='Greens_d')




    <seaborn.axisgrid.FacetGrid at 0x98c849ac>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_52_1.png)



    # Below is a link to the list of matplotlib colormaps
    url = 'http://matplotlib.org/api/pyplot_summary.html?highlight=colormaps#matplotlib.pyplot.colormaps'
    import webbrowser
    webbrowser.open(url)




    True



#### Where did the passengers come from i.e. Where did the passengers land into the ship from?


    sns.factorplot('Embarked', data=titanic_df, kind='count', hue='Pclass', hue_order=range(1,4), aspect=2,
                  order = ['C','Q','S'])




    <seaborn.axisgrid.FacetGrid at 0x9866c76c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_55_1.png)


From the figure above, one may conclude that almost all of the passengers who boarded from Queenstown were in third 
class. On the other hand, many who boarded from Cherbourg were in first class. The biggest portion of passengers 
who boarded the ship came from Southampton, in which 353 passengers were in third class, 164 in second class and 
127 passengers were in first class. In such cases, one may need to look at the economic situation at these different towns at that period of time to understand why most passengers who boarded from Queenstown were in third class for example.


    titanic_df.Embarked.value_counts()




    S    644
    C    168
    Q     77
    dtype: int64




    # For tabulated values, use crosstab pandas method instead of the factorplot in seaborn
    port = pd.crosstab(index=[titanic_df.Pclass], columns=[titanic_df.Embarked])
    port.columns = [['Cherbourg','Queenstown','Southampton']]


    port




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cherbourg</th>
      <th>Queenstown</th>
      <th>Southampton</th>
    </tr>
    <tr>
      <th>Pclass</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>85</td>
      <td>2</td>
      <td>127</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>3</td>
      <td>164</td>
    </tr>
    <tr>
      <th>3</th>
      <td>66</td>
      <td>72</td>
      <td>353</td>
    </tr>
  </tbody>
</table>
</div>




    port.index




    Int64Index([1, 2, 3], dtype='int64', name=u'Pclass')




    port.columns




    Index([u'Cherbourg', u'Queenstown', u'Southampton'], dtype='object')




    port.index=[['First','Second','Third']]


    port




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cherbourg</th>
      <th>Queenstown</th>
      <th>Southampton</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>85</td>
      <td>2</td>
      <td>127</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>17</td>
      <td>3</td>
      <td>164</td>
    </tr>
    <tr>
      <th>Third</th>
      <td>66</td>
      <td>72</td>
      <td>353</td>
    </tr>
  </tbody>
</table>
</div>



#### Who was alone and who was with parents or siblings?


    titanic_df[['SibSp','Parch']].head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SibSp</th>
      <th>Parch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




    # Alone dataframe i.e. the passenger has no siblings or parents
    alone_df = titanic_df[(titanic_df['SibSp'] == 0) & (titanic_df['Parch']==0)]
    # Add Alone column
    alone_df['Alone'] = 'Alone'
    # Not alone data frame i.e. the passenger has either a sibling or a parent.
    not_alone_df = titanic_df[(titanic_df['SibSp'] != 0) | (titanic_df['Parch']!=0)]
    not_alone_df['Alone'] = 'With family'
    
    # Merge the above dataframes
    comb = [alone_df, not_alone_df]
    # Merge and sort by index
    titanic_df = pd.concat(comb).sort_index()

    /home/tarek/anaconda/lib/python2.7/site-packages/IPython/kernel/__main__.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    /home/tarek/anaconda/lib/python2.7/site-packages/IPython/kernel/__main__.py:7: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy



    [len(alone_df), len(not_alone_df)]




    [537, 354]




    # Show the first five records of the alone data frame
    alone_df.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>person</th>
      <th>Alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>female</td>
      <td>Alone</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>male</td>
      <td>Alone</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>Moran, Mr. James</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>330877</td>
      <td>8.4583</td>
      <td>NaN</td>
      <td>Q</td>
      <td>male</td>
      <td>Alone</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>McCarthy, Mr. Timothy J</td>
      <td>male</td>
      <td>54</td>
      <td>0</td>
      <td>0</td>
      <td>17463</td>
      <td>51.8625</td>
      <td>E46</td>
      <td>S</td>
      <td>male</td>
      <td>Alone</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>1</td>
      <td>1</td>
      <td>Bonnell, Miss. Elizabeth</td>
      <td>female</td>
      <td>58</td>
      <td>0</td>
      <td>0</td>
      <td>113783</td>
      <td>26.5500</td>
      <td>C103</td>
      <td>S</td>
      <td>female</td>
      <td>Alone</td>
    </tr>
  </tbody>
</table>
</div>




    # Show the first five rows of the not alone data frame
    not_alone_df.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>person</th>
      <th>Alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>male</td>
      <td>With family</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>female</td>
      <td>With family</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>female</td>
      <td>With family</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>male</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>349909</td>
      <td>21.0750</td>
      <td>NaN</td>
      <td>S</td>
      <td>child</td>
      <td>With family</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)</td>
      <td>female</td>
      <td>27</td>
      <td>0</td>
      <td>2</td>
      <td>347742</td>
      <td>11.1333</td>
      <td>NaN</td>
      <td>S</td>
      <td>female</td>
      <td>With family</td>
    </tr>
  </tbody>
</table>
</div>




    titanic_df.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>person</th>
      <th>Alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>male</td>
      <td>With family</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>female</td>
      <td>With family</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>female</td>
      <td>Alone</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>female</td>
      <td>With family</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>male</td>
      <td>Alone</td>
    </tr>
  </tbody>
</table>
</div>




    """ Another way to perform the above
    titanic_df['Alone'] = titanic_df.SibSp + titanic_df.Parch
    
    titanic_df['Alone'].loc[titanic_df['Alone']>0] = 'With family'
    titanic_df['Alone'].loc[titanic_df['Alone']==0] = 'Alone'"""




    " Another way to perform the above\ntitanic_df['Alone'] = titanic_df.SibSp + titanic_df.Parch\n\ntitanic_df['Alone'].loc[titanic_df['Alone']>0] = 'With family'\ntitanic_df['Alone'].loc[titanic_df['Alone']==0] = 'Alone'"




    fg=sns.factorplot('Alone', data=titanic_df, kind='count', hue='Pclass', col='person', hue_order=range(1,4),
                     palette='Blues')
    fg.set_xlabels('Status')




    <seaborn.axisgrid.FacetGrid at 0x9548b6cc>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_72_1.png)


From the figure above, it is clear that most children traveled with family in third class. For men, most traveled alone in third class. On the other hand, the number of female passengers who traveled either with family or alone among the second and third class is comparable. However, more women traveled with family than alone in first class. 

### Factors Affecting the Surviving


    '''Now lets look at the factors that help someone survived the sinking. We start this analysis by adding a new
    cloumn to the titanic data frame. Use the Survived column to map to the new column with factors 0:no and 1:yes
    using the map method'''
    titanic_df['Survivor'] = titanic_df.Survived.map({0:'no', 1:'yes'})


    titanic_df.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>person</th>
      <th>Alone</th>
      <th>Survivor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>male</td>
      <td>With family</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>female</td>
      <td>With family</td>
      <td>yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>female</td>
      <td>Alone</td>
      <td>yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>female</td>
      <td>With family</td>
      <td>yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>male</td>
      <td>Alone</td>
      <td>no</td>
    </tr>
  </tbody>
</table>
</div>



#### Class Factor


    # Survived vs. class Grouped by gender
    sns.factorplot('Pclass','Survived', hue='person', data=titanic_df, order=range(1,4), 
                   hue_order = ['child','female','male'])




    <seaborn.axisgrid.FacetGrid at 0x92e0334c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_78_1.png)


From the figure above, being a male or a third class reduce the chance for one to survive. 


    sns.factorplot('Survivor', data=titanic_df, hue='Pclass', kind='count', palette='Pastel2', hue_order=range(1,4),
                  col='person')




    <seaborn.axisgrid.FacetGrid at 0x932f65cc>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_80_1.png)


### Age Factor


    # Linear plot of age vs. survived
    sns.lmplot('Age', 'Survived', data=titanic_df)




    <seaborn.axisgrid.FacetGrid at 0x92e2904c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_82_1.png)


There seems to be a general linear trend between age and the survived field. The plot shows that the older the passenger is, the less chance he/she would survive.


    # Survived vs. Age grouped by Sex
    sns.lmplot('Age', 'Survived', data=titanic_df, hue='Sex')




    <seaborn.axisgrid.FacetGrid at 0x92d152cc>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_84_1.png)


Older women have higher rate of survival than older men as shown in the figure above. Also, older women has higher
rate of srvival than younger women; an opposite trend to the one for the male passengers.


    # Survived vs. Age gruped by class
    sns.lmplot('Age', 'Survived', hue='Pclass', data=titanic_df, palette='winter', hue_order=range(1,4))




    <seaborn.axisgrid.FacetGrid at 0x9265a06c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_86_1.png)


In all three classes, the chance to survive reduced as the passengers got older.


    # Create a generation bin
    generations = [10,20,40,60,80]
    sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,x_bins=generations, hue_order=[1,2,3])




    <seaborn.axisgrid.FacetGrid at 0x9231fcac>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_88_1.png)


#### Deck Factor


    titanic_df.columns




    Index([u'PassengerId', u'Survived', u'Pclass', u'Name', u'Sex', u'Age',
           u'SibSp', u'Parch', u'Ticket', u'Fare', u'Cabin', u'Embarked',
           u'person', u'Alone', u'Survivor'],
          dtype='object')




    titanic_DF = titanic_df.dropna(subset=['Cabin'])


    d[0:10]




    ['C', 'C', 'E', 'G', 'C', 'D', 'A', 'C', 'B', 'D']




    len(titanic_DF), len(d)




    (204, 204)




    titanic_DF['Deck'] = d

    /home/tarek/anaconda/lib/python2.7/site-packages/IPython/kernel/__main__.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      if __name__ == '__main__':



    titanic_DF = titanic_DF[titanic_DF.Deck != 'T']


    titanic_DF.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>person</th>
      <th>Alone</th>
      <th>Survivor</th>
      <th>Deck</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>female</td>
      <td>With family</td>
      <td>yes</td>
      <td>C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>female</td>
      <td>With family</td>
      <td>yes</td>
      <td>C</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>McCarthy, Mr. Timothy J</td>
      <td>male</td>
      <td>54</td>
      <td>0</td>
      <td>0</td>
      <td>17463</td>
      <td>51.8625</td>
      <td>E46</td>
      <td>S</td>
      <td>male</td>
      <td>Alone</td>
      <td>no</td>
      <td>E</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>1</td>
      <td>3</td>
      <td>Sandstrom, Miss. Marguerite Rut</td>
      <td>female</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>PP 9549</td>
      <td>16.7000</td>
      <td>G6</td>
      <td>S</td>
      <td>child</td>
      <td>With family</td>
      <td>yes</td>
      <td>G</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>1</td>
      <td>1</td>
      <td>Bonnell, Miss. Elizabeth</td>
      <td>female</td>
      <td>58</td>
      <td>0</td>
      <td>0</td>
      <td>113783</td>
      <td>26.5500</td>
      <td>C103</td>
      <td>S</td>
      <td>female</td>
      <td>Alone</td>
      <td>yes</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>




    sns.factorplot('Deck', 'Survived', data=titanic_DF, order=['A','B','C','D','E','F','G'])




    <seaborn.axisgrid.FacetGrid at 0x9270680c>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_97_1.png)


There does not seem to be any relation between deck and the survival rate as shown in the above figure!

#### Family Status Factor


    sns.factorplot('Alone', 'Survived', data=titanic_df, palette='winter') #hue='person', 
                   #hue_order=['child', 'female', 'male'])




    <seaborn.axisgrid.FacetGrid at 0x91c1cbac>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_100_1.png)


There seems that the survival rate diminishes significantly for those who were alone. However, lets check if a
gender or age play a factor. From the figure below, one may conclude that the survival rate for women and children
are much higher than that of men, as was concluded previously and as anticipated. However, the survival rate is not
significant for either gender or for children who were with family versus who were alone. Moreover, the survival 
rate for women and children increases for those who were alone. For men, the survival rate diminishes slightly 
for those who were alone versus for those who were with family.


    sns.factorplot('Alone', 'Survived', data=titanic_df, palette='winter', hue='person', 
                   hue_order=['child', 'female', 'male'])




    <seaborn.axisgrid.FacetGrid at 0x91bf57cc>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_102_1.png)



    # Lets split it by class now!
    sns.factorplot('Alone', 'Survived', data=titanic_df, palette='summer', hue='person', 
                   hue_order=['child', 'female', 'male'], col='Pclass', col_order=[1,2,3])




    <seaborn.axisgrid.FacetGrid at 0x915553ac>




![png](Titanic%20-%20Project_files/Titanic%20-%20Project_103_1.png)


### Predictive Modeling


    import sklearn


    
