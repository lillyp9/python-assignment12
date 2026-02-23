import plotly.express as px
import plotly.data as pldata
import pandas as pd

#Load data
df = pldata.wind(return_type='pandas')

#Print first and last 10 lines
print(df.head(10))
print(df.tail(10))

#Clean data 
#strengthe column loks like "0-1, "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10"
#Take away the - and have it be a whole number (use regex)
print(df['strength'].unique()) # see the unique values in the strengthe column
df['strength'] = df['strength'].str.replace('-.*', '', regex=True) #find the - and everything after it and replace with nothing

print(df['strength'])

#Create Scatter plot 
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color= 'direction',
    title='Wind Strength vs Frequency by Direction',
    labels={
        'strength': 'Wind Strength', 
        'frequency': 'Frequency',
        'direction': 'Wind Direction'
    
}
)
#Save to HTML
fig.write_html('wind_scatter.html')
#Show plot
fig.show()
