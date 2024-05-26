import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------------------------------------------------------Text Box
def display_design_element():
    st.subheader("🔍📝Insight and Prediction:")

    text = (
        " In the following you can see the predicted information on Pasoh Forest trees 🎯. "
    )
    font_size = 17
    font_color = "#333333"
    border_color = "#8D6A9F"
    background_color = "wight"
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
#-------------------------------------------------------------------------------bar chart function 2019
def clustering2019(x_axis_ranges , df):
    df_ranges = pd.DataFrame(index=x_axis_ranges)
    for column in df.columns:
        col_values = []
        for x_range in x_axis_ranges:
            if '-' in x_range:
                start, end = map(int, x_range.split('-'))
                filtered_values = df[column][(df[column] >= start) & (df[column] <= end)]
            else:
                filtered_values = df[column][df[column] == int(x_range)]
            col_values.append(filtered_values.count())
        df_ranges[column] = col_values

    fig = px.bar(df_ranges, x=['1-5', '6-11', '12-17', '18-23', '24<'], y=df_ranges.columns, barmode='group',
                 color_discrete_sequence=px.colors.qualitative.Dark24)

    # Updating the layout
    fig.update_layout(
        title=dict(text='Actual and Predicted Number of Trees (In each DBH Classes) 2019', x=0.10,
                   font=dict(color='dark green')),

        xaxis_title=dict(text='DBH Class', font=dict(color='purple')),
        yaxis_title=dict(text='Number of Trees', font=dict(color='purple')),
        xaxis=dict(tickangle=45)

    )
    # Displaying the chart using Streamlit
    st.plotly_chart(fig)

#-----------------------------------------------------------------------------------------------bar chart function 2021
def clustering2021(x_axis_ranges , df):
    df_ranges = pd.DataFrame(index=x_axis_ranges)
    for column in df.columns:
        col_values = []
        for x_range in x_axis_ranges:
            if '-' in x_range:
                start, end = map(int, x_range.split('-'))
                filtered_values = df[column][(df[column] >= start) & (df[column] <= end)]
            else:
                filtered_values = df[column][df[column] == int(x_range)]
            col_values.append(filtered_values.count())
        df_ranges[column] = col_values

    custom_colors = ['orange', 'blue', 'orange', 'blue', 'orange']  # Add more colors as needed

    fig = px.bar(df_ranges, x=['1-5', '6-11', '12-17', '18-23', '24<'], y=df_ranges.columns, barmode='group',
                 color_discrete_sequence=custom_colors * 2)

    # Updating the layout
    fig.update_layout(
        title=dict(text='Actual and Predicted Number of Trees (In each DBH Classes) 2021', x=0.10,
                   font=dict(color='dark green')),

        xaxis_title=dict(text='DBH Class', font=dict(color='Blue')),
        yaxis_title=dict(text='Number of Trees', font=dict(color='Blue')),
        xaxis=dict(tickangle=45)
    )

    # Displaying the chart using Streamlit
    st.plotly_chart(fig)
#----------------------------------------------------------------------------------Option Bar
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

option = st.selectbox(
        "Information of forest trees in year:",
        ("2019", "2021"),
    )
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------Call Bar Chart 2019
if option =='2019':
    df = pd.read_csv('DBH2019.csv')
    df = df[['Predicted DBH for 2019' , 'Actual DBH for 2019']]
    # Define the ranges for x-axis
    #st.write(df)
    # ----------------Call the clustering function with your specified ranges and DataFrame
    x_axis_ranges = ['1-14', '15-29', '30-44', '45-58', '59-200']
    result = clustering2019(x_axis_ranges, df)  # 'df' is my DataFrame
    print(result)


#---------------------------------------------------------------------------------------------Bar chart 2021
if option =='2021':
    df = pd.read_csv('DBH2021.csv')
    df = df[['Predicted DBH for 2021' , 'Actual DBH for 2021']]
    # ----------------Call the clustering function with your specified ranges and DataFrame
    x_axis_ranges = ['1-14', '15-29', '30-44', '45-58', '59-200']
    result = clustering2021(x_axis_ranges, df)  # 'df' is my DataFrame
    print(result)


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& Prediction

import matplotlib.pyplot as plt

st.header('Predicted DBH trend for next 30 years for species (form 2021 to 2051)')
st.subheader('DBH')
df = pd.read_csv('Prediction/DBHPrediction2055.csv')

selected_sp_name = st.selectbox("Select Spices to see the trend of DBH:", df['SP_Name'].unique())
filtered_df = df[df['SP_Name'] == selected_sp_name]

mean_values = filtered_df.loc[:, 'D2021':'D2055'].mean()

# Extract the year part from the column names
years = [col[1:] for col in mean_values.index]

# Create a DataFrame for plotting
plot_data = pd.DataFrame({'Year': years, 'Average DBH': mean_values})

# Plot the trend using Plotly Express
fig = px.line(plot_data, x='Year', y='Average DBH', title=f'Trend for {selected_sp_name}')

# Display the plot
st.plotly_chart(fig)
#-----------------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming df is your DataFrame
# Replace this line with your actual DataFrame loading logic
# df = pd.read_csv('your_dataset.csv')

# Create lists to store overall trends
ascending_trend_all = []
descending_trend_all = []

# Iterate over unique SP_Names
for selected_sp_name in df['SP_Name'].unique():
    # Filter the DataFrame based on the selected SP_Name
    filtered_df = df[df['SP_Name'] == selected_sp_name]

    # Extract the year part from the column names
    years = [col[1:] for col in filtered_df.loc[:, 'D2021':'D2055'].columns]

    # Create two lists to store the trend information
    ascending_trend = []
    descending_trend = []

    # Check if changes are ascending or descending for each year
    for year in years:
        changes = filtered_df[f'D{year}'].diff().dropna()
        if all(changes >= 0):
            ascending_trend.append(year)
        elif all(changes <= 0):
            descending_trend.append(year)

    # Append the trends for the current SP_Name to the overall lists
    if ascending_trend:
        ascending_trend_all.append((selected_sp_name, ascending_trend))
    if descending_trend:
        descending_trend_all.append((selected_sp_name, descending_trend))

# Calculate the percentages
total_sp_names = df['SP_Name'].nunique()
percentage_ascending = (len(ascending_trend_all) / total_sp_names) * 100
percentage_descending = (len(descending_trend_all) / total_sp_names) * 100

# Create a pie chart using Plotly Express with custom colors
fig = px.pie(
    names=['Ascending', 'Descending'],
    values=[percentage_ascending, percentage_descending],
    title='Percentage of Species with Ascending and Descending DBH Trends in next 30 years',
    color_discrete_map={'Ascending': 'green', 'Descending': 'red'}
)

# Display the pie chart
st.plotly_chart(fig)

#--------------------------------------------------------------------------------------------------------------------------

st.subheader('⭕ Species at risk of extinction')
import pandas as pd
import streamlit as st

df = pd.read_csv('Prediction/DBHPrediction2055.csv')
result = df.groupby('SP_Name').mean()

zero_values_df = df[(df.loc[:, 'D2021':'D2055'] == 0).all(axis=1)]

# Display the resulting DataFrame
#st.write(zero_values_df[['SP_Name', 'D2021', 'D2023', 'D2025', 'D2027', 'D2029', 'D2031', 'D2033', 'D2035', 'D2037', 'D2039', 'D2041', 'D2043', 'D2045', 'D2047', 'D2049', 'D2051', 'D2053', 'D2055']].T)
#st.write(zero_values_df['SP_Name'])
#-------------------------------------------------------------------------------------------------------
def display_design_element():
    st.subheader("📣Species name list")

    text = (
        'ACROPO, ALANRI, ANI1LA, ARDICO, ARTORI, BACCPY, BARRPE, BLUMTO, BOUEMA, BOUEOP, BUCHAR, '
        'BUCHSE,CALODI, CALOTE, CANALL, CANTDI, CLE1SU, CROTAR, CYATRA, CYNOMA, DACRR1, DIOSBU, DIPTC1, '
        'DRYPLO, ELAEFE, ELAENI, ELAERU, EUGEDE, EUGEGR, EUGENA, EUGESP, GARCNI, GIROPA, HOPEME, HOPEME '
        'IXONIC, LANSDO, LEPISE, LITHCO, LITHCU, LITHWA, MACALO, MALLPE, MEL1FU, MESUFE, MESURA, MONOMA '
        'NEOBHE, OCHAAM, PALAMA, PAR1OB, PARKSP, PAYELU, PEN1MO, PERKSP, POL1SC, RYPAAC, RYPAKU, SANTTO'
        'SANTTO, SARADE, SHORL1, SHORL2, SHORM1, SHORP1, SHORP2, VATIBE, XANTEU, XANTRU, XANTST, XYLOFS, '
        'XYLOM1'
    )
    font_size = 18
    font_color = "#333333"
    border_color = "green"
    background_color = "wight"
    border_width = 2

    styled_text = f"""
        <div style="padding: 10px; border: {border_width}px solid {border_color};
                    border-radius: 5px; background-color: {background_color};">
            <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
        </div>
    """

    st.markdown(styled_text, unsafe_allow_html=True)

display_design_element()
#--------------------------------------------------------------------
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

st.subheader("📣 You can see the trend of DBH based on each DBH class size in next 30 years")

import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('Prediction/DBHPrediction2055.csv')

def cm_to_inches(cm):
    return cm * 0.393701

# Columns to process
columns_to_process = df.columns[2:-1]  # Exclude the first two columns and the last column

# Create a new DataFrame to store the clustered values
clustered_df = df.copy()

# Initialize a dictionary to store cluster counts for each column
cluster_counts_dict = {}

# Iterate over columns and apply clustering
for col in columns_to_process:
    # Convert values from cm to inches
    clustered_df[col] = df[col].apply(cm_to_inches)

    # Apply clustering based on specified ranges
    clustered_df[col] = pd.cut(clustered_df[col], bins=[1, 5, 11, 17, 23, float('inf')], labels=['1-5', '6-11', '12-17', '18-23', '>24'])

    # Count the occurrences of each cluster for the current column
    cluster_counts_dict[col] = clustered_df[col].value_counts()

# Convert the dictionary to a DataFrame
cluster_counts_df = pd.DataFrame(cluster_counts_dict).T  # Transpose the DataFrame

# Create a select box for cluster selection
selected_cluster = st.selectbox("Select each DBH class size that you want to see the trend", cluster_counts_df.columns)

# Create a line chart to visualize cluster counts for the selected cluster
fig = px.line(x=cluster_counts_df.index, y=cluster_counts_df[selected_cluster],
              labels={'index': 'Cluster', 'value': 'Count'},
              title=f'Cluster Counts for {selected_cluster} from D2021 to D2055',
              width=700, height=500)

# Display the line chart
st.plotly_chart(fig)




# ----------------------------------------------------------------------------------------------------Text Box


def display_design_element():
    st.subheader("📣📣 As an appropriate growth, at least a 1cm increase in DBH every year is expected in each tree. "
                 "In the following, you can see the name of Species with expected growth.")

    text = (
        " 1:SHORL1, 2:NEPHCO, 3:EUGERI, 4:SARADE, 5:SHORM1, 6:MACACO, 7:SHORAC, "
        "8:XANTEU, 9:XANTST, 10:RYPAKU, 11:EUGEP4, 12:DIPTC1, 13:CASTME, 14:ARTORI, "
        "15:SHORL2, 16:SHORP2, 17:SAR1GR, 18:BRACHO, 19:SANTTO, 20:MESUFE, 21:XYLOFS, "
        "22:CLE1SU, 23:CYNOMA, 24:PTYCCO, 25:ARCHBU, 26:CALODI, 27:ARCHCL, 28:DIOSBU, "
        "29:DIALPL, 30:ELAERU, 31:BOUEOP, 32:MONOMA, 33:CANTDI, 34:SINDWA, 35:MACALO, "
        "36:ELAEFL, 37:STYRBE, 38:SHORP1, 39:SANTLA, 40:POL1JE, 41:LITHCU, 42:EUGEFL. "
    )
    font_size = 18
    font_color = "#333333"
    border_color = "green"
    background_color = "wight"
    border_width = 2

    styled_text = f"""
        <div style="padding: 10px; border: {border_width}px solid {border_color};
                    border-radius: 5px; background-color: {background_color};">
            <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
        </div>
    """

    st.markdown(styled_text, unsafe_allow_html=True)

display_design_element()
#-------------------------------------------------------------------------------------------------Good Growth
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd

# Load your dataset
# Replace 'your_data.csv' with your actual data file path
df = pd.read_csv('All1521.csv')

# Filter for DBH values in years 2019 and 2021
filtered_df = df[(df['Year'] == 2019) | (df['Year'] == 2021)]

# Remove trees with 0 DBH in both 2019 and 2021
zero_dbh_trees = filtered_df.pivot_table(index='TAG', columns='Year', values='DBH', aggfunc='max')
zero_dbh_trees = zero_dbh_trees[(zero_dbh_trees[2019] != 0) | (zero_dbh_trees[2021] != 0)].index
filtered_df = df[df['TAG'].isin(zero_dbh_trees)]

# Check for at least 2cm growth in DBH for remaining trees
remaining_trees = filtered_df['TAG'].unique()
trees_with_growth = []

for tag in remaining_trees:
    dbh_2019 = filtered_df[(filtered_df['TAG'] == tag) & (filtered_df['Year'] == 2019)]['DBH'].values[0]
    dbh_2021 = filtered_df[(filtered_df['TAG'] == tag) & (filtered_df['Year'] == 2021)]['DBH'].values[0]
    species_name = filtered_df[(filtered_df['TAG'] == tag)]['Species'].values[0]
    xco = filtered_df[(filtered_df['TAG'] == tag) & (filtered_df['Year'] == 2021)]['XCO'].values[0]
    yco = filtered_df[(filtered_df['TAG'] == tag) & (filtered_df['Year'] == 2021)]['YCO'].values[0]

    if dbh_2021 - dbh_2019 >= 2:
        trees_with_growth.append({'TAG': tag, 'Species': species_name, 'XCO': xco, 'YCO': yco})

# Display names of species with trees that have at least 2cm growth in DBH
st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
st.subheader('If you want, you can see the details of each species 🔍')

selected_species = st.selectbox('Select Species', sorted(list(set([tree['Species'] for tree in trees_with_growth]))))

if selected_species:
    st.write(f"Species: {selected_species}")

    species_trees = [tree for tree in trees_with_growth if tree['Species'] == selected_species]

    if st.button('Click here to see the Details!'):
        if species_trees:
            st.write("Details of trees with good growth:")
            growth_df = pd.DataFrame(species_trees)
            st.table(growth_df[['TAG', 'XCO', 'YCO']])
        else:
            st.write("No trees met the criteria for this species.")
else:
    st.write("Please select a species.")

#----------------------------------------------------------------------------------------------------Growth zone bar chart
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

st.subheader('⚔️ Competition occurs among trees:')



import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load your dataset (replace 'YourDataset.csv' with your actual file path)
data = pd.read_csv('All1521.csv')

# Selected years
selected_years = [2015, 2017, 2019, 2021]

# Step 1: Remove rows where DBH is zero for the selected years
non_zero_rows = data[(data[['DBH']] != 0).any(axis=1)]

# Step 2: Convert 'RDen' to numeric and handle non-numeric values
non_zero_rows['RDen'] = pd.to_numeric(non_zero_rows['RDen'], errors='coerce')
# Step 3: Divide the value in 'RDen' by 10
non_zero_rows['RDen'] = non_zero_rows['RDen'] / 10

# Step 4: Categorize the trees into 5 categories
bins = [-1, 15, 35, 55, 75, float('inf')]
labels = ['Open Growth', 'Enthusiastic Growth', 'Goldilocks', 'Danger', 'No Return']
non_zero_rows['Growth Zone'] = pd.cut(non_zero_rows['RDen'], bins=bins, labels=labels)

# Display the table
 #st.write(non_zero_rows[['TAG', 'DBH', 'XCO', 'YCO', 'RDen', 'Growth Zone']])

# Display the bar chart
plt.figure(figsize=(10, 6))
growth_zone_counts = non_zero_rows['Growth Zone'].value_counts().sort_index()
plt.bar(growth_zone_counts.index, growth_zone_counts.values, color='skyblue')
plt.xlabel('Growth Zone')
plt.ylabel('Number of Trees')
plt.title('Distribution of Trees in Different Growth Zones (Year 2019)')
st.pyplot(plt)

#--------------------------------------------------------------------------------------------------Zone explanation button
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

import streamlit as st

def display_design_element2(title, text, font_color, border_color):
    font_size = 16
    background_color = "white"
    border_width = 2

    styled_text = f"""
        <div style="padding: 10px; border: {border_width}px solid {border_color};
                    border-radius: 5px; background-color: {background_color};">
            <p style="font-size: {font_size}px; color: {font_color}; font-weight: bold;">{title}</p>
            <p style="font-size: {font_size}px; color: #333333;">{text}</p>
        </div>
    """

    st.markdown(styled_text, unsafe_allow_html=True)
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
    width:500px;
}

div.stButton > button:hover {
    background-color: #bba6dd;
    color:#1e2136;
    border: #1e2136;
    }
</style>""", unsafe_allow_html=True)

# Create a button with a unique key
button_clicked = st.button("If you want to know the explanation of the growth zones, Click here!", key="unique_button_key" )

# Display text blocks only when the button is clicked
if button_clicked:
    display_design_element2(
        "OPEN (EXUBERANT) GROWTH ZONE (RD 0–15):",
        "Although seedlings or young trees may compete with leafy or woody vegetation during the establishment stage, they are not yet competing with each other and should have lots of room to grow.",
        "green",
        "green"
    )

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    display_design_element2(
        "ENTHUSIASTIC GROWTH ZONE (RD 15-35):",
        "Usually seen in young stands following crown closure when trees still have plenty of room and resources (water, nutrients, and light) but are beginning to compete with each other and with any other woody plants in the stand.",
        "#659962",
        "#659962"
    )

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    display_design_element2(
        "THE GOLDILOCKS ZONE (RD 35–55):",
        "Traditionally thought of as the “optimum growth zone” by foresters, we call this the Goldilocks Zone because it is seen as “just right”: not too open, not too crowded. It is a zone of robust growth and the zone in which many managers often try to maintain stands for decades with repeated thinning.",
        "#f6bd6f",
        "#f6bd6f"
    )

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    display_design_element2(
        "DANGER ZONE (RD 55–75):",
        "Trees compete intensely for resources. We see rapid and continued crown lift and wider differentiation into crown classes. Some trees fail to get the resources needed. Weaker trees die, freeing up resources that allow surviving trees to grow.",
        "#ea6d30",
        "#ea6d30"
    )

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    display_design_element2(
        "ZONE OF NO RETURN (RD>75):",
        "This zone is characterized by many small, skinny, and stressed trees. Even the dominant trees may have small, weak crowns. For many stands arriving at this point, it is too late to thin. Once a stand reaches this stage, the best option is often to leave it alone until the time arrives for a regeneration harvest to start a new stand.",
        "#c31736",
        "#c31736"
    )






#------------------------------------------------------------------------------------------- Zone Table
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

# Load your dataset (replace 'YourDataset.csv' with your actual file path)
data = pd.read_csv('All1521.csv')

# Selected years
selected_years = [2015, 2017, 2019, 2021]

# Step 1: Remove rows where DBH is zero for the selected years
non_zero_rows = data[(data[['DBH']] != 0).any(axis=1)]

# Step 2: Convert 'RDen' to numeric and handle non-numeric values
non_zero_rows['RDen'] = pd.to_numeric(non_zero_rows['RDen'], errors='coerce')

# Step 3: Divide 'RDen' values by 10
non_zero_rows['RDen'] = non_zero_rows['RDen'] / 10

# Step 4: Fill missing values with a default value (e.g., -1)
# Step 4: Fill missing values with the mean of 'RDen'
non_zero_rows['RDen'].fillna(non_zero_rows['RDen'].mean(), inplace=True)

# Step 5: Categorize the trees based on 'RDen' values for the year 2019
non_zero_rows['Category'] = pd.cut(non_zero_rows[non_zero_rows['Year'] == 2019]['RDen'],
                                   bins=[0, 15, 35, 55, 75, float('inf')],
                                   labels=['Open Growth Zone', 'Enthusiastic Growth Zone', 'Goldilocks Zone',
                                           'Danger Zone', 'Zone of No Return'],
                                   include_lowest=True)

# Get unique growth zones excluding NaN
growth_zones = non_zero_rows['Category'].dropna().unique()

# Selectbox to choose the growth zone
selected_zone = st.selectbox('Select Growth Zone:', growth_zones, index=None)

# Check if the selected growth zone has NaN values
if non_zero_rows[non_zero_rows['Category'] == selected_zone].empty:
    st.write()
else:
    # Display the selected growth zone table
    st.subheader(f'Table for {selected_zone}')
    columns_to_display = ['Species', 'QUAD', 'Age', 'Basal Area', 'DBH', 'XCO', 'YCO']
    zone_table = non_zero_rows[non_zero_rows['Category'] == selected_zone][columns_to_display]
    st.write(zone_table)

    # Scatter plot for tree locations with Altair
    st.subheader(f'Location of trees in the {selected_zone}')
    zone_scatter = non_zero_rows[non_zero_rows['Category'] == selected_zone]

    # Use Altair for interactive scatter plot
    chart = alt.Chart(zone_scatter).mark_circle().encode(
        x='XCO:Q',
        y='YCO:Q',
        color='Species:N',
        tooltip=['Species', 'XCO', 'YCO']
    ).properties(
        width=700,
        height=500
    )

    st.altair_chart(chart)

#------------------------------------------------------------------------Slide bar for growth rate


st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

st.subheader("Select the desire growth rate range to see the trees!")
import streamlit as st
import pandas as pd

# Load the dataset
#@st.cache
def load_data():
    data = pd.read_csv('All1521.csv')
    return data

data = load_data()

# Filter the data for the year 2021
data_2021 = data[data['Year'] == 2021]

# Filter the data based on the Growth rate slider
growth_rate_range = st.slider('Select Growth Rate Range', float(data_2021['Growth rate'].min()), float(data_2021['Growth rate'].max()), (float(data_2021['Growth rate'].min()), float(data_2021['Growth rate'].max())))

filtered_data = data_2021[(data_2021['Growth rate'] >= growth_rate_range[0]) & (data_2021['Growth rate'] <= growth_rate_range[1])]

# Display the filtered data
st.write(filtered_data)
