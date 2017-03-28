import pandas

food_info = pandas.read_csv("food_info.csv") # can also pass http address where csv file is
# print type(food_info) #pandas.core.frame.DataFrame
#
# print food_info.head(2)
#
# # see all column names
# print food_info.columns
#
# # shape -> see dimension of dataframe
# dimensions = food_info.shape
# num_rows = dimensions[0]
# num_cols = dimensions[1]
# print num_rows
#
# #print 2 row
# print food_info.loc[1]
# print food_info.loc[0:3]
# # getting multiple rows
# print food_info.loc[[2, 4, 6]]
#
#
# zinc = food_info["Zinc_(mg)"]
# print type(zinc)    # pandas.core.series.Series
#
# zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]
# print zinc_copper
#
# food_info.describe()
#
# # shows data type of each column
# # print food_info.dtypes
#
# # converting text DATE column data to date data type using to_datetime
# # unrate = pd.read_csv("unrate.csv")
# # unrate["DATE"]=pd.to_datetime(unrate["DATE"])

print food_info.columns
print food_info["NDB_No"].head()

# rename column name from old to new
# food_info.rename(columns={'NDB_No': 'Id'}, inplace=True)

# # column_new_names=['Id','Short Description','Water']
# # food_info.columns=column_new_names
# # can also apply new column names while getting data from csv
# # food_info = pd.read_csv("food_info.csv",names=column_new_names,header=0)
# # replacing food column names
# # food_info.columns.str.replace(' ','_')

# # drops column by name
# food_info.drop(['Energ_Kcal','Protein_(g)'],axis=1,inplace=True)
# print food_info.head()

# # dropping rows by specifying row numbers
# food_info.drop([0, 1], axis=0, inplace=True)

# sorts and print only given column sorted
# print food_info['Shrt_Desc'].sort_values()
# print food_info['Water_(g)'].sort_values(ascending=False)

print food_info.head()
# sorts given dataframe by given column order and prints all series
print food_info.sort_values(['Water_(g)', 'Shrt_Desc'], ascending=False)

# FILTERING DATA
# filtering rows having Water_(g) > 40 and Protein_(g) > 1 -> returns filtered dataframe
print food_info[(food_info['Water_(g)'] > 40) & (food_info['Protein_(g)'] == 1)].head()

# print food_info.head()