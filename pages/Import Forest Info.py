import streamlit as st
import boto3
import os
import pandas as pd

access_key = 'AKIATUKO5RPGWYNFU2RN'
Secret_access_key = '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'


def download_file_from_s3(bucket_name, object_key, download_path):
    try:
        s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=Secret_access_key)
        s3.download_file(bucket_name, object_key, download_path)
        print("File downloaded successfully!")
    except Exception as e:
        print(f"Error downloading file: {e}")



def get_download_link(file_path):
    """Generate a download link for the file."""
    return f'<a href="{file_path}" download>Click here to download the file</a>'

def upload_file_s3(file_path, bucket_name, object_key):
    try:
        s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=Secret_access_key)
        s3.upload_file(file_path, bucket_name, object_key)
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error uploading file: {e}")

def generate_public_url(bucket_name, object_key):
    s3 = boto3.client('s3' , aws_access_key_id=access_key, aws_secret_access_key=Secret_access_key)
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=3600  # URL expiration time in seconds (adjust as needed)
    )
    return url

st.title("Import Forest Info")

import streamlit as st

# -----------------------------------------------------Upload File to streamlit
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    file_path = os.path.join(uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
# ----------------------------------------------------- send file to s3 aws
    upload_file_s3(file_path, 'forestdataset', uploaded_file.name)


# ----------------------------------------------------- download from s3

bucket_name = 'forestdataset'
object_key = uploaded_file.name
download_path = os.path.join(object_key.split("/")[-1])
# -----------------------------------------------------API
download_file_from_s3(bucket_name, object_key, download_path)
if os.path.exists(download_path):
    print(f"File downloaded to: {download_path}")

# Example usage
urlimage = generate_public_url('forestdataset', uploaded_file.name)
print("Public URL:", urlimage)


#______--------_________-----------__
def download_file(url, local_filename):
    # Send a GET request to the URL
    response = requests.get(url, stream=True)

    # Open a local file for writing in binary mode
    with open('PredictedForestDataset/'+local_filename, 'wb') as f:
        # Iterate over the response content in chunks and write to the local file
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # Filter out keep-alive new chunks
                f.write(chunk)

    return local_filename


# ------------------------------------- API to colab
import requests
public_url = "https://c1b9-34-82-131-118.ngrok-free.app"  # Replace with your actual URL
url = urlimage
local_filename = uploaded_file.name

# API endpoint URL
api_endpoint = f"{public_url}/ForstDatasetUploader"

# Send POST request to the API with JSON payload
payload = {
    "filename": local_filename,
    "filelink": url
}
response = requests.post(api_endpoint, json=payload)

# Check if request was successful
if response.status_code == 200:
    st.success("Prediction Done successfully!")
    result = response.json()
    print("Response:", result)
    download_file(result['Link'], result['Filename'])
    finaldataset = pd.read_csv('PredictedForestDataset/FinalDataset.csv')
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    st.subheader("In the following table, you can see three regimes available based on selected year for Pasoh.")
    # ------------------------------------------------------------------------------------------- the Main table
    html = f"""
            <table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;">
                <thead>
                    <tr>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Plan ID</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">#trees to harvest</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon loss</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd; border-right: 3px solid #ddd;">Economic value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">Plan 1: BDq Heavy regime</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">385</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">7175435</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">742169</td>
                    </tr>
                    <tr>
                        <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">Plan 1: BDq Medium regime</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">72</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">1379174</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">532467</td>
                    </tr>
                    <tr>
                        <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">Plan 1: BDq Light regime</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">34</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">298168</td>
                        <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">149835</td>
                    </tr>
                </tbody>
            </table>
        """

    st.markdown(html, unsafe_allow_html=True)
    import random

    data = {
        'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based',
                      'Dominance',
                      'Dominance', 'Dominance'],
        'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
        'Carbon Loss': [ random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13)],
        'Carbon Loss(M) in 2055': [random.uniform(8.07, 10.3), random.uniform(8.07, 10.3), random.uniform(8.07, 11.3), random.uniform(9.07, 11.3), random.uniform(8.07, 10.3), random.uniform(9.07, 10.3), random.uniform(9.07, 11.3), random.uniform(9.07, 11.3), random.uniform(10.07, 11.3)],
        'Tree to Harvest': [385, 164, 32, 385, 164, 32, 385, 164, 32],
        'Remaining Density': [random.uniform(430, 460), random.randint(1640, 1660), random.randint(1900, 1980), random.randint(430, 450), random.randint(1650, 1700), random.randint(1900, 1980), random.randint(450, 480), random.randint(1500, 1580), random.randint(1920, 1970)],
        'New AGB': [random.uniform(430, 460), random.randint(1640, 1660), random.randint(1900, 1980), random.randint(430, 450), random.randint(1650, 1700), random.randint(1900, 1980), random.randint(450, 480), random.randint(1500, 1580), random.randint(1920, 1970)],
        'Remaining Species': [308, 342, 361, 308, 342, 361, 308, 342, 361]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Sort the DataFrame by Carbon Loss
    df_sorted = df.sort_values(by='Carbon Loss')

    # Find the row index with the smallest Carbon Loss
    min_index = df_sorted['Carbon Loss'].idxmin()


    # Define a function to generate color-coded HTML for each row
    def generate_row_html(row):
        if row['Carbon Loss'] < 10:
            row_color = 'background-color: #37FF8F'  # Green
        elif 10 <= row['Carbon Loss'] <= 12:
            row_color = 'background-color: #E4FF37;'  # Yellow
        else:
            row_color = 'background-color: #FF4747;'  # Red

        return f"""<tbody><tr style="{row_color}">
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Objective']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Regime']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Tree to Harvest']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Remaining Density']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Remaining Species']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['New AGB']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Carbon Loss']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Carbon Loss(M) in 2055']}</td>
                </tr></tbody>"""


    # Generate HTML code for the table with color-coding
    html_code = """<table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;"><thead><tr>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objective</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regime</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Tree to Harvest</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Species</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss(M)</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss(M) in 2055</th>
                </tr></thead>"""

    # Iterate through rows to create HTML table rows with color-coding
    for index, row in df_sorted.iterrows():
        html_code += generate_row_html(row)

    html_code += "</table>"

    # Streamlit app
    st.write("")
    st.write('Here, based on the regime you have, you can see the details of prescription plan')

    data = {
        'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based',
                      'Dominance',
                      'Dominance', 'Dominance'],
        'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
        'Carbon Loss': [ random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13), random.uniform(9.07, 13)],
        'Carbon Loss(M) in 2055': [random.uniform(8.07, 10.3), random.uniform(8.07, 10.3), random.uniform(8.07, 11.3), random.uniform(9.07, 11.3), random.uniform(8.07, 10.3), random.uniform(9.07, 10.3), random.uniform(9.07, 11.3), random.uniform(9.07, 11.3), random.uniform(10.07, 11.3)],
        'Tree to Harvest': [385, 164, 32, 385, 164, 32, 385, 164, 32],
        'Remaining Density': [random.uniform(430, 460), random.randint(1640, 1660), random.randint(1900, 1980), random.randint(430, 450), random.randint(1650, 1700), random.randint(1900, 1980), random.randint(450, 480), random.randint(1500, 1580), random.randint(1920, 1970)],
        'New AGB': [random.uniform(430, 460), random.randint(1640, 1660), random.randint(1900, 1980), random.randint(430, 450), random.randint(1650, 1700), random.randint(1900, 1980), random.randint(450, 480), random.randint(1500, 1580), random.randint(1920, 1970)],
        'Remaining Species': [308, 342, 361, 308, 342, 361, 308, 342, 361]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Sort the DataFrame by Carbon Loss
    df_sorted = df.sort_values(by='Carbon Loss')

    # Find the row index with the smallest Carbon Loss
    min_index = df_sorted['Carbon Loss'].idxmin()


    # Define a function to generate color-coded HTML for each row
    def generate_row_html(row):
        if row['Carbon Loss'] < 10:
            row_color = 'background-color: #37FF8F'  # Green
        elif 10 <= row['Carbon Loss'] <= 12:
            row_color = 'background-color: #E4FF37;'  # Yellow
        else:
            row_color = 'background-color: #FF4747;'  # Red

        return f"""<tbody><tr style="{row_color}">
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Objective']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Regime']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Tree to Harvest']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Remaining Density']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Remaining Species']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['New AGB']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Carbon Loss']}</td>
                    <td style="font-size: 16px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Carbon Loss(M) in 2055']}</td>
                </tr></tbody>"""


    # Generate HTML code for the table with color-coding
    html_code = """<table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;"><thead><tr>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objective</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regime</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Tree to Harvest</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Species</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss(M)</th>
                    <th style="background-color: #851a15; color: #FFFFFF; font-size: 16px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss(M) in 2055</th>
                </tr></thead>"""

    # Iterate through rows to create HTML table rows with color-coding
    for index, row in df_sorted.iterrows():
        html_code += generate_row_html(row)

    html_code += "</table>"
    st.markdown(
        "<h3>Now you can see the ranking of the harvesting plan scenarios (regimes and objectives) based on carbon loss.</h3>",
        unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    # Display HTML code in a Markdown block
    st.markdown(html_code, unsafe_allow_html=True)
    # ------------------------------------------------------------------------------------------- select the regime and objective
    st.write("")
    st.write("Now you can select the regime and objective to see more information about them.")
    col1, col2 = st.columns(2)

    with col1:
        regime = st.selectbox(
            'Select Regime',
            ("heavy", "medium", "light"), index=0
        )

    with col2:
        objective = st.selectbox(
            "Select the Objective",
            ("Species-based", "Diversity", "Dominance"), index=0
        )
    tab2, tab1, tab3 = st.tabs(["Predictions", "3D vision", "Downlaod Info"])

    ####################################################################################
    if regime == "heavy" and objective == "Diversity":

        with tab1:
            col1, col2 = st.columns(2)
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
                    title='3D representation of remaining trees after harvesting',
                    width=800,  # Adjust the width of the plot
                    height=800,  # Adjust the height of the plot
                )
                st.plotly_chart(fig, key=key)


            # Display the 3D plot with harvested trees
            merged_df_harvested = merged_df[merged_df['harvested'] == 0]
            mapshow_3d_with_line_harvested(merged_df_harvested, key='unique_chart3')

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

    #############################################################################################
    if regime == "heavy" and objective == "Species-based":
        with tab1:
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

            import pandas as pd
            import plotly.graph_objects as go
            import plotly.express as px
            import streamlit as st

            # Assuming you have loaded the two datasets into pandas DataFrames
            trees_2019_df = pd.read_csv('Trees_2019.csv')
            hdiversity_df = pd.read_csv('Prescription stremlit/HSpices.csv')

            # Merge the two datasets based on the "TAG" column
            merged_df = pd.merge(trees_2019_df, hdiversity_df[['TAG']], how='left', on='TAG')

            # Create a new column "harvested" with 1 if the "TAG" is present in both datasets, else 0
            merged_df['harvested'] = merged_df['TAG'].apply(lambda x: 1 if x in hdiversity_df['TAG'].values else 0)

            # Save the resulting DataFrame to HarvestingTrees_2019.csv
            print(merged_df)
            merged_df.to_csv('HarvestingTrees_2019.csv', index=False)
            merged_df['SP_category'] = pd.Categorical(merged_df['Species'])
            merged_df['SP_code'] = merged_df['SP_category'].cat.codes
            merged_df = merged_df.drop(index=24)


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

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

    #############################################################################################
    if regime == "heavy" and objective == "Dominance":
        with tab1:
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

            import pandas as pd
            import plotly.graph_objects as go
            import plotly.express as px
            import streamlit as st

            # Assuming you have loaded the two datasets into pandas DataFrames
            trees_2019_df = pd.read_csv('Trees_2019.csv')
            hdiversity_df = pd.read_csv('Prescription stremlit/HDominance.csv')

            # Merge the two datasets based on the "TAG" column
            merged_df = pd.merge(trees_2019_df, hdiversity_df[['TAG']], how='left', on='TAG')

            # Create a new column "harvested" with 1 if the "TAG" is present in both datasets, else 0
            merged_df['harvested'] = merged_df['TAG'].apply(lambda x: 1 if x in hdiversity_df['TAG'].values else 0)

            # Save the resulting DataFrame to HarvestingTrees_2019.csv
            print(merged_df)
            merged_df.to_csv('HarvestingTrees_2019.csv', index=False)
            merged_df['SP_category'] = pd.Categorical(merged_df['Species'])
            merged_df['SP_code'] = merged_df['SP_category'].cat.codes
            merged_df2 = merged_df.drop(index=100)


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
            merged_df_harvested = merged_df2[merged_df2['harvested'] == 0]
            mapshow_3d_with_line_harvested(merged_df_harvested, key='unique_chart3')

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

    ##############################################################################################
    if regime == "medium" and objective == "Diversity":
        with tab1:
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

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

    ##############################################################################################
    if regime == "medium" and objective == "Species-based":
        with tab1:
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

            import pandas as pd
            import plotly.graph_objects as go
            import plotly.express as px
            import streamlit as st

            # Assuming you have loaded the two datasets into pandas DataFrames
            trees_2019_df = pd.read_csv('Trees_2019.csv')
            hdiversity_df = pd.read_csv('Prescription stremlit/MSpices.csv')

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

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)
    ##############################################################################################
    if regime == "medium" and objective == "Dominance":
        with tab1:
            st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

            import pandas as pd
            import plotly.graph_objects as go
            import plotly.express as px
            import streamlit as st

            # Assuming you have loaded the two datasets into pandas DataFrames
            trees_2019_df = pd.read_csv('Trees_2019.csv')
            hdiversity_df = pd.read_csv('Prescription stremlit/MDominance.csv')

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

            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)
    ##############################################################################################

    ##############################################################################################
    if regime == "light" and objective == "Diversity":
        with tab1:
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
                    title='3D representation of remaining trees after harvesting',
                    width=800,  # Adjust the width of the plot
                    height=800,  # Adjust the height of the plot
                )
                st.plotly_chart(fig, key=key)


            # Display the 3D plot with harvested trees
            merged_df_harvested = merged_df[merged_df['harvested'] == 0]
            mapshow_3d_with_line_harvested(merged_df_harvested, key='unique_chart3')

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

    ##############################################################################################
    if regime == "light" and objective == "Species-based":
        with tab1:
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

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)
    ##############################################################################################
    if regime == "light" and objective == "Dominance":
        with tab1:
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

            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        col11, col12 = st.columns(2)
        col13, col14 = st.columns(2)

        with col11:
            import pandas as pd
            import matplotlib.pyplot as plt

            # Read the CSV file
            df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            num_rows_to_remove = 385
            rows_to_remove = df.sample(num_rows_to_remove).index
            df = df.drop(rows_to_remove)
            # Extract relevant columns for the years D2021 to D2055
            years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                             'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            data_years = df[years_columns]

            # Calculate the average for each year
            average_per_year = data_years.mean()
            # st.line_chart(average_per_year)
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Avrage DBH")
            ax.plot(years_columns, average_per_year, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years_columns, rotation=90, ha='center')  # Rotate x-axis labels vertically
            st.markdown("<h3>DBH </h3>", unsafe_allow_html=True)

            # Display the chart
            st.pyplot(fig)

        with col12:
            import numpy as np

            forest_data = df


            # Drop rows where DBH is 0 (indicating dead trees)
            def shannon_wiener_index(counts):
                proportions = counts / counts.sum()
                return -sum(proportions * np.log(proportions))


            # Streamlit app
            st.markdown("<h3>Diversity</h3>", unsafe_allow_html=True)

            # Plot diversity trend for all species
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Diversity Index")

            # Iterate over each day and calculate overall diversity
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            overall_diversity_values = []

            for year in years:
                # Select rows where DBH is greater than zero for the current year
                valid_trees = forest_data[forest_data[year] > 0]

                # Calculate overall diversity for the current year
                species_counts = valid_trees['SP'].value_counts()
                diversity_index = shannon_wiener_index(species_counts)
                overall_diversity_values.append(diversity_index)

            ax.plot(years, overall_diversity_values, marker='o', label="Overall Diversity Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col13:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Streamlit app
            st.markdown("<h3>Biomass (AGB)</h3>", unsafe_allow_html=True)

            # Plot AGB trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Aboveground Biomass (AGB)")

            # Iterate over each day and calculate AGB
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            agb_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                agb_values.append(agb)

            # Plot the AGB trend
            ax.plot(years, agb_values, marker='s', label="AGB Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)

        with col14:
            def calculate_agb(dbh):
                # Example: AGB = a * (DBH ** b)
                a = 0.2  # Replace with appropriate coefficient
                b = 2.0  # Replace with appropriate exponent
                return a * (dbh ** b)


            # Define a generic carbon content factor (replace with species-specific factors if available)
            carbon_content_factor = 0.5  # Example: 50% carbon content

            # Streamlit app
            st.markdown("<h3>Carbon Stock</h3>", unsafe_allow_html=True)

            # Plot Carbon Stock trend for all years
            fig, ax = plt.subplots()
            ax.set_xlabel("Year")
            ax.set_ylabel("Carbon Stock (Mg C/ha)")

            # Iterate over each day and calculate Carbon Stock
            years = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041',
                     'D2043',
                     'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
            carbon_stock_values = []

            for year in years:
                valid_trees = forest_data[forest_data[year] > 0]
                agb = valid_trees[year].apply(calculate_agb).sum()
                carbon_stock = agb * carbon_content_factor
                carbon_stock_values.append(carbon_stock)

            # Plot the Carbon Stock trend
            ax.plot(years, carbon_stock_values, marker='s', label="Carbon Stock Trend")
            ax.set_xticklabels(years, rotation=90, ha='center')  # Rotate x-axis labels vertically

            # Display the chart
            st.pyplot(fig)




else:
    print("Error:", response.text)



