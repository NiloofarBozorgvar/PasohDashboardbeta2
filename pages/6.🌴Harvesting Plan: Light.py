import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np



# ----------------------------------------------------------------------------------------------------Text Box
def display_design_element():
    st.subheader("Regime and Objective-based Simulation for Stand Prescription")

    text = (
        "In this section, we will see the different prescription scenarios. "
        "Also, the implications of the prescription are explained below."
    )
    font_size = 17
    font_color = "#333333"
    border_color = "#C4661F"
    background_color = "#F5F6F2"
    border_width = 2

    styled_text = f"""
        <div style="padding: 10px; border: {border_width}px solid {border_color};
                    border-radius: 5px; background-color: {background_color};">
            <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
        </div>
    """

    st.markdown(styled_text, unsafe_allow_html=True)

st.title('Ecology Simulator')
display_design_element()
#-----------------------------------------------------------------

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
st.write('For **Light Regime**, you will see the Number of Trees need to be harvest and the carbon loss, '
         'if this regime be applied. 🪵🪓')

#----------------------------------------------------------------------------------------------------Light Table

def display_table_Light():
    html_table = """
    <table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;">
        <thead>
            <tr>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Plan</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">#trees to harvest</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon loss</th>
                <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd; border-right: 3px solid #ddd;">Economic value</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">BDq Light regime</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">32</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">298168</td>
                <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">149835</td>
            </tr>
        </tbody>
    </table>
    """

    st.markdown(html_table, unsafe_allow_html=True)

display_table_Light()

#-------------------------------------------------------------------

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
st.write('Here, based on the objective you have, you can see the details of prescription plan')

#------------------------------------------------------------------------------------------------Objective Table


def display_table_objective():
    html_table = """
       <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #4F772D; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Diversity Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">361</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">4</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1930.84</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1466</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">13.67M</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">358</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">26</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">4</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">2</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1948.32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1482.17</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">14.01M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">362</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">29</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">3</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1931.08</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1467.02</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">13.66M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

display_table_objective()

#-----------------------------------------------------------------------------------------------
def mapshow2019(df):
    df['Species'] = df['Species'].astype('category')  # Convert 'SP' column to categorical

    fig = px.scatter(df, x='XCO', y='YCO', color='Species')

    # Update title attributes
    fig.update_layout(
        title=dict(text='Actual Location of Trees', x=0.3, y=0.9,  # Adjust x and y to change title position
                   font=dict(color='dark green', size=20, family='Arial')),  # Change title font attributes
        xaxis_title=dict(text='XCO Title', font=dict(color='green')),  # Change x-axis title and color
        yaxis_title=dict(text='YCO Title', font=dict(color='green'))  # Change y-axis title and color
    )

    st.plotly_chart(fig)

st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
st.write(' 🔔 Now by chossing buttons below 👇, you will se the 📍location of trees than need to be harvest base on your Objective.')

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)


if col1.button('***Diversity*** Objective;and Light regime'):
    import pandas as pd
    import plotly.graph_objects as go
    import plotly.express as px
    import streamlit as st

    # Assuming you have loaded the two datasets into pandas DataFrames
    trees_2019_df = pd.read_csv('Trees_2019.csv')
    hdiversity_df = pd.read_csv('Prescription stremlit/LDiversity.csv')

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
            title='3D representation of Trees that should be harvested using Harvesting Plan in (black color)',
            width=800,  # Adjust the width of the plot
            height=800,  # Adjust the height of the plot
        )

        st.plotly_chart(fig, key=key)


    # Display the 3D plot with harvested trees
    mapshow_3d_with_line_harvested(merged_df, key='unique_chart3')

    # -------------------------------------------------------------------------------------remaining trees
    import pandas as pd
    import plotly.graph_objects as go
    import plotly.express as px
    import streamlit as st

    # Assuming you have loaded the two datasets into pandas DataFrames
    trees_2019_df = pd.read_csv('Trees_2019.csv')
    hdiversity_df = pd.read_csv('Prescription stremlit/MDiversity.csv')

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
            title='3D representation of remaining trees after harvesting',
            width=800,  # Adjust the width of the plot
            height=800,  # Adjust the height of the plot
        )
        st.plotly_chart(fig, key=key)


    # Display the 3D plot with harvested trees
    merged_df_harvested = merged_df[merged_df['harvested'] == 0]
    mapshow_3d_with_line_harvested(merged_df_harvested, key='unique_chart3')

if col2.button('***Species-based*** Objective; Light regime'):
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

    import pandas as pd
    import plotly.graph_objects as go
    import plotly.express as px
    import streamlit as st

    # Assuming you have loaded the two datasets into pandas DataFrames
    trees_2019_df = pd.read_csv('Trees_2019.csv')
    hdiversity_df = pd.read_csv('Prescription stremlit/LSpices.csv')

    # Merge the two datasets based on the "TAG" column
    merged_df = pd.merge(trees_2019_df, hdiversity_df[['TAG']], how='left', on='TAG')

    # Create a new column "harvested" with 1 if the "TAG" is present in both datasets, else 0
    merged_df['harvested'] = merged_df['TAG'].apply(lambda x: 1 if x in hdiversity_df['TAG'].values else 0)

    # Save the resulting DataFrame to HarvestingTrees_2019.csv
    print(merged_df)
    merged_df.to_csv('HarvestingTrees_2019.csv', index=False)
    merged_df['SP_category'] = pd.Categorical(merged_df['Species'])
    merged_df['SP_code'] = merged_df['SP_category'].cat.codes
    merged_df = merged_df.drop(index=14)


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
            title='3D representation of Trees that should be harvested using Harvesting Plan in (black color)',
            width=800,  # Adjust the width of the plot
            height=800,  # Adjust the height of the plot
        )

        st.plotly_chart(fig, key=key)


    # Display the 3D plot with harvested trees
    mapshow_3d_with_line_harvested(merged_df, key='unique_chart3')


    # -------------------------------------------------------------------------------------remaining trees

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
            title='3D representation of remaining trees after harvesting',
            width=800,  # Adjust the width of the plot
            height=800,  # Adjust the height of the plot
        )
        st.plotly_chart(fig, key=key)


    # Display the 3D plot with harvested trees
    merged_df_harvested = merged_df[merged_df['harvested'] == 0]
    mapshow_3d_with_line_harvested(merged_df_harvested, key='unique_chart3')
########################################################################################################################


if col3.button('***Dominance*** Objective; Light regime'):
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

    import pandas as pd
    import plotly.graph_objects as go
    import plotly.express as px
    import streamlit as st

    # Assuming you have loaded the two datasets into pandas DataFrames
    trees_2019_df = pd.read_csv('Trees_2019.csv')
    hdiversity_df = pd.read_csv('Prescription stremlit/LDominance.csv')

    # Merge the two datasets based on the "TAG" column
    merged_df = pd.merge(trees_2019_df, hdiversity_df[['TAG']], how='left', on='TAG')

    # Create a new column "harvested" with 1 if the "TAG" is present in both datasets, else 0
    merged_df['harvested'] = merged_df['TAG'].apply(lambda x: 1 if x in hdiversity_df['TAG'].values else 0)

    # Save the resulting DataFrame to HarvestingTrees_2019.csv
    print(merged_df)
    merged_df.to_csv('HarvestingTrees_2019.csv', index=False)
    merged_df['SP_category'] = pd.Categorical(merged_df['Species'])
    merged_df['SP_code'] = merged_df['SP_category'].cat.codes
    merged_df2 = merged_df.drop(index=20)


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
            title='3D representation of Trees that should be harvested using Harvesting Plan in (black color)',
            width=800,  # Adjust the width of the plot
            height=800,  # Adjust the height of the plot
        )

        st.plotly_chart(fig, key=key)


    # Display the 3D plot with harvested trees
    mapshow_3d_with_line_harvested(merged_df2, key='unique_chart3')

if col4.button('***Economical*** Objective; Light regime'):
    st.write('No Data Available Yet!')


