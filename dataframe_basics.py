import pandas

# create a dataframe with list of lists
df1 = pandas.DataFrame([[2,4,6], [10,20,30]], columns=["Price", "Age", "Value"])

print(df1)

# Extract average of all columns over the rows
print(df1.mean())

# the type of df1.mean() is a pandas.core.series.Series object
print(type(df1.mean()))

# Returns the mean of the series returned by df1.mean()
print(df1.mean().mean())

# Series is basically one column values for all rows
print("Price Series: \n", df1.Price)

# create a dataframe with list of dict
df2 = pandas.DataFrame([{"Name": "John", "Age": 20},{"Name": "Jack"}])

print(df2)



