# Automate Excel Sheet
# pip install pandas
import pandas as excel
# read excel file
df = excel.read_excel('excel.xlsx', sheet_name='Sheet1')
# print dataframe
print(df)
# Read by column name
print(df['Age'])
# Read by row number
print(df['Salary'][1])
# Read by row and column number
print(df[0][1])
# Get total rows and columns
row, col = df.shape
print(row, col)
# read by cell
print(df.iat[1, 1])
# Write by cell
df.iat[1, 1] = 'New Value'
# Write by row
df.loc[1, 'Salary'] = 'New Value'
# Write by column
df.loc[:, 'Salary'] = 'New Value'
# Append new row
df.loc[row+1] = ['New Value', 'New Value']
# Append new column
df.loc[:, col+1] = 'New Value'
# save to excel file
df.to_excel('excel.xlsx', sheet_name='Sheet1')

# PLOT GRAPHS
# Create Beautiful Graphs
# pip install plotly
import plotly.express as plotly
import plotly.graph_objects as graph
# Draw Bar Chart
plot = plotly.bar(x=['D1', 'D2', 'D3'], y=[1, 2, 3])
plot.show()
# Draw Scatter Chart
plot = plotly.scatter(x=[1, 2, 3], y=[1, 2, 3])
plot.show()
# Draw Pie Chart
plot = plotly.pie(labels=['D1', 'D2', 'D3'], values=[1, 2, 3])
plot.show()
# Draw Histogram
plot = plotly.histogram(x=[1, 2, 3])
plot.show()
# Draw Box Plot
plot = plotly.box(x=[1, 2, 3])
plot.show()
# Draw Finnance Candlestick Chart
plot = graph.Figure(data=[graph.Candlestick(x=[1, 2, 3], open=[1, 2, 3], high=[1, 2, 3], low=[1, 2, 3], close=[1, 2, 3])])
plot.show()
# Time series Stock Chart
data = plotly.data.stocks()
plot = plotly.line(data, x="Date", y="Stock")
plot.show()
