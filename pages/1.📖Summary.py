#----------------------------------------------------------------------------------------------text box
import streamlit as st

def display_design_element():
    st.subheader("Pasoh Forest Malaysia")

    text = ("Investigating the Pasoh Forest dataset for the year 2019 reveals a view of its ecological attributes. "
            "The dataset encapsulates vital information about various tree species, their attributes, "
            "and the ecosystem's dynamics. Analyzing this dataset offers insights into the forest's species diversity, "
            "size classes, growth rates, and spatial distribution. "
            "Understanding these facets provides understanding of Pasoh Forest's ecological dynamics, "
            "aiding in ecosystem management and conservation strategies.👋")
    font_size = 19
    font_color = "#333333"  # Dark grey
    border_color = "#FFA500"  # Orange
    border_width = 2

    # Display the bordered text box for design visualization
    st.markdown(
        f"""
        <div style="padding:10px; border: {border_width}px solid {border_color}; border-radius: 5px;">
            <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    st.title('Ecology Simulator')

    # Display the design element
    display_design_element()
#--------------------------------------------------------------------------------------------Call Text Box
if __name__ == "__main__":
    main()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
#------------------------------------------------------------------------------------Metrics

col1, col2, col3 = st.columns(3)

# Custom styling for buttons
button_style = """
    height: 80px;
    width: 230px;
    background-color: #FFCFAB; 
    color: #414F4C; /* White text color */
    border: px solid #008CBA; 
    border-radius: 5px; 
"""

# Button 1
col1.markdown(f'<button style="{button_style}"> 🏞️                         Number of Hectare: 2</button>', unsafe_allow_html=True)

# Button 2
col2.markdown(f'<button style="{button_style}">🌳🌳 Number of Trees: 1944</button>', unsafe_allow_html=True)

# Button 3
col3.markdown(f'<button style="{button_style}">🌲 🌴 Number of Species: 380</button>', unsafe_allow_html=True)



#-------------------------------------------------------------------Number of Trees and SP in each DBH for Year 2019

st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

All1521 = pd.read_csv('All1521.csv')  # Replace 'All1521.csv' with the correct file path

# Display the first plot in the left column using Streamlit
col1, col2 = st.columns([1, 1])
with col1:
    All1521 = pd.read_csv('All1521.csv')  # Replace 'your_dataset_file.csv' with the correct file path

    # Title for the web app
    st.subheader('Number of Trees in each DBH Class by Inch, Year 2019')

    All1521['Size Class by Inch'] = All1521['Size Class by Inch'].astype(str)
    # Filtering data for the year 2019 and Size Class by Inch not equal to 0 using query
    data_2019 = All1521.query("(Year == 2019) & (`Size Class by Inch` != '0') ")

    print(data_2019['Size Class by Inch'].astype(str))
    # Grouping data by 'Size Class by Inch' and counting the number of trees
    tree_count = data_2019.groupby('Size Class by Inch')['TAG'].count().reset_index()

    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(tree_count['Size Class by Inch'], tree_count['TAG'], color='skyblue')
    plt.xlabel('Size Class by Inch')
    plt.ylabel('Number of Trees')
    plt.title('Number of Trees in Each DBH Class by Inch (Year 2019)')
    plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
    plt.tight_layout()

    # Display the plot using Streamlit
    st.pyplot(plt)
with col2:
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt

    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')

    # Title for the web app
    st.subheader('Number of Species in each DBH Class by Inch, Year 2019')

    All1521['Size Class by Inch'] = All1521['Size Class by Inch'].astype(str)

    # Filtering data for the year 2019 and Size Class by Inch not equal to 0 using query
    data_2019 = All1521.query("(Year == 2019) & (`Size Class by Inch` != '0') ")

    # Grouping data by 'Size Class by Inch' and counting the number of unique species
    species_count = data_2019.groupby('Size Class by Inch')['Species'].nunique().reset_index()

    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(species_count['Size Class by Inch'], species_count['Species'], color='green')
    plt.xlabel('Size Class by Inch')
    plt.ylabel('Number of Species')
    plt.title('Number of Species in Each DBH by Inch (Year 2019)')
    plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
    plt.tight_layout()

    # Display the plot using Streamlit
    st.pyplot(plt)
#------------------------------------------------------------------------------------AGB and carbon stock in each DBH class
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
All1521 = pd.read_csv('All1521.csv')


All1521['Size Class by Inch'] = All1521['Size Class by Inch'].astype(str)

# Filtering data for the year 2019 and Size Class by Inch not equal to 0 using query
data_2019 = All1521.query("(Year == 2019) & (`Size Class by Inch` != '0') ")

# Grouping data by 'Size Class by Inch' and calculating AGB and Carbon Stock
agb_carbon_data = data_2019.groupby('Size Class by Inch').agg({
    'DBH': 'sum',        # Assuming 'DBH' represents Above-Ground Biomass (AGB)
    'Carbon': 'sum'      # Assuming 'Carbon' represents Carbon Stock
}).reset_index()

# Colors for each DBH class size
colors = sns.color_palette('viridis', n_colors=len(agb_carbon_data['Size Class by Inch']))

# Creating the pie chart for AGB
plt.figure(figsize=(14, 8))
plt.pie(agb_carbon_data['DBH'], labels=agb_carbon_data['Size Class by Inch'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Above-Ground Biomass (AGB) Distribution by DBH Class (Year 2019)')

# Display the AGB pie chart using Streamlit in column 1
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader('AGB Distribution by DBH Class, Year 2019')

    st.pyplot(plt)

# Creating the pie chart for Carbon Stock
plt.figure(figsize=(10, 6))
plt.pie(agb_carbon_data['Carbon'], labels=agb_carbon_data['Size Class by Inch'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Carbon Stock Distribution by DBH Class (Year 2019)')

# Display the Carbon Stock pie chart using Streamlit in column 2
with col2:
    st.subheader('Carbon Stock Distribution by DBH Class, Year 2019')

    st.pyplot(plt)

#------------------------------------------------------------------------------------Density and basal erea in each DBH class

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
All1521 = pd.read_csv('All1521.csv')


All1521['Size Class by Inch'] = All1521['Size Class by Inch'].astype(str)

# Filtering data for the year 2019 and Size Class by Inch not equal to 0 using query
data_2019 = All1521.query("(Year == 2019) & (`Size Class by Inch` != '0') ")

# Grouping data by 'Size Class by Inch' and calculating Density and Basal Area
density_basal_data = data_2019.groupby('Size Class by Inch').agg({
    'Density': 'sum',
    'Basal Area': 'sum'
}).reset_index()

# Colors for each DBH class size
colors = sns.color_palette('Set3', n_colors=len(density_basal_data['Size Class by Inch']))

# Creating the pie chart for Density
plt.figure(figsize=(10, 6))
plt.pie(density_basal_data['Density'], labels=density_basal_data['Size Class by Inch'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Density Distribution by DBH Class (Year 2019)')

# Display the Density pie chart using Streamlit in column 1
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader('Density  Distribution by DBH Class, Year 2019')

    st.pyplot(plt)

# Creating the pie chart for Basal Area
plt.figure(figsize=(10, 6))
plt.pie(density_basal_data['Basal Area'], labels=density_basal_data['Size Class by Inch'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Basal Area Distribution by DBH Class (Year 2019)')

# Display the Basal Area pie chart using Streamlit in column 2
with col2:
    st.subheader('Basal Area Distribution by DBH Class, Year 2019')

    st.pyplot(plt)




#-------------------------------------------------------------------------------------------------Scatter plot location
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

import plotly.express as px

def mapshow2019(df):
    df['SP'] = df['SP'].astype('category')  # Convert 'SP' column to categorical

    fig = px.scatter(df, x='XCO', y='YCO', color='SP')

    # Update title attributes
    fig.update_layout(
        title=dict(text='Actual Location of Trees in 2019', x=0.3, y=0.9,  # Adjust x and y to change title position
                   font=dict(color='dark green', size=20, family='Arial')),  # Change title font attributes
        xaxis_title=dict(text='XCO Title', font=dict(color='green')),  # Change x-axis title and color
        yaxis_title=dict(text='YCO Title', font=dict(color='green'))  # Change y-axis title and color
    )

    st.plotly_chart(fig)

    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

data = pd.read_csv('AllNew.csv')
data = data[['XCO', 'YCO', 'SP']]
df = pd.DataFrame(data)
print(df.columns.str.strip())

# Get unique species values for the selectbox
species_list = df['SP'].unique().tolist()
#--------------az inja
selected_species = st.multiselect('Select Species to see their location', species_list)

if selected_species:
    filtered_df = df[df['SP'].isin(selected_species)]
    mapshow2019(filtered_df)
else:
#--------ta inja pak konam agar nakhastam select box bashe
    mapshow2019(df)
#----------------------------------------------------------------------------------------------Location plot based on DBH


import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.subheader('3D Tree Location by DBH Class, Year 2019')


def mapshow_3d_with_line(df, key):
    fig = go.Figure()

    # Create a mapping of Size Class by Inch to colors
    df['Size Class by Inch'] = df['Size Class by Inch'].astype('category')  # Convert 'Size Class by Inch' to categorical

    size_class_colors = {'1-5': '#205c40', '6-11': '#76ff7a', '12-17': '#fdfc74', '18-23': '#ff8243', '>24': '#bc5d58'}  # Exclude '0' key

    # Add tree points in 3D scatter plot
    fig.add_trace(go.Scatter3d(
        x=df['XCO'], y=df['YCO'], z=df['Height'],
        mode='markers',
        marker=dict(color=df['Size Class by Inch'].map(size_class_colors), size=df['Height']),
        name='Size Class'
    ))

    # Add lines from each tree to its top based on height
    for i, row in df.iterrows():
        fig.add_trace(go.Scatter3d(
            x=[row['XCO'], row['XCO']],
            y=[row['YCO'], row['YCO']],
            z=[0, row['Height']],
            mode='lines',
            line=dict(color='#5E4C3E', width=3),
            showlegend=False
        ))


    fig.update_layout(
        scene=dict(
            xaxis_title='XCO Title',
            yaxis_title='YCO Title',
            zaxis_title='Tree Height',
            aspectmode='manual',  # Set aspect ratio manually
            aspectratio=dict(x=1, y=2, z=0.8),  # Adjust the aspect ratio as needed
        ),
        title='3D Tree location by DBH size',
        width=800,  # Adjust the width of the plot
        height=800,  # Adjust the height of the plot
    )
    # Update layout for larger plot


    st.plotly_chart(fig, key=key)

# Load the dataset
data = pd.read_csv('All1521.csv')
df = pd.DataFrame(data)

#--------------az inja
selected_size_class = st.multiselect('Select Size Class to see their location', sorted(df['Size Class by Inch'].unique().tolist()), default=['1-5', '6-11', '12-17', '18-23', '>24'])

if selected_size_class:
    filtered_df = df[df['Size Class by Inch'].isin(selected_size_class)]
    mapshow_3d_with_line(filtered_df, key='3d_plot')
else:
#--------ta inja pak konam agar nakhastam select box bashe
    mapshow_3d_with_line(df, key='3d_plot')





#---------------------------------------------------------------------------------------------pie chart SP in Hectrae 1 & 2
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

col1, col2 = st.columns([1, 1])

with col1:
    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')  # Replace 'All1521.csv' with the correct file path

    # Title for the web app
    st.subheader('Most frequent Species in Hectare 1 (Year 2019)')

    # Filtering data for Hectare 1 and the year 2019
    hectare_1_2019 = All1521[(All1521['Hectare'] == 1) & (All1521['Year'] == 2019)]

    # Grouping data by 'Species' and calculating tree count for each species
    species_count = hectare_1_2019['Species'].value_counts().reset_index()
    species_count.columns = ['Species', 'TreeCount']

    # Selecting top 20 species based on tree count
    top_20_species = species_count.head(10)

    # Creating a horizontal bar chart for top 20 species in Hectare 1 for year 2019
    plt.figure(figsize=(8, 8))
    plt.barh(top_20_species['Species'], top_20_species['TreeCount'], color='pink')
    plt.title('Hectare 1, Year 2019')
    plt.xlabel('Tree Count')
    plt.ylabel('Species')
    plt.tight_layout()

    # Display the horizontal bar chart using Streamlit
    st.pyplot(plt)

with col2:
    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')

    # Title for the web app
    st.subheader('Most frequent Species in Hectare 2 (Year 2019)')

    # Filtering data for Hectare 2 and the year 2019
    hectare_2_2019 = All1521[(All1521['Hectare'] == 2) & (All1521['Year'] == 2019)]

    # Grouping data by 'Species' and calculating tree count for each species
    species_count = hectare_2_2019['Species'].value_counts().reset_index()
    species_count.columns = ['Species', 'TreeCount']

    # Selecting top 20 species based on tree count
    top_20_species = species_count.head(10)

    # Creating a horizontal bar chart for top 20 species in Hectare 2 for year 2019
    plt.figure(figsize=(8, 8))
    plt.barh(top_20_species['Species'], top_20_species['TreeCount'], color='lightcoral')
    plt.title('Hectare 2, Year 2019')
    plt.xlabel('Tree Count')
    plt.ylabel('Species')
    plt.tight_layout()

    # Display the horizontal bar chart using Streamlit
    st.pyplot(plt)


#----------------------------------------------------------------------------------------  AGB in Hectrae 1 & 2
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

col1, col2 = st.columns([1, 1])
with col1:
    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')  # Replace 'All1521.csv' with the correct file path

    # Title for the web app
    st.subheader('Above-Ground Biomass (AGB) in Each Hectare, Year 2019')

    # Filtering data for the year 2019
    data_2019 = All1521[All1521['Year'] == 2019]

    # Clean 'AGB' column (remove non-numeric characters, commas, etc.)
    data_2019['AGB'] = data_2019['AGB'].str.replace(r'[^0-9.]', '', regex=True)

    # Convert 'AGB' column to numeric
    data_2019['AGB'] = pd.to_numeric(data_2019['AGB'], errors='coerce')

    # Grouping data by 'Hectare' and calculating total AGB for each Hectare
    hectare_agb = data_2019.groupby('Hectare')['AGB'].sum().reset_index()

    # Creating a bar chart for AGB in each Hectare for year 2019
    plt.figure(figsize=(8, 6))
    plt.bar(hectare_agb['Hectare'], hectare_agb['AGB'], color='skyblue')
    plt.xlabel('Hectare')
    plt.ylabel('Above-Ground Biomass (AGB)')
    plt.title('Above-Ground Biomass (AGB) in Each Hectare, Year 2019')
    plt.xticks(hectare_agb['Hectare'])
    plt.tight_layout()

    # Display the bar chart using Streamlit
    st.pyplot(plt)
#---------------------
with col2:
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt

    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')  # Replace 'All1521.csv' with the correct file path

    # Title for the web app
    st.subheader('Top 10 Species with most Above-Ground Biomass (AGB) Values, Year 2019')

    # Filtering data for the year 2019
    data_2019 = All1521[All1521['Year'] == 2019]

    # Convert 'AGB' column to numeric
    data_2019['AGB'] = pd.to_numeric(data_2019['AGB'], errors='coerce')

    # Grouping data by 'Species' and calculating total AGB for each species
    species_agb = data_2019.groupby('Species')['AGB'].sum().reset_index()

    # Sorting species by AGB in descending order
    species_agb_sorted = species_agb.sort_values(by='AGB', ascending=False)

    # Selecting top 10 species based on total AGB
    top_10_species_agb = species_agb_sorted.head(10)

    # Reverse the order of species for plotting
    top_10_species_agb = top_10_species_agb[::-1]

    # Creating a bar chart for top 10 species by AGB
    plt.figure(figsize=(10, 8))
    plt.barh(top_10_species_agb['Species'], top_10_species_agb['AGB'], color='skyblue')
    plt.xlabel('Above-Ground Biomass (AGB)')
    plt.ylabel('Species')
    plt.title('Top 10 Species by Above-Ground Biomass (AGB) - Year 2019')
    plt.tight_layout()

    # Display the bar chart using Streamlit
    st.pyplot(plt)

#----------------------------------------------------------------------------------------  Carbon Stock in Hectrae 1 & 2
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

col1, col2 = st.columns([1, 1])
with col1:
    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')

    # Title for the web app
    st.subheader('Carbon Stock in Each Hectare, Year 2019')

    # Filtering data for the year 2019
    data_2019 = All1521[All1521['Year'] == 2019]

    # Grouping data by 'Hectare' and calculating total Carbon for each Hectare
    hectare_carbon = data_2019.groupby('Hectare')['Carbon'].sum().reset_index()

    # Creating a bar chart for Carbon in each Hectare for year 2019
    plt.figure(figsize=(10, 8))
    plt.bar(hectare_carbon['Hectare'], hectare_carbon['Carbon'], color='orange')
    plt.xlabel('Hectare')
    plt.ylabel('Carbon')
    plt.title('Carbon Stock in Each Hectare - Year 2019')
    plt.xticks(hectare_carbon['Hectare'])
    plt.tight_layout()

    # Display the bar chart using Streamlit
    st.pyplot(plt)
#------------------
with col2:
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt

    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')  # Replace 'All1521.csv' with the correct file path

    # Title for the web app
    st.subheader('Top 10 Species with most Carbon Stock, Year 2019')

    # Filtering data for the year 2019
    data_2019 = All1521[All1521['Year'] == 2019]

    # Grouping data by 'Species' and calculating total Carbon for each species
    species_carbon = data_2019.groupby('Species')['Carbon'].sum().reset_index()

    # Selecting top 20 species based on total Carbon
    top_20_species_carbon = species_carbon.nlargest(10, 'Carbon')

    # Creating a bar chart for top 20 species by Carbon
    plt.figure(figsize=(10, 8))
    plt.barh(top_20_species_carbon['Species'], top_20_species_carbon['Carbon'], color='orange')
    plt.xlabel('Carbon')
    plt.ylabel('Species')
    plt.title('Top 10 Species by Carbon Stock - Year 2019')
    plt.tight_layout()

    # Display the bar chart using Streamlit
    st.pyplot(plt)

#----------------------------------------------------------------------------------------  IV in Hectrae 1 & 2
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

col1, col2 = st.columns([1, 1])
with col1:
    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')

    # Title for the web app
    st.subheader('Important Value (IV) in Each Hectare, Year 2019')

    # Filtering data for the year 2019
    data_2019 = All1521[All1521['Year'] == 2019]

    # Clean 'IV' column - Remove non-numeric characters
    data_2019['IV'] = data_2019['IV'].str.replace('[^\d.]', '', regex=True)

    # Convert 'IV' column to numeric
    data_2019['IV'] = pd.to_numeric(data_2019['IV'], errors='coerce')

    # Grouping data by 'Hectare' and calculating total IV for each Hectare
    hectare_iv = data_2019.groupby('Hectare')['IV'].sum().reset_index()

    # Creating a bar chart for IV in each Hectare for year 2019
    plt.figure(figsize=(10, 8))
    plt.bar(hectare_iv['Hectare'], hectare_iv['IV'], color='purple')
    plt.xlabel('Hectare')
    plt.ylabel('Important Value (IV)')
    plt.title('Important Value (IV) in Each Hectare, Year 2019')
    plt.xticks(hectare_iv['Hectare'])
    plt.tight_layout()

    # Display the bar chart using Streamlit
    st.pyplot(plt)
#---------------
with col2:
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt

    # Load the dataset
    All1521 = pd.read_csv('All1521.csv')

    # Title for the web app
    st.subheader('Top 10 Species with most IV (Important Value), Year 2019')

    # Filtering data for the year 2019
    data_2019 = All1521[All1521['Year'] == 2019]

    # Clean 'IV' column - Remove non-numeric characters and convert to numeric
    data_2019['IV'] = pd.to_numeric(data_2019['IV'].str.replace('[^\d.]', '', regex=True), errors='coerce')

    # Grouping data by 'Species' and calculating total IV for each species
    species_iv = data_2019.groupby('Species')['IV'].sum().reset_index()

    # Selecting top 20 species based on total IV
    top_20_species_iv = species_iv.nlargest(10, 'IV')

    # Creating a bar chart for top 20 species by IV
    plt.figure(figsize=(10, 8))
    plt.barh(top_20_species_iv['Species'], top_20_species_iv['IV'], color='purple')
    plt.xlabel('IV (Important Value)')
    plt.ylabel('Species')
    plt.title('Top 20 Species by most IV (Important Value), Year 2019')
    plt.tight_layout()

    # Display the bar chart using Streamlit
    st.pyplot(plt)
#-------------------------------------------------------------------------------------Density in each Quaderant

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
All1521 = pd.read_csv('All1521.csv')

# Title for the web app
st.subheader('Density in each QUADRANTS for Year 2019')

# Filtering data for the year 2019
data_2019 = All1521[All1521['Year'] == 2019]

# Grouping data by QUADRANT and calculating the sum of 'Density' column
quadrant_density_sum = data_2019.groupby('QUAD')['Density'].sum().reset_index()

# Create a bar plot with Plotly
fig = px.bar(
    quadrant_density_sum, x='QUAD', y='Density',
    labels={'QUAD': 'QUADRANT', 'Density': 'Sum of Density'},
    title='Density in each QUADRANTS for Year 2019',
    color='Density'
)
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))

# Display the bar plot using Streamlit
st.plotly_chart(fig)

#---------------------------------------------------------------------------------------Density across quaderants
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
All1521 = pd.read_csv('All1521.csv')  # Replace 'All1521.csv' with the correct file path

# Title for the web app
st.subheader('Density Across QUADRANTS, Year 2019 (Excluding Dead Trees)')

# Filtering data for the year 2019 and excluding dead trees ('Status' != 'Dead')
data_2019_alive = All1521[(All1521['Year'] == 2019) & (All1521['Status'] != 'Dead')]

# Create a scatter plot with Plotly
fig = px.scatter(
    data_2019_alive, x='XCO', y='YCO', size='Density', color='Density',
    hover_data=['Density', 'Species'],
    labels={'XCO': 'Longitude', 'YCO': 'Latitude', 'Density': 'Density'},
    title='Density Across QUADRANTS, Year 2019 (Excluding Dead Trees)'
)
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))

# Display the scatter plot using Streamlit
st.plotly_chart(fig)
#------------------------------------------------------------------------------ Top SP with Max Lifespan

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
All1521 = pd.read_csv('All1521.csv')  # Replace 'All1521.csv' with the correct file path

# Title for the web app
st.subheader('Top Species with Maximum Lifespan')

# Grouping data by 'Species' and calculating maximum lifespan for each species
species_max_lifespan = All1521.groupby('Species')['LifeSpan'].max().reset_index()

# Sorting the data to get the top species with the highest maximum lifespan
top_species_max_lifespan = species_max_lifespan.nlargest(20, 'LifeSpan')

# Create a donut chart using Plotly
fig = px.pie(
    top_species_max_lifespan, values='LifeSpan', names='Species',
    title='Top Species with Maximum Lifespan',
    hole=0.5  # Adjust the hole size for a donut shape
)

# Display the donut chart using Streamlit
st.plotly_chart(fig)
#-------------------------------------------------





















