from this import s

import streamlit as st
import pandas as pd
import plotly.express as px
from st_pages import Page, show_pages, add_page_title


add_page_title()

show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("pages/1.📖Summary.py", "Summary", "📖"),
        Page("pages/2.📝Insight.py", "Insight", "📝"),
        Page("pages/3. ⛑️ Prescription Scenarios.py", "Prescription Scenarios", "⛑️"),
        Page("pages/Import Forest Info.py", "Import Forest Info", "⛑️"),
        Page("pages/4.🌲Harvesting Plan: Heavy.py", "Harvesting Plan: Heavy", "🌲"),
        Page("pages/5.🌳Harvesting Plan: Medium.py", "Harvesting Plan: Medium", "🌳"),
        Page("pages/6.🌴Harvesting Plan: Light.py", "Harvesting Plan: Light", "🌴"),
        Page("pages/7.📊Simulation.py" , "Simulation" , "📊"),
        Page("pages/DashboardV2Scientist.py" , "DashboardScientist" , "📊")
        #Page("pages/8. 📟Digital Twin.py", "Digital Twin", "📟"),

    ]
)
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
    #--------------------
    import streamlit as st

#------------------------------------------------------------------------------------------------------text box
import streamlit as st

def display_design_element():

    st.subheader("for Pasoh Forest Reserve")
    st.image('Pasoh.jpeg', caption='Pasoh Forest Reserve')

    text = (" The Pasoh Forest Reserve, \na nature reserve located about 8 km from Simpang Pertang, "
            "Malaysia and around 70 km southeast of Kuala Lumpur. It has a total area of 2,450 hectares,"
            " with a core area of 600 ha surrounded by a buffer zone. "
            "Palm oil plantations surround the reserve on three sides while the other side "
            "adjoins a selectively logged dipterocarp forest. An average of 2 metres of rain fall each year, "
            "ranging from 1,728 to 3,112 mm. In 1987, a 50 hectare forest dynamics plot was established in the reserve."
            " Several censuses of sever population in the plot have been carried out, "
            "the first in 1989, and have counted about 340,000 trees belonging to more that 800 species in that plot.")
    font_size = 17
    font_color = "#333333"  # Dark grey
    border_color = "#568203"  # green
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

#-----------------------------------------------------------------------------------Call first text
def main():
    st.title('Ecology Simulator')

    # Display the design element
    display_design_element()
#-------------------------------------------------------------------------------Call Text Box
if __name__ == "__main__":
    main()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    # ----------------------------------------------------------------------------------------Text in colomns
    import streamlit as st


    def main():
        st.title("Pasoh Forest Reserve Information")

        left_column, right_column = st.columns(2)

        # Left column content
        with left_column:
            st.header("Ecological Zone")
            st.write("Forest Type:  Tropical rainforest")
            st.write("Number of species:  948")
            st.write("Number of stems:  444,338")
            st.write("Number of Trees:  435,839")

        # Right column content
        with right_column:
            st.header("Details")
            st.write("Size: 50.00ha")
            st.write("Dimensions: 1000 x 500")
            st.write("Latitude: 2.982000000000")
            st.write("Longitude: 102.313000000000")


    if __name__ == "__main__":
        main()
#---------------------------------------------------------------------------------------------------map
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    import streamlit as st
    import folium


    def main():
        st.title("Pasoh Forest Reserve Location")

        # Coordinates for Pasoh Forest Reserve
        pasoh_coords = (2.982000000000, 102.313000000000)

        # Create a Folium map centered around Pasoh Forest Reserve
        map_pasoh = folium.Map(location=pasoh_coords, zoom_start=10)

        # Add a marker for Pasoh Forest Reserve
        folium.Marker(location=pasoh_coords, popup="Pasoh Forest Reserve").add_to(map_pasoh)

        # Display the map using st.write()
        folium_static_map(map_pasoh)


    def folium_static_map(m):
        width, height = 700, 400
        html = m.get_root().render()
        st.components.v1.html(html, width=width, height=height)


    if __name__ == "__main__":
        main()




