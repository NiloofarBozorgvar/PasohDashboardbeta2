#----------------------------------------------------------------------------------------------text box
import time

import streamlit as st
def display_design_element():
    #st.subheader("***")

    text = (
        "In this Section you can see the Digital twin of the Pasoh Forest (for 2 hectare) in year 2019."
    )
    font_size = 17
    font_color = "#333333"
    border_color = "#568203"
    background_color = "#FFFFFF"
    border_width = 2

    styled_text = f"""
        <div style="padding: 10px; border: {border_width}px solid {border_color};
                    border-radius: 5px; background-color: {background_color};">
            <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
        </div>
    """

    st.markdown(styled_text, unsafe_allow_html=True)

st.title('📌 Pasoh Forest Reserve - Digital Twin')
display_design_element()
#----------------------------------------------------------------------------------------3D Location
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load your dataset
data = pd.read_csv('All1521.csv')
data = data[['XCO', 'YCO', 'Height', 'Species', 'DBH']]  # Considering 'DBH' as the column for Diameter at Breast Height

# Filter out trees with DBH=0
data = data[data['DBH'] != 0]

# Map species to categorical values for color representation
data['SP_category'] = pd.Categorical(data['Species'])
data['SP_code'] = data['SP_category'].cat.codes

# Get unique species values for the selectbox
species_list = data['Species'].unique().tolist()

def mapshow_3d_with_line(df, key):
    fig = go.Figure()

    # Add tree points in 3D scatter plot
    fig.add_trace(go.Scatter3d(
        x=df['XCO'], y=df['YCO'], z=df['Height'],
        mode='markers',
        marker=dict(color=df['SP_code'], size=df['Height'], colorscale='Viridis', colorbar=dict(title='Species')),
        name='Species'
    ))

    # Add lines from each tree to its top based on height
    for i, row in df.iterrows():
        fig.add_trace(go.Scatter3d(
            x=[row['XCO'], row['XCO']], y=[row['YCO'], row['YCO']],
            z=[0, row['Height']],
            mode='lines',
            line=dict(color='#5E4C3E', width=3),
            showlegend=False
        ))

    # Update layout for larger plot
    fig.update_layout(
        scene=dict(
            xaxis_title='XCO Title',
            yaxis_title='YCO Title',
            zaxis_title='Tree Height',
        ),
        title='3D Tree Locations with Heights and Lines Representing Tree Heights',
        width=800,  # Adjust the width of the plot
        height=800,  # Adjust the height of the plot
    )

    st.plotly_chart(fig, key=key)

# Dropdown to select species
selected_species = st.multiselect('Select Species to see their 3D location with height (Excluding DBH=0)',
                                 species_list, key='unique_key')

if selected_species:
    filtered_df = data[data['Species'].isin(selected_species)]
    mapshow_3d_with_line(filtered_df, key='unique_chart')
else:
    mapshow_3d_with_line(data, key='unique_chart')
#########################################################################################################################

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Assuming you have loaded the two datasets into pandas DataFrames
trees_2019_df = pd.read_csv('Trees_2019.csv')
hdiversity_df = pd.read_csv('Prescription stremlit/HDiversity.csv')

# Merge the two datasets based on the "TAG" column
merged_df = pd.merge(trees_2019_df, hdiversity_df[['TAG']], how='left', on='TAG')

# Create a new column "harvested" with 1 if the "TAG" is present in both datasets, else 0
merged_df['harvested'] = merged_df['TAG'].apply(lambda x: 1 if x in hdiversity_df['TAG'].values else 0)

# Save the resulting DataFrame to HarvestingTrees_2019.csv
print(merged_df)
merged_df.to_csv('HarvestingTrees_2019.csv', index=False)
merged_df['SP_category'] = pd.Categorical(merged_df['Species'])
merged_df['SP_code'] = merged_df['SP_category'].cat.codes

def mapshow_3d_with_line_harvested(df, key):
    fig = go.Figure()

    # Use the color scale from the original map
    color_scale_original = px.colors.sequential.Viridis

    # Add tree points in 3D scatter plot
    for i, row in df.iterrows():
        if row['harvested'] == 1:
            # Tree is harvested, use black color
            color = 'black'
        else:
            # Tree is not harvested, use color based on species
            color = color_scale_original[row['SP_code'] % len(color_scale_original)]

        # Add lines from each tree to its top based on height
        fig.add_trace(go.Scatter3d(
            x=[row['XCO'], row['XCO']], y=[row['YCO'], row['YCO']],
            z=[0, row['Height']],
            mode='lines',
            line=dict(color='#5E4C3E', width=3),
            showlegend=False
        ))

        # Add scatter points for the tree tops with transparency
        fig.add_trace(go.Scatter3d(
            x=[row['XCO']],
            y=[row['YCO']],
            z=[row['Height']],
            mode='markers',
            marker=dict(
                color=color,
                size=18,  # Adjust the size of the markers
                opacity=0.8,  # Adjust the opacity (transparency)
                line=dict(
                    color='#ffffff',  # Set the border color to black
                    width=1  # Adjust the border width
                )
            ),
            showlegend=False
        ))

    # Update layout for larger plot with rectangular aspect ratio
    fig.update_layout(
        scene=dict(
            xaxis_title='XCO Title',
            yaxis_title='YCO Title',
            zaxis_title='Tree Height',
            aspectmode='manual',  # Set aspect ratio manually
            aspectratio=dict(x=1, y=2.3, z=0.8),  # Adjust the aspect ratio as needed
        ),
        title='3D representation of Harvested Trees with Transparent Circles',
        width=800,  # Adjust the width of the plot
        height=800,  # Adjust the height of the plot
    )

    st.plotly_chart(fig, key=key)

# Display the 3D plot with harvested trees
mapshow_3d_with_line_harvested(merged_df, key='unique_chart3')

########################################################################################################################

#-------------------------------------------------------------------------------------remainig trees
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Assuming you have loaded the two datasets into pandas DataFrames
trees_2019_df = pd.read_csv('Trees_2019.csv')
hdiversity_df = pd.read_csv('Prescription stremlit/HDiversity.csv')

# Merge the two datasets based on the "TAG" column
merged_df = pd.merge(trees_2019_df, hdiversity_df[['TAG']], how='left', on='TAG')

# Create a new column "harvested" with 1 if the "TAG" is present in both datasets, else 0
merged_df['harvested'] = merged_df['TAG'].apply(lambda x: 1 if x in hdiversity_df['TAG'].values else 0)

# Save the resulting DataFrame to HarvestingTrees_2019.csv
print(merged_df)
merged_df.to_csv('HarvestingTrees_2019.csv', index=False)
merged_df['SP_category'] = pd.Categorical(merged_df['Species'])
merged_df['SP_code'] = merged_df['SP_category'].cat.codes

def mapshow_3d_with_line_harvested(df, key):
    fig = go.Figure()

    # Use the color scale from the original map
    color_scale_original = px.colors.sequential.Viridis

    # Add tree points in 3D scatter plot
    for i, row in df.iterrows():
        if row['harvested'] == 1:
            # Tree is harvested, use black color
            color = 'black'
        else:
            # Tree is not harvested, use color based on species
            color = color_scale_original[row['SP_code'] % len(color_scale_original)]

        # Add lines from each tree to its top based on height
        fig.add_trace(go.Scatter3d(
            x=[row['XCO'], row['XCO']], y=[row['YCO'], row['YCO']],
            z=[0, row['Height']],
            mode='lines',
            line=dict(color='#5E4C3E', width=3),
            showlegend=False
        ))

        # Add scatter points for the tree tops with transparency
        fig.add_trace(go.Scatter3d(
            x=[row['XCO']],
            y=[row['YCO']],
            z=[row['Height']],
            mode='markers',
            marker=dict(
                color=color,
                size=18,  # Adjust the size of the markers
                opacity=0.8,  # Adjust the opacity (transparency)
                line=dict(
                    color='#ffffff',  # Set the border color to black
                    width=1  # Adjust the border width
                )
            ),
            showlegend=False
        ))

    # Update layout for larger plot with rectangular aspect ratio
    fig.update_layout(
        scene=dict(
            xaxis_title='XCO Title',
            yaxis_title='YCO Title',
            zaxis_title='Tree Height',
            aspectmode='manual',  # Set aspect ratio manually
            aspectratio=dict(x=1, y=2.3, z=0.8),  # Adjust the aspect ratio as needed
        ),
        title='3D representation of Harvested Trees with Transparent Circles',
        width=800,  # Adjust the width of the plot
        height=800,  # Adjust the height of the plot
    )

    st.plotly_chart(fig, key=key)

# Display the 3D plot with harvested trees

merged_df_harvested = merged_df[merged_df['harvested'] == 0]
mapshow_3d_with_line_harvested(merged_df_harvested, key='unique_chart3')



