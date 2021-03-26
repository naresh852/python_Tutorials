''''pandas is a data analysis library that allows us to read and work with different types of data we can use
this to analyze csv files,excel files and other similar formats'''

# StackOverflow Survey Download Page - http://bit.ly/SO-Survey-Download​
# Datetime Formatting Codes - http://bit.ly/python-dt-fmt​
# Pandas Date Offset Codes - http://bit.ly/pandas-dt-fmt
'''data frames are pretty much backbone of the pandas
a dataframe is set of rows and columns of data'''
'''
import pandas as pd
df=pd.read_csv('file name or path')
df
df.shape # is an attribute not a method to get rows and cols
df.info() #to see rows cols and DATATYPES ALSO
pd.set_option('display.max_columns',85) #to see limited rows upto 85 only
pd.set_option('display.max_rows',25) #to see limited rows upto 25
pd.set_option('display.max_columns',None) #to see all columns
df.head() #to see only 5 rows data  only
df.head(10)# to see only 10 rows data

df.tail() # to see last 5 rows data
df.tail(10) #to see only 10 last elements
'''
'''
df.columns #to see all columns
df['keyofcolumn'] #to get key values
df['keyor coll'].value_counts() #its like a counter from collections
df.loc[0:2,'Hobbyist':'ConvertedComp'] #to see upto 0,1,2 values from hoobby to conver
'''
'''
people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df=DataFrame(people)  #to convert to (keys)sets and rows(cols)
dataframe is much much more than a dict of lists
series is just basically a list of data  #defi: its a one dimensional array
in lamens terms its rws of Data

df['email'] or df.email we get same o/p
we get series as o/p seris a single col with many values
df.['email'] is better than df.email cause if we have col name count and key also count

df[['last','email']] to access those cols not as df['last','email'] cause pandas would consider it as a string
we get wrong o/p of col count
we get a DF as  o/p

df.columns to see all columns 
to get rows we use loc or iloc 

i loc allows to access to rows  elements by integer values
df.iloc[0]
'''

#set resset and use indexes
'''df.set_index('email') #to setemail as index for temporary
df.set_index('email',inplace=True) #to set email as index permanently
df.index #to get all index values
df.reset_index(inplace=True) #to reset index to original permanently
iloc is better be used for integers and loc fot strings

TO SETA PARTICULAR COL AS INDEX IN BEGINNING OF CSV CREATION
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv',index_col='Column')

df.loc['colname'] # to see that col details
df.loc['colname','question text'] # to see full untruncated value
#to sort index alphabetically temporarily
schema_df.sort_index()
schema_df.sort_index(ascending =False) #to get reverse order
# to sort index alphabetically permannetly
schema_df.sort_index(inplace=True)
'''
#filterRING ROWS AND COLUMNS
'''
df['last']=='Doe'  #to get all booleans of doe matches in DF returns a series
df[df['last']=='Doe'] # to get a DF of all values matches
filt=df['last']=='Doe'

df['filt']
df.loc['filt']   both give same o/p but have more benefits in loc
df.loc['filt','email']  #filt is ,like a rowand email is like a column we want 

filt=(df['first']=='fot') & (df['last']=='zdoe') is better than filt=df.loc[(df['first']=='fot') & (df['last']=='zdoe')]

df.loc[~filt,'email'] #to get negate values of filt 

high_salary=df['CompTotal']>25000 #for salary greater than 25000
df.loc[high_salary,['CompTotal','Country','LanguageWorkedWith','Age']] #for high salary and all other stuff in []

countries=['india','japan','USA','Australia']
filt=df['country'].isin(countries)
df.loc[filt,'Country']

#working with strings,must keep a default if not therre or throws a error
filt=df['LanguageWorkedWith'].str.contains('Python',na=False)

'''
#UPDATE ROWS AND COLUMNS AND MODIFY  DAAT IN DATAFRAME
'''
df.columns=['first_name', 'last_name','email'] #to replace col names with yiur fav names

df.columns=[x.upper() for x in df.columns] #to make all col upper
df.columns=df.columns.str.replace('_',' ')  #to replace _ with ' '

df.rename(columns={'first_name':'first','last_name':'last'}) #to rename temporarily columns
df.rename(columns={'first_name':'first','last_name':'last'},inplace=True) #to rename permanently columns
#to REPLACE ROWS 
CHOOSE INDEX OF ROW THEN ENTER IT IN THAT
df.loc[2]=['nare','reddy','nareshreddy@gmail.com']

TO CHANGE ONLY ONE OR TWO THINGS IN A ROW DO THIS
MENTION COLNAMES IN FIRST AND THEN THEIR NAMES U WANT TO 51-ADD REMOVE ROWS COLS IN DF
df.loc[2,['first','last']]=['John','Doe']

TO CHANGE FIRST NAME ONLY NO NEED BRACKETS  A LOT
df.loc[2,'last']='smith'
AT ALSO DOES SAME SIMIAR TO LOC
df.at[2,'last']='smith'

NEVER TRY TO ASSIGN VALUES WITHOUT LOC OR ILOC OR AT
df.loc[2,'last']='smith'  #ERROR THROWS

TO MAKE ALL EMAILS LOWER
df['email'].str.lower() #RETURNS A SERIES 
TO GET A DF
df['email']=df['email'].str.lower()
#####TO DELETE A COLUMN -  del df['columnname']
apply    df['email'].apply(len)  
#########APPLY#############
def update_email(email):
    return email.upper()
df['email'].apply(update_email)   ######returns a series
df['email']=df['email'].apply(update_email) #####returns a df dataframe
df['email']=df['email'].apply(lambda x:x.lower())  #####we can use lambda also 

df.apply(len) ##to get only no o ele in columns
df.apply(len,axis='columns') ###to get only rows elements 
len(df['email'])
df.apply(pd.Series.min) #######to get min elem in each column
df.apply(lambda x:x.min()) ##### x is series

##########APPLYMAP##############
df.applymap(len)  ######to get  lengths all elem in DF FORMAT
df.applymap(str.lower) ###to make all ele lower

############ MAP #######
MAP ONLY WORKS ON A SERIES 
df['first'].map({'Corey':'nare','Jane':'reddy'})  ####to replace a name or names in a series
 not replaced ele becomes Nan
to avoid that we use replace
############### replace ###########
df['first'].replace({'Corey':'nare','Jane':'reddy'}) #returns series
df['first']=df['first'].replace({'nare':'Corey','reddy':'Jane'}) #returns df

df['Hobbyist'].map({'Yes':True,'No':False})  #changes made to series
anything oter than gets converted to Nan
df['Hobbyist']=df['Hobbyist'].map({'Yes':True,'No':False}) #changes made to df
'''
####ADDING REMOVING COLS ROWS IN DF
'''
ASSIGNING IS ALWAYS DO THORUGH DF['COLNAME'] NOT THROUGH . NOTATION
TO ADD A NEW COL
df['full_name']=df['first']+' '+df['last']

TO REMOVE A COL TEMPORARILY
df.drop(columns=['first','last'])
df.drop(columns=['first','last'],inplace=True)

TO split a series of a single col
df['full_name'].str.split(' ') #### to return series
df['full_name'].str.split(' ',expand=True) ####### to return DF

TO ADD COLS TO PREVIOUS DATA FRAME AND ASSIGN COL NAMES ALSO
df[['first','last']]=df['full_name'].str.split(' ',expand=True)

TO ADD A ROW
df.append({'first':'Tony'},ignore_index=True)

TO ADD A NEW DF TO A OLD DF
df.append(df2,ignore_index=True)   ##TEMPORARILY
df=df.append(df2,ignore_index=True)  ###PERMANENT
TO REMOVE A ROW IN A DF
df.drop(index=4,inplace=True) ##PERMANENTLY
TO REMOEV A ROW WITH APARTI CONDITION
filt=df['first']=='John'
df.drop(index=df[filt].index)  ##TEMPORARY

'''
###SORTING IN DF
'''
df.sort_values(by='first')  ###SORTING IN ASCENDING
df.sort_values(by='first',ascending=False)  ###SORTING IN DESCENDING
df.sort_values(by=['first','last'],ascending=False) ###SORTING MULTIVALUES ATONCE IN DESC ORDER

TO MAKE CHANGES PERMANENT
df.sort_values(by=['first','last'],ascending=[False,True],inplace=True)
TO SORT ACCORDING TO INDEX VALUES
df.sort_index()
TO SOR VALUES IN A SERIES
df['first'].sort_values()  ##temporary
TO ACCESS MOULTI COLUMNS
df[['Country','ConvertedComp']]
TO ACCESS MULTI COLS HEAD 50
df[['Country','ConvertedComp']].head(50)
TO SEE TOP 10 SALARIS
df['ConvertedComp'].nlargest(10)

TO SEE 10 LARGEST SALARIES TOTAL DF FORMAT ALL COLS INCLUDED
df.nlargest(10,'ConvertedComp')

TO SEE 10 SMALLEST SLARIS IN TOTAL DF FORMAT ALL COLS INCLUDED
df.nsmallest(10,'ConvertedComp')
'''
##GROUPING AND AGGREGATING
# AGGREGATING-COMBINING MULTILPLE PIECES OF DATA INTO SINGLE RESULT
'''
TO GET A MEDIAN OF A COL
df['ConvertedComp'].median()
TO GET ALL MEADIANS OF ALL INT COLS
df.median()
TO GET DETAILED VIEW OF ALL THNGS MEAN,MEDIAN,MIN,MAX
df.describe()
COUNT-- is no of non NAN (NOT ANSWERED) rows{basically people who answered the survey or has valid input}
df['ConvertedComp'].count()
TO SEE HOW MANY PEOPLE SAID YES AND NO,OR HOW MANY PPL GET A PART SALARY    
df['ConvertedComp'].value_counts()
df['Hobbyist'].value_counts()
TO SEE PERCENTAGE VALUES
df['LanguageWorkedWith'].value_counts(normalize=True)

IF WE WANT TO SEE RESULTS BASED ON A SPECIFIC COL OR COUNTRY WE USE GROUPING CONCEPT
group by operation of some combination of splitting a object apply function and combineing results
#returns a dfgroupby object  
df.groupby(['Country'])
country_grp=df.groupby(['Country'])   ####returns a DF
country_grp.get_group('United States')  ##to acess a part country in country grp

TO SEE COMPTOTAL VALUECOUNTS OF INDIA
filt=df['Country']=='India'
df.loc[filt]['CompTotal']   #####RETURNS A DF
df.loc[filt]['CompTotal'].value_counts()

USING GROUPING
country_grp['LanguageWorkedWith'].value_counts()  ###to get all country using languages workwith count

TO GET A PARTICULAR COUNTRY VALUE
country_grp['LanguageWorkedWith'].value_counts().loc['India']  ##IT IS SAME AS USING A FILTER BUT WE NO NEED TO CREATE A FILTER FOR EACH COUNTRY

USING AGG TO AGGRAGATE A PARTICULAR VALUES LIKE MEAN MEDIAN
country_grp['ConvertedComp'].agg(['mean','median'])
country_grp['ConvertedComp'].agg(['mean','median']).loc['India']
THIS WONT WORK FOR GROUPBY OBJECTS ONLY WORKS FOR SERIES
country_grp['LanguageWorkedWith'].str.contains('Python').sum()  ##ERROR
CORRECT WAY TO DEAL WITH GROUPBY OBJ# country_grp['LanguageWorkedWith'].apply(lambda x:x.str.contains('Python').sum())
filt=df['Country']=='India'
df.loc[filt,'LanguageWorkedWith'].str.contains('Python').sum()  ##NO ERROR CAUSE ITS A SERIES

####PEOPLE WHO RESPONDED IN A COUNTRY RETUNRS A SERIES
country_respondents=df['Country'].value_counts()
country_respondents
####PEOPLE WHO USE ONLY IN A PART COUNTRY RETURNS SERIES
people_use_python=country_grp['LanguageWorkedWith'].apply(lambda x:x.str.contains('Python').sum())
people_use_python
#####MADE A NEW DF OF PYTHON USING SERIS OF BOTH REPONSES
python_df=pd.concat([country_respondents,people_use_python],axis='columns')
python_df
#######TO RENAME COLS IN DF
python_df.rename(columns={'Country':'noofrespondents','LanguageWorkedWith':'knowspython'},inplace=True)
'''
####CLEANING DATA CASTING DATATYPES AND HANDLING MISSING VALUES
'''
####TO REMOVE NOT ANSWER ROWS ANY ROW WITH A MISSING VALUE
df.dropna() ##IS EQUAL TO df.dropna(axis='index',how='any')
df.dropna(axis='index',how='all')    ###to remove  rows if all are NAN
##########TO REMOE COLS
df.dropna(axis='columns',how='all')   ##remove if all vlaues are missing
df.dropna(axis='columns',how='any')  ##remove if a single value is Nan
#####to remove a rows regarding a particular col
TO MAKE CHANGES PERMANNET ADD inplace=True at end in side bracekts
df.dropna(axis='index',how='any',subset=['last','email'])   ##any removes row if on evalues misses
#all removes a row if all values are mssing
######tocheck how many nan are there ########
df.isna()
###33TO RELPACE NAN WITH A PARTICULAR VALUE
df.fillna('missing')
df.fillna(0)
#########TO CHEECK DATAYPES OF VALUES
df.dtypes
if object it means its a string or mix of these
Nan value is actually a float unedr the hood 
type(np.nan)
df['age'].mean()  ##int values are strings that s y it throws  a error
df['age']=df['age'].astype(int) ###cannot convert Nan vlaues to int
df['age']=df['age'].astype(float) ###can convert some Nan to float as Nan is a float
####TO CONVERT ALL VALUES IN DF TO A PART TYPES
df.astype(int)
##########TO SET CSV FILE NA OR MISSING VALUES TO Nan
na_vals=['ALL','NA','Missing']
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent',na_values=na_vals)
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')
#####TO SEE ALL UNIQUE VALUES OF A PARTICULAR COL
df['YearsCode'].unique()
#######TO REPLACE VALUES IN DF
df.replace('NA',np.nan,inplace=True)
df.replace('Missing',np.nan,inplace=True)
'''
#######WORKING WITH DATE TIME SERIES
'''
df.loc[0,'Date'].day_name()  ###TO FIND weekday BUT Date SHOULD BE IN INT FORMAT
df['Date']=pd.to_datetime(df['Date'])  ##TO CONVERT TO DATETIME FORMAT
if aobvr throws error
df['Date']=pd.to_datetime(df['Date'],format='%Y-%m-%d %I-%p')  ###to format to a datetime as in DF table format
TO GET DAY NAME
df.loc[0,'Date'].day_name()
 ###TO FORMAT DATETIME OF ONLY DATES IN BEGINNING ONLY less code
d_parser=lambda x: pd.datetime.strptime(x,'%Y-%m-%d %I-%p')
df=pd.read_csv('ETH_1h.csv',parse_dates=['Date'],date_parser=d_parser)

df['Date'].dt.day_name() #######to get dayname of a date in series
df['Date'].min()  ###mini day in Date series

df['Date'].max()   ###to see recent day in series
filt=df['Date']>='2020'
df.loc[filt]            ######to GET DATA ABOVE A TIME
#######  to get date froma particular time ################
filt=(df['Date']>=pd.to_datetime('2019-01-01')) & (df['Date']<pd.to_datetime('2020-01-01'))
df.loc[filt]
#####to do sclicing #########
df['2020-01':'2020-02']['Close'].mean()
@########## to get max value of  day #########
# df['2020-01-01']['High'].max()
df.loc['2020-01-01','High'].max()

df['High'].resample('D').max() ####max value of every day 
######to access matplotlib in jupyter
%matplotlib inline
highs.plot()
#########to aggregate many values at a time #############
df.resample('W').mean() ##gives mean in all rows for all rows in a week
df.resample('W').agg({'Close':'mean','High':'max','Low':'min','Volume':'sum'})
'''

###READING /WRITING FILES FROM TO JSON,CSV,TSV,EXCEL,SQL
'''
########TO WRITE TO CSV File
india_df.to_csv('data/modifies.csv')
######TSV [TAB SEPARATED VALUES]
########TO WRITE ##########
india_df.to_csv('data/modified.tsv',sep='\t')
# india_df.to_csv('data/modified.tsv',sep='-')

##########TO RED TSV FILE ########
tsv_df=pd.read_csv('data/modified.tsv',sep='\t')
#########3EXCEL FILES  #########
pip install xlwt xlrd openpyxl  #openpyxl for new xlxs files
  TO WRITE TO EXCEL FILES 
  india_df.to_excel('data/modified.xlsx')
  TO READ EXCEL FILES 
  test_df=pd.read_excel('data/modified.xlsx',index_col='Respondent') #index_col is not necessary
#########TO WRITE TO JSON##########
india_df.to_json('data/modified.json',orient='records',lines=True) #orient lines are made data more readable
 THE WAY JSON IS WRITTEN TO ,MUST BE READ ALSO SAME WAY
 test=pd.read_json('data/modified.json',orient='records',lines=True)
 test=pd.read_json('data/modified.json')
 #######3READ WRITE SQL ############3   
 ORM =OBJECT RELATIONAL MATTER
 pip install SQLAlchemy
 if you use postgresql  then again pip install psycopg2-binary
 IF YOU USE MYSQL THEN BELOW CMD
 pip install mysql-connector-python
 
 ==========sql lite is built in db connector onlyy for local disk================
 from sqlalchemy import create_engine
 engine = create_engine('sqlite:///giraffe.db')
 =======================TO ACCESS mysql DB====================== 
 engine = create_engine('mysql+mysqlconnector://root:password@localhost/giraffe')
 df=pd.read_sql('branch',engine)
 =================to write ==================
 df.to_sql('tablename',engine,ifexists='append')  ##if_exits='replace'
 ==============to do a particular query============
 df=pd.read_sql_query('write query here',engine)
'''