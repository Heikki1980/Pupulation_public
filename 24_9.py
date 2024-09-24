'''
29. Use the same population data as in the previous exercise.

a) Create a new Pandas data frame where the first column is the year and other 142 columns are populations of all the countries in the data
b) Use streamlit and create an interactive web graph where you can select the countries to be included in the population plot

30. Bonus task Upload your Python script and data from task 29 to Git repository. Test that you can create the visualization by running streamlit run <script repository>.
'''
import pandas as pd
import streamlit as st
from IPython.display import display
file = "C:\\Users\\hived\\Desktop\\Haku yamk\\Kurssit\\Data analytics and mathematics\\population.csv"
df = pd.read_csv(file) # Unnamed country continent year lifeExp pop gdpPercap iso_alpha iso_num
df = df.drop(columns=['Unnamed: 0'])
# print(df.head())
# print(df.columns)
# lets define the list of column headers (country names) (except the first column which is the year)
uniques_names = df['country'].unique().tolist()
# print(uniques_names)

# lets define the years (the first column)
years = df['year'].unique()
# print(years)

# then create the first column of dataframe
df_visu = pd.DataFrame(years, columns=['year'])
# print(df_visu)

# display(df_visu.head())
# what should we have in the other columns? Population by country
# for example Sweden
# print(df[df['country'] == 'Sweden']['pop'].values)

# for all countries, this works but it's not the best or fastest code.
for country_name in uniques_names:
    df_visu[country_name] = df[df['country'] == country_name]['pop'].values
#print(df_visu)

# Make graphics
# define figure title
st.title('Population plot')

# define selector (columns to draw)
columns = st.multiselect('Countries: ', uniques_names)

# plot the line chart
# instead of the code below use terminal to run streamlit run 24_9.py and that will open browser with the graph
st.line_chart(df_visu, x='year', y=columns, y_label='Population', x_label='Year')
