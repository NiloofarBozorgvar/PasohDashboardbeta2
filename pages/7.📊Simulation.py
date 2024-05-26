import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    'Species': ['Oak', 'Pine', 'Maple', 'Birch', 'Spruce'],
    'D2019': [30, 25, 20, 18, 22]
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Harvest Simulation")

# Select the year (only 2021)
selected_year = st.selectbox("Select the Year", [2019])
selected_ml = st.selectbox("Select the Machine Learning Model", ['SVMOptimal' , 'SVMV1' ,'SVMV2' , 'GRUV1'])

# Select the number of trees to harvest using a slider
total_trees_2021 = df[f'D2019'].sum()
max_slider_value = min(total_trees_2021, 390)  # Ensure the max_value doesn't exceed the total number of trees
trees_to_harvest = st.slider("Number of Trees to Harvest", min_value=10, max_value=max_slider_value, value=total_trees_2021 // 2)

# Number input fields for DBH classes
dbh_classes = ['DBH Class 1', 'DBH Class 2', 'DBH Class 3', 'DBH Class 4', 'DBH Class 5']
dbh_inputs = []

initial_trees_per_class = trees_to_harvest // 5

for i, dbh_class in enumerate(dbh_classes):
    max_trees = min(trees_to_harvest, df[f'D{selected_year}'].iloc[i])
    trees_for_dbh_class = st.number_input(f"Number of Trees for {dbh_class}", min_value=0, max_value=max_slider_value, value=initial_trees_per_class)
    dbh_inputs.append(trees_for_dbh_class)

# Button to apply the simulation
if st.button("Apply Simulation"):
    # Update the dataset based on the selected year and harvested trees for each DBH class
    for i, dbh_class in enumerate(dbh_classes):
        df[f'D{selected_year}'].iloc[i] -= dbh_inputs[i]

    # Display the updated dataset

    col11, col12 = st.columns(2)
    col13, col14 = st.columns(2)

    with col11:


        # Read the CSV file
        #df = pd.read_csv('Prediction/DBHPrediction2055.csv')
        # Remove 385 rows randomly
        import requests
        import pandas as pd

        url = f'https://c971-34-106-174-225.ngrok-free.app/Predictionto2055{selected_ml}'

        # Replace 'localhost:8000' with your server's address

        # Make a POST request to the endpoint
        response = requests.post(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the JSON response
            data = response.json()
            # Fetch the predictions
            df = pd.DataFrame(data)
        else:
            print("Error:", response.status_code)

        #st.write(df)
        num_rows_to_remove = trees_to_harvest
        rows_to_remove = df.sample(num_rows_to_remove).index
        df = df.drop(rows_to_remove)
        # Extract relevant columns for the years D2021 to D2055
        years_columns = ['D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039',
                         'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']
        data_years = df[years_columns]

        # Calculate the average for each year
        average_per_year = data_years.mean()
        #st.write(average_per_year)
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
