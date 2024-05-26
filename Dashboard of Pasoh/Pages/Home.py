import streamlit as st
import pandas as pd
import plotly.express as px

#-----------------------------------------------------------------------------------------------bar chart function 2019
import pandas as pd
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

    # Create a bar chart using Plotly

    # Using Plotly Express to create a grouped bar chart with custom colors
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
#------------------------------------------------------------------------------------------------------Add Space
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)


#------------------------------------------------------------------------------------------------Scatter function
import plotly.express as px
def mapshow2019(df):
    df['SP'] = df['SP'].astype('category')  # Convert 'SP' column to categorical

    fig = px.scatter(df, x='XCO', y='YCO', color='SP')

    # Update title attributes
    fig.update_layout(
        title=dict(text='Actual Location of Trees', x=0.3, y=0.9,  # Adjust x and y to change title position
                   font=dict(color='dark green', size=20, family='Arial')),  # Change title font attributes
        xaxis_title=dict(text='XCO Title', font=dict(color='green')),  # Change x-axis title and color
        yaxis_title=dict(text='YCO Title', font=dict(color='green'))  # Change y-axis title and color
    )

    st.plotly_chart(fig)


#-----------------------------------------------------------------------------------------Predicted Scatter function
import plotly.express as px
def mapshowpredict(df):
    fig = px.scatter(df, x='XCO', y='YCO')

    # Update title attributes
    fig.update_layout(
        title=dict(text='Predicted Location of Trees in 2021', x=0.3, y=0.9,  # Adjust x and y to change title position
                   font=dict(color='dark green', size=20, family='Arial')),  # Change title font attributes
        xaxis_title=dict(text='XCO Title', font=dict(color='Blue')),  # Change x-axis title and color
        yaxis_title=dict(text='YCO Title', font=dict(color='Blue'))  # Change y-axis title and color
    )

    st.plotly_chart(fig)
#------------------------------------------------------------------------------------------------------text box
import streamlit as st

def display_design_element():
    st.subheader("Pasoh Forest Malaysia")

    text = "In this section the 'Actual' and 'Predicted' tree information (Number of Trees in each DBH classes, and Location of Trees) are displayed for years 2019 & 2021."
    font_size = 17
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
#-------------------------------------------------------------------------------Call Text Box
if __name__ == "__main__":
    main()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    #----------------------------------------------------------------------------------Option Bar
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





#----------------------------------------------------------------------------------------------Call the scatter
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

data = pd.read_csv('AllNew.csv')
data = data[['XCO' , 'YCO' , 'SP']]
df = pd.DataFrame(data)
print(df.columns.str.strip())

# Get unique species values for the selectbox
species_list = df['SP'].unique().tolist()
selected_species = st.multiselect('Select Species to see their location', species_list)

if selected_species:
    filtered_df = df[df['SP'].isin(selected_species)]
    mapshow2019(filtered_df)
else:
    mapshow2019(df)

#----------------------------------------------------------------------------------------------Call the scatter predicted
data = pd.read_csv('AllNew.csv')
data = data[['XCO' , 'YCO']]
df = pd.DataFrame(data)
print(df.columns.str.strip())
mapshowpredict(df)