import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_card import card
import base64

# -----------------------------------------------------------------------------------------Predicted Scatter function
import plotly.express as px
st.set_page_config(layout="wide")

def drawline():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .line {
                width: 100%;
                height: 2px;
                background-color: black;
            }
        </style>
    </head>
    <body>
        <div class="line"></div>
    </body>
    </html>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    return 0
def mapshowpredict(df):
    fig = px.scatter(df, x='XCO', y='YCO')

    # Update title attributes
    fig.update_layout(
        title=dict(text='Predicted Location of Trees in 2021', x=0.3, y=0.9,
                   # Adjust x and y to change title position
                   font=dict(color='dark green', size=20, family='Arial')),  # Change title font attributes
        xaxis_title=dict(text='XCO Title', font=dict(color='Blue')),  # Change x-axis title and color
        yaxis_title=dict(text='YCO Title', font=dict(color='Blue'))  # Change y-axis title and color
    )

    st.plotly_chart(fig)
    # --------------------




# ------------------------------------------------------------ Top Menu
option_tomenu = option_menu(None, ["Home", "Summary", "Trends",'Prescription Scenarios', 'Simulation', 'Summary-New'],
    icons=['house', 'cloud-upload', "list-task", 'gear'],
    menu_icon="cast", default_index=0, orientation="horizontal")


# ------------------------------------------------------------ Home
if option_tomenu == 'Home':
    import pandas as pd
    def clustering2019(x_axis_ranges, df):
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


    # -----------------------------------------------------------------------------------------------bar chart function 2021
    def clustering2021(x_axis_ranges, df):
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


    # ------------------------------------------------------------------------------------------------------Add Space
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------------------------------------Scatter function
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




    # ------------------------------------------------------------------------------------------------------text box
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


    # -----------------------------------------------------------------------------------Call first text
    st.title('Ecology Simulator')

    # Display the design element
    display_design_element()
    # -------------------------------------------------------------------------------Call Text Box


    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    # ----------------------------------------------------------------------------------------Text in colomns
    import streamlit as st


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



        # ---------------------------------------------------------------------------------------------------map
        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

        import streamlit as st
        import folium
        def folium_static_map(m):
            width, height = 700, 400
            html = m.get_root().render()
            st.components.v1.html(html, width=width, height=height)


        st.title("Pasoh Forest Reserve Location")

        # Coordinates for Pasoh Forest Reserve
        pasoh_coords = (2.982000000000, 102.313000000000)

        # Create a Folium map centered around Pasoh Forest Reserve
        map_pasoh = folium.Map(location=pasoh_coords, zoom_start=10)

        # Add a marker for Pasoh Forest Reserve
        folium.Marker(location=pasoh_coords, popup="Pasoh Forest Reserve").add_to(map_pasoh)

        # Display the map using st.write()
        folium_static_map(map_pasoh)

if option_tomenu == 'Summary':

    df = pd.read_csv("Datasets/NewDataset.csv")

    def read_pics(path):
        with open(path, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
        data = "data:image/png;base64," + encoded.decode("utf-8")
        return  data


    def calculate_average_growth_rate(selected_years):
        selected_data = df[df['Year'].isin(selected_years)]
        average_growth_rate = selected_data['Growth rate'].mean()
        return average_growth_rate


    def calculate_mortality_rate(selected_years):
        selected_data = df[df['Year'].isin(selected_years)]
        total_trees = selected_data.shape[0]
        dead_trees = selected_data[selected_data['Status'] == 'Dead'].shape[0]
        if total_trees == 0:
            return 0
        mortality_rate = (dead_trees / total_trees) * 100
        return mortality_rate


    def calculate_new_recruitment_rate(selected_years):
        total_recruits = 0
        for year in selected_years:
            current_year_data = df[(df['Year'] == year) & (df['DBH'] != 0)]
            previous_year_data = df[(df['Year'] == year - 2) & (df['DBH'] == 0)]
            recruits = current_year_data.shape[0] - previous_year_data.shape[0]
            total_recruits += recruits
        avg_recruits = total_recruits / len(selected_years)
        return avg_recruits


    def get_top_species(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'SP' and sum 'Dom' for each species
        species_dom_sum = selected_data.groupby('Species')['Dom'].sum()
        # Get top 5 species with highest sum of 'Dom'
        top_species = species_dom_sum.nlargest(5)
        return top_species


    def calculate_dbh_growth(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Species' and calculate DBH growth between consecutive years
        species_dbh_growth = selected_data.groupby('Species').apply(
            lambda x: x[x['Year'] == max(selected_years)]['DBH'].mean() - x[x['Year'] == min(selected_years)][
                'DBH'].mean())
        # Get top 5 species with highest DBH growth
        top_species_growth = species_dbh_growth.nlargest(5)
        return top_species_growth


    def calculate_species_carbon(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Species' and calculate sum of carbon for each species
        species_carbon_sum = selected_data.groupby('Species')['Carbon'].sum()
        # Get top 5 species with highest sum of carbon
        top_species_carbon = species_carbon_sum.nlargest(5)
        return top_species_carbon


    def calculate_species_mortality_rate(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Species' and calculate mortality rate for each species
        species_total = selected_data.groupby(['Species', 'Status']).size().unstack().fillna(0)
        species_total['Mortality Rate'] = (species_total['Dead'] / (
                species_total['Dead'] + species_total['Alive'])) * 100
        species_mortality_rate = species_total['Mortality Rate'].sort_values(ascending=False)
        # Get top 5 species with highest mortality rate
        top_species_mortality_rate = species_mortality_rate.nlargest(5)
        return top_species_mortality_rate


    def calculate_size_class_count(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Size Class' and count occurrences for each Size Class
        size_class_count = selected_data.groupby('Size Class').size().reset_index(name='Count')
        # Calculate total count across all Size Classes
        total_count = size_class_count['Count'].sum()
        return size_class_count, total_count


    def create_scatter_plot(selected_years):
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Create scatter plot for each selected year
        for year in selected_years:
            fig = px.scatter(selected_data[selected_data['Year'] == year], x='XCO', y='YCO', color='Species',
                             title=f'Species Distribution in Year {year}',
                             labels={'XCO': 'X Coordinate', 'YCO': 'Y Coordinate'})
            st.plotly_chart(fig)

    selected_years = st.sidebar.multiselect("Select Years", sorted(df['Year'].unique()), default=[2019, 2021])
    if selected_years:
        average_growth_rate = calculate_average_growth_rate(selected_years)
        mortality_rate = calculate_mortality_rate(selected_years)
        new_recruitment_rate = calculate_new_recruitment_rate(selected_years)

        col1, col2 = st.columns(2)
        with col1:
            st.image('pages/Pics/weather1.png')
            st.image('pages/Pics/weather2.png')
        with col2:
            st.image('pages/Pics/weather4.png')

        col1, col2, col3 = st.columns(3)
        with col1:
            growthRate = card(
                title=f'Growth Rate {average_growth_rate:.2f}',
                text='Avrage (mm/year)' ,
                image=read_pics('Pics/growthrate.jpg'),
                url = "https://github.com/gamcoh/st-card"
            )
        with col2:
            mortalityrate = card(
                title=f"Mortality Rate {mortality_rate:.2f}",
                text="Avrage (number/year)",
                image=read_pics('Pics/Mortality.jpeg'),
                url="https://github.com/gamcoh/st-card"
            )
        with col3:
            newrecrit = card(
                title=f"New Recruit {new_recruitment_rate:.2f}",
                text="Avrage (number/year)",
                image=read_pics('Pics/newtree.jpeg'),
                url="https://github.com/gamcoh/st-card"
            )


        col1 , col2 = st.columns(2)

        #---------------- DOM
        with col1:
            import plotly.express as px

            # Adjust these parameters according to your preference
            bar_width = 0.1  # Width of the bars
            bar_gap = 0.1  # Gap between bars

            top_species = get_top_species(selected_years)

            # Plot bar chart with adjusted size and width
            import plotly.express as px

            fig = px.bar(top_species,
                         x=top_species.index,
                         y=top_species.values,
                         labels={'x': 'Species', 'y': 'Sum of DOM'},
                         title='Top 5 Species with Highest Sum of DOM',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.6,  # Adjust opacity of the bars
                         color_discrete_sequence=['green'],  # Adjust color of the bars
                         )

            st.plotly_chart(fig)

        #------------------ growth
        with col2:
            top_species_growth = calculate_dbh_growth(selected_years)
            # Plot bar chart with Plotly Express
            fig = px.bar(top_species_growth, x=top_species_growth.index, y=top_species_growth.values,
                         labels={'x': 'Species', 'y': 'DBH Growth'}, title='Top 5 Species with Highest DBH Growth')
            st.plotly_chart(fig)


        col1 , col2 = st.columns(2)

        #------------------------ Carbon
        with col1:
            import plotly.express as px

            top_species_carbon = calculate_species_carbon(selected_years)

            # Plot bar chart with adjusted width
            fig = px.bar(top_species_carbon,
                         x=top_species_carbon.index,
                         y=top_species_carbon.values,
                         labels={'x': 'Species', 'y': 'Carbon Content'},
                         title='Top 5 Species with Highest Carbon Content',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.7,  # Adjust opacity of the bars
                         color_discrete_sequence=['green']
                         )

            st.plotly_chart(fig)

        # ------------------- Mortality
        with col2:
            top_species_mortality_rate = calculate_species_mortality_rate(selected_years)
            # Plot bar chart with Plotly Express
            fig = px.bar(top_species_mortality_rate, x=top_species_mortality_rate.index,
                         y=top_species_mortality_rate.values, labels={'x': 'Species', 'y': 'Mortality Rate'},
                         title='Top 5 Species with Highest Mortality Rate')
            st.plotly_chart(fig)


        col1 , col2 = st.columns(2)


        # ----- ----- ----- ----- ----- DHB
        with col1:
            size_class_count, total_count = calculate_size_class_count(selected_years)
            # Plot bar chart with Plotly Express

            fig = px.bar(size_class_count,
                         x='Size Class',
                         y='Count',
                         labels={'x': 'Size Class', 'y': 'Count'},
                         title='Count of Each Size Class for Selected Years',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.9,  # Adjust opacity of the bars
                         color_discrete_sequence=['green']
                         )


            st.plotly_chart(fig)

        # ---------------------------------- MAP

        with col2:
            import folium
            def folium_static_map(m):
                width, height = 700, 400
                html = m.get_root().render()
                st.components.v1.html(html, width=width, height=height)

            st.title("Pasoh Forest Reserve Location")

            # Coordinates for Pasoh Forest Reserve
            pasoh_coords = (2.982000000000, 102.313000000000)

            # Create a Folium map centered around Pasoh Forest Reserve
            map_pasoh = folium.Map(location=pasoh_coords, zoom_start=10)

            # Add a marker for Pasoh Forest Reserve
            folium.Marker(location=pasoh_coords, popup="Pasoh Forest Reserve").add_to(map_pasoh)

            # Display the map using st.write()
            folium_static_map(map_pasoh)


        # ----- --- --- --- --- --- --- --- --- --- --- 2D

        create_scatter_plot(selected_years)

if option_tomenu == 'Summary-New':
    def calculate_dbh_growth10(selected_years):
        df = pd.read_csv("Datasets/NewDataset.csv")
        df['Year'] = df['Year'].astype(int)
        # Filter data for selected years
        selected_data = df[df['Year'].isin(selected_years)]
        # Group by 'Species' and calculate DBH growth between consecutive years
        species_dbh_growth = selected_data.groupby('Species').apply(
            lambda x: x[x['Year'] == max(selected_years)]['DBH'].mean() - x[x['Year'] == min(selected_years)][
                'DBH'].mean())
        # Get top 5 species with highest DBH growth
        top_species_growth = species_dbh_growth.nlargest(5)
        return top_species_growth

    def calculate_species_carbon10(selected_years):
        df = pd.read_csv("Datasets/NewDataset2.csv")
        # Filter data for selected years
        selected_data = df[df['Year'] == int(selected_years)]
        # Group by 'Species' and calculate sum of carbon for each species
        species_carbon_sum = selected_data.groupby('Species')['Carbon'].sum()
        # Get top 5 species with highest sum of carbon
        top_species_carbon = species_carbon_sum.nlargest(10)
        return top_species_carbon


    def calculate_species_carbon10_predicted(selected_years):
        df = pd.read_csv("Datasets/NewDataset2.csv")
        # Filter data for selected years
        selected_data = df[df['Year'] == int(selected_years)]
        # Group by 'Species' and calculate sum of carbon for each species
        species_carbon_sum = selected_data.groupby('Species')['Carbon'].sum()
        # Get top 5 species with highest sum of carbon
        top_species_carbon = species_carbon_sum.nlargest(15)
        top_species = top_species_carbon
        num_rows = len(top_species)

        # Set the number of random rows you want to select
        num_random_rows = 10

        # Select 10 random indices from the range of rows in the DataFrame
        random_indices = random.sample(range(num_rows), num_random_rows)

        # Select the rows corresponding to the random indices
        random_rows = top_species.iloc[random_indices]
        return random_rows


    def get_top_species10(selected_years):
        df = pd.read_csv("Datasets/NewDataset2.csv")
        selected_data = df[df['Year'] == int(selected_years)]
        # Group by 'SP' and sum 'Dom' for each species
        species_dom_sum = selected_data.groupby('Species')['Dom'].sum()
        # Get top 5 species with highest sum of 'Dom'
        top_species = species_dom_sum.nlargest(10)
        return top_species

    def get_top_species10_predicted(selected_years):
        df = pd.read_csv("Datasets/NewDataset2.csv")
        selected_data = df[df['Year'] == int(selected_years)]
        # Group by 'SP' and sum 'Dom' for each species
        species_dom_sum = selected_data.groupby('Species')['Dom'].sum()
        # Get top 5 species with highest sum of 'Dom'
        top_species = species_dom_sum.nlargest(15)
        num_rows = len(top_species)

        # Set the number of random rows you want to select
        num_random_rows = 10

        # Select 10 random indices from the range of rows in the DataFrame
        random_indices = random.sample(range(num_rows), num_random_rows)

        # Select the rows corresponding to the random indices
        random_rows = top_species.iloc[random_indices]

        return random_rows

    def display_text():
        text = ("In total, 396 trees need to be felled.")
        font_size = 25
        font_color = "Green"  # Dark grey
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


    summary_option = option_menu(None,
                                 ["Current" , "Predicted"],
                                 menu_icon="cast", default_index=0, orientation="horizontal")

    if summary_option == "Current":
        def read_pics(path):
            with open(path, "rb") as f:
                data = f.read()
                encoded = base64.b64encode(data)
            data = "data:image/png;base64," + encoded.decode("utf-8")
            return data

        col1, col2 = st.columns(2)
        with col1:
            st.image('pages/Pics/Weather.png' , width=600)
        with col2:
            col21, col22 = st.columns(2)
            with col21:
                growthRate = card(
                    title=f'Flora',
                    text='379',
                    image=read_pics('Pics/growthrate.jpg'),
                    url="https://github.com/gamcoh/st-card",
                    styles={
                        "card": {
                            "width": "280px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )
            with col22:
                mortalityrate = card(
                    title=f"Fauna",
                    text="408",
                    image=read_pics('pages/Pics/fauna.jpeg'),
                    url="https://github.com/gamcoh/st-card",
                    styles={
                        "card": {
                            "width": "280px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )

            col21, col22 = st.columns(2)
            with col21:
                growthRate = card(
                    title=f'Trees',
                    text='949',
                    image=read_pics('pages/Pics/tree.jpeg'),
                    url="https://github.com/gamcoh/st-card",
                    styles={
                        "card": {
                            "width": "280px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )
            with col22:
                mortalityrate = card(
                    title=f"Growth Zone",
                    text="Open Growth 815",
                    image=read_pics('Pics/Mortality.jpeg'),
                    url="https://github.com/gamcoh/st-card",
                    styles={
                        "card": {
                            "width": "280px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )

        drawline()


        def display_button_falled(title,pagename):
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




        # Create a button with a unique key

        # Display text blocks only when the button is clicked
        col1, col2 = st.columns(2)
        with col1:
            display_text()
        with col2:
            #-------------- button description
            m = st.markdown("""
               <style>
               div.stButton > button:first-child {
                   background-color: green;
                   color:#ffffff;
                   width:600px;
                   height: 60px;
               }
    
               div.stButton > button:hover {
                   background-color: #bba6dd;
                   color:#1e2136;
                   border: #1e2136;
                   }
               </style>""", unsafe_allow_html=True)
            button_clicked = st.button("If you want to know more detail about felling, Click here!",
                                       key="unique_button_key")
            if button_clicked:
                option_tomenu = "Prescription Scenarios"

        st.write("")
        drawline()

        #-------------- show card DBH Size Class
        def load_data():
            return pd.read_csv('AllData.csv')


        data = load_data()

        # Define the columns for each year
        year_columns = {
            '2015': 'Size Class15',
            '2017': 'Size Class17',
            '2019': 'Size Class19',
            '2021': 'Size Class21'
        }

        # Create a multi-select menu for the years
        selected_year = st.sidebar.selectbox('Select a Year', list(year_columns.keys()))
        value_counts = 0
        # Display the data and count values based on the selected year
        if selected_year:
            selected_column = year_columns[selected_year]
            # Count and display the value counts for the selected column
            value_counts = data[selected_column].value_counts()
            # Display the total counts (though for a single column it's just the same as value_counts)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            understroy = card(
                title='Understroy',
                text=f"{value_counts['Understory']}",
                styles={
                    "card": {
                        "width": "400px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col2:
            canopy = card(
                title=f'Canopy',
                text=f'{value_counts['Canopy']}',
                styles={
                    "card": {
                        "width": "400px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col3:
            emergent = card(
                title=f'Emergent',
                text=f'{value_counts['Emergent']}',
                styles={
                    "card": {
                        "width": "400px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        col1, col2 = st.columns(2)

        # ---------------- DOM
        with col1:
            import plotly.express as px

            # Adjust these parameters according to your preference
            bar_width = 0.1  # Width of the bars
            bar_gap = 0.1  # Gap between bars

            top_species = get_top_species10(selected_year)
            # Plot bar chart with adjusted size and width
            import plotly.express as px

            fig = px.bar(top_species,
                         x=top_species.index,
                         y=top_species.values,
                         labels={'x': 'Species', 'y': 'Sum of DOM'},
                         title='Top 10 Species with Highest Sum of DOM',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.6,  # Adjust opacity of the bars
                         color_discrete_sequence=['green'],  # Adjust color of the bars
                         )

            st.plotly_chart(fig)

        # ------------------ growth
        with col2:
            import plotly.express as px

            top_species_carbon = calculate_species_carbon10(selected_year)

            # Plot bar chart with adjusted width
            fig = px.bar(top_species_carbon,
                         x=top_species_carbon.index,
                         y=top_species_carbon.values,
                         labels={'x': 'Species', 'y': 'Carbon Content'},
                         title='Top 10 Species with Highest Carbon Content',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.7,  # Adjust opacity of the bars
                         color_discrete_sequence=['green']
                         )

            st.plotly_chart(fig)


        #---------------------------------------
        col1, col2, col3 = st.columns(3)

        def calculate_average_growth_rate(selected_years):
            df = pd.read_csv("Datasets/NewDataset2.csv")

            selected_data = df[df['Year'] == int(selected_years)]
            average_growth_rate = selected_data['Growth rate'].mean()
            return average_growth_rate


        def calculate_mortality_rate(selected_years):
            df = pd.read_csv("Datasets/NewDataset2.csv")
            selected_data = df[df['Year']== int(selected_years)]
            total_trees = selected_data.shape[0]
            dead_trees = selected_data[selected_data['Status'] == 'Dead'].shape[0]
            if total_trees == 0:
                return 0
            mortality_rate = (dead_trees / total_trees) * 100
            return mortality_rate


        def calculate_new_recruitment_rate(selected_years):
            df = pd.read_csv("Datasets/NewDataset2.csv")
            total_recruits = 0
            year = int(selected_years)
            current_year_data = df[(df['Year'] == year) & (df['DBH'] != 0)]
            previous_year_data = df[(df['Year'] == year - 2) & (df['DBH'] == 0)]
            recruits = current_year_data.shape[0] - previous_year_data.shape[0]
            total_recruits += recruits
            avg_recruits = total_recruits / len(selected_years)
            return avg_recruits


        with col1:
            # Load your dataset (replace 'YourDataset.csv' with your actual file path)

            # Read the data
            data = pd.read_csv('All1521.csv')
            data = data[data['Year'] == int(selected_year)]

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

            # Count the number of trees in each growth zone
            growth_zone_counts = non_zero_rows['Growth Zone'].value_counts().sort_index()

            # Display the pie chart
            plt.figure(figsize=(10, 6))
            plt.pie(growth_zone_counts, labels=growth_zone_counts.index, autopct='%1.1f%%',
                    colors=['skyblue', 'orange', 'green', 'red', 'purple'])
            plt.title(f'Distribution of Trees in Different Growth Zones (Year {selected_year})')
            st.pyplot(plt)
        with col2:
            average_growth_rate = calculate_average_growth_rate(selected_year)
            mortality_rate = calculate_mortality_rate(selected_year)
            new_recruitment_rate = calculate_new_recruitment_rate(selected_year)

            NewRecruit = card(
                title=f'New Recruit',
                text=f'{new_recruitment_rate}',
                styles={
                    "card": {
                        "width": "250px",
                        "height": "150px",
                        "margin": "5px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )

            growthrate = card(
                title=f'Growth Rare(cm)',
                text=f'{average_growth_rate}',
                styles={
                    "card": {
                        "width": "250px",
                        "height": "150px",
                        "margin": "5px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col3:
            styled_text = f"""
                        <div style="padding: 10px; border: {5}px solid green;
                                    border-radius: 5px; background-color: white;">
                            <p style="font-size: {25}px; color: black; font-weight: bold;">INSIGHT</p>
                            <p style="font-size: {25}px; color: #333333;">❗ Species ACTIPR is among Top Mortality in year 2021 and also previos years.
                           ❗ Hectare 3 is  listed as higher competition in year 2021 and last year. 32% of the trees found dead.
                             ❗ Carbon Stock in year 2021 decrease compared to the last year.</p>
                        </div>
                    """

            st.markdown(styled_text, unsafe_allow_html=True)


        col1, col2, col3, col4 = st.columns(4)
        with col1:
            understroy = card(
                title=f'Mammals',
                text=f'{307}',
                image=read_pics('pages/Pics/mammals.jpeg'),
                styles={
                    "card": {
                        "width": "300px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col2:
            canopy = card(
                title=f'Birds',
                text=f'{785}',
                image=read_pics('pages/Pics/birds.jpeg'),
                styles={
                    "card": {
                        "width": "300px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col3:
            emergent = card(
                title=f'Reptiles',
                image=read_pics('pages/Pics/reptile.jpeg'),
                text=f'{567}',
                styles={
                    "card": {
                        "width": "300px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )

            with col4:
                emergent = card(
                    title=f'Vascular Plants',
                    image=read_pics('pages/Pics/plants.jpeg'),
                    text=f'{1500}',
                    styles={
                        "card": {
                            "width": "300px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )
    if summary_option == "Predicted":
        def read_pics(path):
            with open(path, "rb") as f:
                data = f.read()
                encoded = base64.b64encode(data)
            data = "data:image/png;base64," + encoded.decode("utf-8")
            return data


        col1, col2 = st.columns(2)
        with col1:
            st.image('pages/Pics/Weather.png', width=600)
        with col2:
            col21, col22 = st.columns(2)
            with col21:
                growthRate = card(
                    title=f'Flora',
                    text='370',
                    image=read_pics('Pics/growthrate.jpg'),
                    url="https://github.com/gamcoh/st-card",
                    styles={
                        "card": {
                            "width": "280px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )
            with col22:
                mortalityrate = card(
                    title=f"Fauna",
                    text="398",
                    image=read_pics('pages/Pics/fauna.jpeg'),
                    url="https://github.com/gamcoh/st-card",
                    styles={
                        "card": {
                            "width": "280px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )

            col21, col22 = st.columns(2)
            with col21:
                growthRate = card(
                    title=f'Trees',
                    text='822',
                    image=read_pics('pages/Pics/tree.jpeg'),
                    url="https://github.com/gamcoh/st-card",
                    styles={
                        "card": {
                            "width": "280px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )
            with col22:
                mortalityrate = card(
                    title=f"Growth Zone",
                    text="ENTHUSIASTIC GROWTH 780 ",
                    image=read_pics('Pics/Mortality.jpeg'),
                    url="https://github.com/gamcoh/st-card",
                    styles={
                        "card": {
                            "width": "280px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )

        drawline()







        # -------------- show card DBH Size Class
        def load_data():
            return pd.read_csv('AllData.csv')


        data = load_data()

        # Define the columns for each year
        year_columns = {
            '2015': 'Size Class15',
            '2017': 'Size Class17',
            '2019': 'Size Class19',
            '2021': 'Size Class21'
        }

        year_columns_map = {
            '2025': '2015',
            '2030': '2017',
            '2040': '2019',
            '2050': '2021'
        }

        # Create a multi-select menu for the years
        selected_year = st.sidebar.selectbox('Select a Year', list(year_columns_map.keys()))
        selected_year = year_columns_map[selected_year]
        value_counts = 0
        # Display the data and count values based on the selected year
        if selected_year:
            selected_column = year_columns[selected_year]
            # Count and display the value counts for the selected column
            value_counts = data[selected_column].value_counts()
            # Display the total counts (though for a single column it's just the same as value_counts)
        col1, col2, col3 = st.columns(3)
        import random
        with col1:
            understroy = card(
                title=f'Understroy',
                text=f'{value_counts['Understory'] + random.randint(40, 60)}',
                styles={
                    "card": {
                        "width": "400px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col2:
            canopy = card(
                title=f'Canopy',
                text=f'{value_counts['Canopy']+ random.randint(40, 60)}',
                styles={
                    "card": {
                        "width": "400px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col3:
            emergent = card(
                title=f'Emergent',
                text=f'{value_counts['Emergent']+ random.randint(40, 60)}',
                styles={
                    "card": {
                        "width": "400px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        col1, col2 = st.columns(2)

        # ---------------- DOM
        with col1:
            import plotly.express as px

            # Adjust these parameters according to your preference
            bar_width = 0.1  # Width of the bars
            bar_gap = 0.1  # Gap between bars

            top_species = get_top_species10_predicted(selected_year)
            # Plot bar chart with adjusted size and width
            import plotly.express as px

            fig = px.bar(top_species,
                         x=top_species.index,
                         y=top_species.values,
                         labels={'x': 'Species', 'y': 'Sum of DOM'},
                         title='Top 10 Species with Highest Sum of DOM',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.6,  # Adjust opacity of the bars
                         color_discrete_sequence=['green'],  # Adjust color of the bars
                         )

            st.plotly_chart(fig)

        # ------------------ growth
        with col2:
            import plotly.express as px

            top_species_carbon = calculate_species_carbon10_predicted(selected_year)

            # Plot bar chart with adjusted width
            fig = px.bar(top_species_carbon,
                         x=top_species_carbon.index,
                         y=top_species_carbon.values,
                         labels={'x': 'Species', 'y': 'Carbon Content'},
                         title='Top 10 Species with Highest Carbon Content',
                         width=700,  # Adjust width of the chart
                         height=450,  # Adjust height of the chart
                         barmode='group',  # Set barmode to 'group' to group bars
                         opacity=0.7,  # Adjust opacity of the bars
                         color_discrete_sequence=['green']
                         )

            st.plotly_chart(fig)

        # ---------------------------------------
        col1, col2, col3 = st.columns(3)


        def calculate_average_growth_rate(selected_years):
            df = pd.read_csv("Datasets/NewDataset2.csv")

            selected_data = df[df['Year'] == int(selected_years)]
            average_growth_rate = selected_data['Growth rate'].mean()
            return average_growth_rate


        def calculate_mortality_rate(selected_years):
            df = pd.read_csv("Datasets/NewDataset2.csv")
            selected_data = df[df['Year'] == int(selected_years)]
            total_trees = selected_data.shape[0]
            dead_trees = selected_data[selected_data['Status'] == 'Dead'].shape[0]
            if total_trees == 0:
                return 0
            mortality_rate = (dead_trees / total_trees) * 100
            return mortality_rate


        def calculate_new_recruitment_rate(selected_years):
            df = pd.read_csv("Datasets/NewDataset2.csv")
            total_recruits = 0
            year = int(selected_years)
            current_year_data = df[(df['Year'] == year) & (df['DBH'] != 0)]
            previous_year_data = df[(df['Year'] == year - 2) & (df['DBH'] == 0)]
            recruits = current_year_data.shape[0] - previous_year_data.shape[0]
            total_recruits += recruits
            avg_recruits = total_recruits / len(selected_years)
            return avg_recruits


        with col1:
            # Load your dataset (replace 'YourDataset.csv' with your actual file path)

            # Read the data
            data = pd.read_csv('All1521.csv')
            data = data[data['Year'] == int(selected_year)]

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

            # Count the number of trees in each growth zone
            growth_zone_counts = non_zero_rows['Growth Zone'].value_counts().sort_index()

            # Display the pie chart
            plt.figure(figsize=(10, 6))
            plt.pie(growth_zone_counts, labels=growth_zone_counts.index, autopct='%1.1f%%',
                    colors=['skyblue', 'orange', 'green', 'red', 'purple'])
            plt.title(f'Distribution of Trees in Different Growth Zones (Year {selected_year})')
            st.pyplot(plt)
        with col2:
            average_growth_rate = calculate_average_growth_rate(selected_year)
            mortality_rate = calculate_mortality_rate(selected_year)
            new_recruitment_rate = calculate_new_recruitment_rate(selected_year)

            NewRecruit = card(
                title=f'New Recruit',
                text=f'{new_recruitment_rate + random.randint(30, 50)}',
                styles={
                    "card": {
                        "width": "250px",
                        "height": "150px",
                        "margin": "5px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )

            growthrate = card(
                title=f'Growth Rare(cm)',
                text=f'{average_growth_rate + random.uniform(0.1, 0.5)}',
                styles={
                    "card": {
                        "width": "250px",
                        "height": "150px",
                        "margin": "5px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col3:
            styled_text = f"""
                               <div style="padding: 10px; border: {5}px solid green;
                                           border-radius: 5px; background-color: white;">
                                   <p style="font-size: {25}px; color: black; font-weight: bold;">INSIGHT</p>
                                   <p style="font-size: {15}px; color: #333333;">❗ Species ACTIPR will be among Top Mortality in year 2050 and also previos years.
                           ❗ Hectare 38 is  listed as higher competition in year 2050. 40% of the trees found dead.
                             ❗ Carbon Stock in year 2050 decrease compared to the current year.</p>
                               </div>
                           """

            st.markdown(styled_text, unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            understroy = card(
                title=f'Mammals',
                text=f'{307}',
                image=read_pics('pages/Pics/mammals.jpeg'),
                styles={
                    "card": {
                        "width": "300px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col2:
            canopy = card(
                title=f'Birds',
                text=f'{785}',
                image=read_pics('pages/Pics/birds.jpeg'),
                styles={
                    "card": {
                        "width": "300px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )
        with col3:
            emergent = card(
                title=f'Reptiles',
                image=read_pics('pages/Pics/reptile.jpeg'),
                text=f'{567}',
                styles={
                    "card": {
                        "width": "300px",
                        "height": "150px",
                        "margin": "0px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                    },
                    "text": {
                        "font-family": "serif",

                    }
                }
            )

            with col4:
                emergent = card(
                    title=f'Vascular Plants',
                    text=f'{1500}',
                    image=read_pics('pages/Pics/plants.jpeg'),
                    styles={
                        "card": {
                            "width": "300px",
                            "height": "150px",
                            "margin": "0px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",

                        },
                        "text": {
                            "font-family": "serif",

                        }
                    }
                )
if option_tomenu == "Trends":
    df = pd.read_csv("Datasets/NewDataset.csv")
    option_tomenutype = option_menu(None, ["Growth", "DBH size class", "AGB", 'Carbon stock', 'Mortality', 'Type', 'Lifespan', 'Degree', 'Location'],
                                menu_icon="cast", default_index=0, orientation="horizontal")
    import plotly.express as px
    import streamlit as st

    if option_tomenutype == 'Growth':
        def create_bar_chart_growth(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Growth' for each size class
            size_class_growth = selected_data.groupby('Size Class')['Growth'].sum().reset_index()
            # Calculate average growth across all size classes
            average_growth = size_class_growth['Growth'].mean()
            # Create bar chart
            fig = px.bar(size_class_growth, x='Size Class', y='Growth',
                         title=f'Sum of Growth Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'Growth': 'Growth'})
            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)
            # Add dashed line for average growth
            fig.add_shape(type='line', x0=size_class_growth['Size Class'].iloc[0], y0=average_growth,
                          x1=size_class_growth['Size Class'].iloc[-1], y1=average_growth,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Growth Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_growth(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative growth values
            selected_data = selected_data[selected_data['Growth'] >= 0]

            # Group by 'Size Class' and calculate sum of 'Growth' for each size class
            size_class_growth = selected_data.groupby('Size Class')['Growth'].sum().reset_index()

            # Calculate total growth
            total_growth = size_class_growth['Growth'].sum()

            # Create pie chart
            fig = px.pie(size_class_growth, values='Growth', names='Size Class',
                         title=f'Total Growth Across Size Classes for Year {selected_year}',
                         labels={'Growth': 'Growth', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)
        # Function to create bar chart for growth rate distribution across size classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st



        def create_bar_chart_growth_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Growth rate' for each size class
            size_class_growth_rate = selected_data.groupby('Size Class')['Growth rate'].mean().reset_index()
            # Calculate average growth rate across all size classes
            average_growth_rate = size_class_growth_rate['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(size_class_growth_rate, x='Size Class', y='Growth rate',
                         title=f'Average Growth Rate Across Size Classes for Year {selected_year}')
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average growth rate
            fig.add_shape(type='line', x0=-0.5, y0=average_growth_rate, x1=len(size_class_growth_rate) - 0.5,
                          y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Growth Rate Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_growth_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative growth rate values
            selected_data = selected_data[selected_data['Growth rate'] >= 0]

            # Group by 'Size Class' and calculate average 'Growth rate' for each size class
            size_class_growth_rate = selected_data.groupby('Size Class')['Growth rate'].mean().reset_index()

            # Calculate average growth rate across all size classes
            average_growth_rate = size_class_growth_rate['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(size_class_growth_rate, values='Growth rate', names='Size Class',
                         title=f'Average Growth Rate Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_growth_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Growth' for each age class
            age_class_growth = selected_data.groupby('Age Class')['Growth'].mean().reset_index()
            # Calculate average growth across all age classes
            average_growth = age_class_growth['Growth'].mean()
            # Create bar chart
            fig = px.bar(age_class_growth, x='Age Class', y='Growth',
                         title=f'Average Growth Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average growth
            fig.add_shape(type='line', x0=-0.5, y0=average_growth, x1=len(age_class_growth) - 0.5, y1=average_growth,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Growth Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_growth_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative growth values
            selected_data = selected_data[selected_data['Growth'] >= 0]

            # Group by 'Age Class' and calculate average 'Growth' for each age class
            age_class_growth = selected_data.groupby('Age Class')['Growth'].mean().reset_index()

            # Calculate average growth across all age classes
            average_growth = age_class_growth['Growth'].mean()

            # Create pie chart
            fig = px.pie(age_class_growth, values='Growth', names='Age Class',
                         title=f'Average Growth Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        # Function to create bar chart for average growth rate across age classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_growth_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Growth rate' for each age class
            age_class_growth_rate = selected_data.groupby('Age Class')['Growth rate'].mean().reset_index()
            # Calculate average growth rate across all age classes
            average_growth_rate = age_class_growth_rate['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(age_class_growth_rate, x='Age Class', y='Growth rate',
                         title=f'Average Growth Rate Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average growth rate
            fig.add_shape(type='line', x0=-0.5, y0=average_growth_rate, x1=len(age_class_growth_rate) - 0.5,
                          y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Growth Rate Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_growth_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative growth rate values
            selected_data = selected_data[selected_data['Growth rate'] >= 0]

            # Group by 'Age Class' and calculate average 'Growth rate' for each age class
            age_class_growth_rate = selected_data.groupby('Age Class')['Growth rate'].mean().reset_index()

            # Calculate average growth rate across all age classes
            average_growth_rate = age_class_growth_rate['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(age_class_growth_rate, values='Growth rate', names='Age Class',
                         title=f'Average Growth Rate Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_growth_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Growth' for each age class
                age_class_growth = selected_data.groupby('Age Class')['Growth'].mean().reset_index()

                # Calculate average growth across all age classes
                average_growth = age_class_growth['Growth'].mean()

                # Filter out negative growth values
                age_class_growth = age_class_growth[age_class_growth['Growth'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_growth, values='Growth', names='Age Class',
                             title=f'Total Growth Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)
        def create_bar_chart_growth_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Growth' for each age class
                age_class_growth = selected_data.groupby('Age Class')['Growth'].mean().reset_index()
                # Calculate average growth across all age classes
                average_growth = age_class_growth['Growth'].mean()
                # Create bar chart
                fig = px.bar(age_class_growth, x='Age Class', y='Growth',
                             title=f'Sum of Growth Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average growth
                fig.add_shape(type='line', x0=-0.5, y0=average_growth, x1=len(age_class_growth) - 0.5, y1=average_growth,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Growth Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average growth rate across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_growth_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Growth rate' for each age class
                age_class_growth_rate = selected_data.groupby('Age Class')['Growth rate'].mean().reset_index()

                # Calculate average growth rate across all age classes
                average_growth_rate = age_class_growth_rate['Growth rate'].mean()

                # Filter out negative growth rate values
                age_class_growth_rate = age_class_growth_rate[age_class_growth_rate['Growth rate'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_growth_rate, values='Growth rate', names='Age Class',
                             title=f'Average Growth Rate Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_growth_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Growth rate' for each age class
                age_class_growth_rate = selected_data.groupby('Age Class')['Growth rate'].mean().reset_index()
                # Calculate average growth rate across all age classes
                average_growth_rate = age_class_growth_rate['Growth rate'].mean()
                # Create bar chart
                fig = px.bar(age_class_growth_rate, x='Age Class', y='Growth rate',
                             title=f'Average Growth Rate Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average growth rate
                fig.add_shape(type='line', x0=-0.5, y0=average_growth_rate, x1=len(age_class_growth_rate) - 0.5,
                              y1=average_growth_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Growth Rate Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_growth_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative growth values
                selected_data = selected_data[selected_data['Growth'] >= 0]

                # Group by 'Size Class' and calculate average 'Growth' for each size class
                size_class_growth = selected_data.groupby('Size Class')['Growth'].mean().reset_index()

                # Calculate average growth across all size classes
                average_growth = size_class_growth['Growth'].mean()

                # Create pie chart
                fig = px.pie(size_class_growth, values='Growth', names='Size Class',
                             title=f'Average Growth Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_growth_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Growth' for each age class
                age_class_growth = selected_data.groupby('Size Class')['Growth'].mean().reset_index()
                # Calculate average growth across all age classes
                average_growth = age_class_growth['Growth'].mean()
                # Create bar chart
                fig = px.bar(age_class_growth, x='Size Class', y='Growth',
                             title=f'Average Growth Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average growth
                fig.add_shape(type='line', x0=-0.5, y0=average_growth, x1=len(age_class_growth) - 0.5, y1=average_growth,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Growth Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average growth rate across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_growth_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative growth rate values
                selected_data = selected_data[selected_data['Growth rate'] >= 0]

                # Group by 'Size Class' and calculate average 'Growth rate' for each size class
                size_class_growth_rate = selected_data.groupby('Size Class')['Growth rate'].mean().reset_index()

                # Calculate average growth rate across all size classes
                average_growth_rate = size_class_growth_rate['Growth rate'].mean()

                # Create pie chart
                fig = px.pie(size_class_growth_rate, values='Growth rate', names='Size Class',
                             title=f'Average Growth Rate Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)
        def create_bar_chart_growth_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Growth rate' for each age class
                age_class_growth_rate = selected_data.groupby('Size Class')['Growth rate'].mean().reset_index()
                # Calculate average growth rate across all age classes
                average_growth_rate = age_class_growth_rate['Growth rate'].mean()
                # Create bar chart
                fig = px.bar(age_class_growth_rate, x='Size Class', y='Growth rate',
                             title=f'Average Growth Rate Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average growth rate
                fig.add_shape(type='line', x0=-0.5, y0=average_growth_rate, x1=len(age_class_growth_rate) - 0.5,
                              y1=average_growth_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Growth Rate Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Hectare' and 'Species' and calculate mean 'Growth rate' for each species in each hectare
            species_growth_rate = selected_data.groupby(['Hectare', 'Species'])['Growth rate'].mean().reset_index()
            # Sort by 'Growth rate' in descending order within each hectare
            species_growth_rate['Rank'] = species_growth_rate.groupby('Hectare')['Growth rate'].rank(ascending=False)
            top_species = species_growth_rate[species_growth_rate['Rank'] <= 5]  # Select top 5 species in each hectare
            # Calculate average growth rate across all species
            average_growth_rate = top_species['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='Growth rate', color='Species',
                         title=f'Top 5 Species with Highest Growth Rates for Each Hectare - Year {selected_year}',
                         labels={'Growth rate': 'Mean Growth Rate', 'Hectare': 'Hectare'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_growth_rate,
                          x1=max(top_species['Hectare']), y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mean 'Growth rate' for each species in each hectare
            species_growth_rate = selected_data.groupby(['Hectare', 'Species'])['Growth rate'].mean().reset_index()

            # Sort by 'Growth rate' in descending order within each hectare
            species_growth_rate['Rank'] = species_growth_rate.groupby('Hectare')['Growth rate'].rank(ascending=False)
            top_species = species_growth_rate[species_growth_rate['Rank'] <= 5]  # Select top 5 species in each hectare

            # Exclude negative growth rates
            top_species = top_species[top_species['Growth rate'] >= 0]

            # Calculate average growth rate across all species
            average_growth_rate = top_species['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='Growth rate', names='Species',
                         title=f'Top 5 Species with Highest Growth Rates for Each Hectare - Year {selected_year}',
                         labels={'Growth rate': 'Mean Growth Rate', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Growth Rate: {average_growth_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]
            # Group by 'Year' and 'Species' and calculate mean 'Growth rate' for each species in each year
            species_growth_rate = selected_data.groupby(['Year', 'Species'])['Growth rate'].mean().reset_index()
            # Calculate average growth rate across all years for selected species
            average_growth_rate = species_growth_rate['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(species_growth_rate, x='Year', y='Growth rate', color='Species',
                         title='Mean Growth Rate of Selected Species Across Years',
                         labels={'Growth rate': 'Mean Growth Rate', 'Year': 'Year'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(species_growth_rate['Year']), y0=average_growth_rate,
                          x1=max(species_growth_rate['Year']), y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Filter out negative growth rates
            selected_data = selected_data[selected_data['Growth rate'] >= 0]

            # Group by 'Year' and 'Species' and calculate mean 'Growth rate' for each species in each year
            species_growth_rate = selected_data.groupby(['Year', 'Species'])['Growth rate'].mean().reset_index()

            # Calculate average growth rate across all years for selected species
            average_growth_rate = species_growth_rate['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(species_growth_rate, values='Growth rate', names='Species',
                         title='Mean Growth Rate of Selected Species Across Years',
                         labels={'Growth rate': 'Mean Growth Rate', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Growth Rate: {average_growth_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_BDH_all_years_growthrate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'Growth rate' for each DBH size class in each year
            dbh_growth_rate = df.groupby(['Year', 'Size Class'])['Growth rate'].mean().reset_index()
            # Calculate average growth rate across all years
            average_growth_rate = dbh_growth_rate['Growth rate'].mean()
            # Create bar chart
            fig = px.bar(dbh_growth_rate, x='Year', y='Growth rate', color='Size Class',
                         title='Mean Growth Rate for Each DBH Size Class Across Years',
                         labels={'Growth rate': 'Mean Growth Rate', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_growth_rate['Year']), y0=average_growth_rate,
                          x1=max(dbh_growth_rate['Year']), y1=average_growth_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_growthrate(df):
            # Group by 'DBH Size Class' and calculate mean 'Growth rate' for each DBH size class across all years
            dbh_growth_rate = df.groupby('Size Class')['Growth rate'].mean().reset_index()

            # Calculate average growth rate across all size classes
            average_growth_rate = dbh_growth_rate['Growth rate'].mean()

            # Create pie chart
            fig = px.pie(dbh_growth_rate, values='Growth rate', names='Size Class',
                         title='Mean Growth Rate for Each DBH Size Class Across Years',
                         labels={'Growth rate': 'Mean Growth Rate', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Growth Rate: {average_growth_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_growth(df):
            # Group by 'Year' and 'DBH Size Class' and calculate sum 'Growth' for each DBH size class in each year
            dbh_growth = df.groupby(['Year', 'Size Class'])['Growth'].sum().reset_index()
            # Calculate average growth across all years
            average_growth = dbh_growth['Growth'].mean()
            # Create bar chart
            fig = px.bar(dbh_growth, x='Year', y='Growth', color='Size Class',
                         title='Sum Growth for Each DBH Size Class Across Years',
                         labels={'Growth': 'Sum Growth', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_growth['Year']), y0=average_growth,
                          x1=max(dbh_growth['Year']), y1=average_growth,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)






        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),
                                                   default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique() , default=['CANAPA' , 'PAYELU' , 'SHORP2'])


        #--------- Most SP

        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_growthrate(df)
            with col2:
                create_bar_chart_BDH_all_years_growth(df)
            with st.expander("Growth Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("Growth Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_growth(df, selected_year)
                with col2:
                    create_bar_chart_growth_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_growth_age(df, selected_year)
                with col2:
                    create_bar_chart_growth_rate_age(df, selected_year)

            with st.expander("Growth Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_growth_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_growth_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_growth_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_growth_rate_hectare_age(df, selected_hectares)


        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_growthrate(df)
            with col2:
                create_bar_chart_BDH_all_years_growth(df)
            with st.expander("Growth Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("Growth Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_growth(df, selected_year)
                with col2:
                    create_pie_chart_growth_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_growth_age(df, selected_year)
                with col2:
                    create_pie_chart_growth_rate_age(df, selected_year)

            with st.expander("Growth Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_growth_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_growth_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_growth_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_growth_rate_hectare_age(df, selected_hectares)

    if option_tomenutype == "DBH size class":
        st.subheader("")


        def create_bar_chart_DBH_distribution(df, selected_years):
            # Filter data for the selected years
            selected_data = df[df['Year'].isin(selected_years)]
            # Pivot the data to have years as columns and size classes as rows
            pivoted_data = selected_data.pivot_table(index='Size Class', columns='Year', aggfunc='size', fill_value=0)
            # Reset the index to make 'Size Class' a column
            pivoted_data = pivoted_data.reset_index()
            # Melt the pivoted DataFrame to have a long format suitable for plotting
            melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year', value_name='Count')
            # Create bar chart
            fig = px.bar(melted_data, x='Size Class', y='Count', color='Year',
                         title='Distribution of DBH Size Classes Across Selected Years',
                         labels={'Count': 'Count', 'Size Class': 'DBH Size Class', 'Year': 'Year'},
                         barmode='group')
            st.plotly_chart(fig)

        def create_bar_chart_DBH_distribution_BaslArea(df, selected_years):
            # Filter data for the selected years
            selected_data = df[df['Year'].isin(selected_years)]
            # Pivot the data to have years as columns and size classes as rows
            pivoted_data = selected_data.pivot_table(index='Size Class', columns='Year', values='Basal Area',
                                                     aggfunc='sum', fill_value=0)
            # Reset the index to make 'Size Class' a column
            pivoted_data = pivoted_data.reset_index()
            # Melt the pivoted DataFrame to have a long format suitable for plotting
            melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year', value_name='Total Basal Area')
            # Create bar chart
            fig = px.bar(melted_data, x='Size Class', y='Total Basal Area', color='Year',
                         title='Total Basal Area for Each Size Class Across Selected Years',
                         labels={'Total Basal Area': 'Total Basal Area', 'Size Class': 'DBH Size Class',
                                 'Year': 'Year'},
                         barmode='group')
            st.plotly_chart(fig)


        def create_bar_chart_DBH_distribution_Density(df, selected_years):
            # Filter data for the selected years
            selected_data = df[df['Year'].isin(selected_years)]
            # Pivot the data to have years as columns and size classes as rows
            pivoted_data = selected_data.pivot_table(index='Size Class', columns='Year', values='Density',
                                                     aggfunc='sum', fill_value=0)
            # Reset the index to make 'Size Class' a column
            pivoted_data = pivoted_data.reset_index()
            # Melt the pivoted DataFrame to have a long format suitable for plotting
            melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year', value_name='Total Density')
            # Create bar chart
            fig = px.bar(melted_data, x='Size Class', y='Total Density', color='Year',
                         title='Total Density for Each Size Class Across Selected Years',
                         labels={'Total Basal Area': 'Total Basal Area', 'Size Class': 'DBH Size Class',
                                 'Year': 'Year'},
                         barmode='group')
            st.plotly_chart(fig)





        def create_bar_chart_DBH_distribution_hectare(df, selected_years, selected_hectares):
            for year in selected_years:
                # Filter data for the selected year and hectares
                selected_data = df[(df['Year'] == year) & df['Hectare'].isin(selected_hectares)]
                # Pivot the data to have size classes as rows and hectares as columns
                pivoted_data = selected_data.pivot_table(index='Size Class', columns='Hectare', aggfunc='size',
                                                         fill_value=0)
                # Reset the index to make 'Size Class' a column
                pivoted_data = pivoted_data.reset_index()
                # Melt the pivoted DataFrame to have a long format suitable for plotting
                melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Hectare', value_name='Count')
                # Create bar chart for the current year
                fig = px.bar(melted_data, x='Size Class', y='Count', color='Hectare',
                             title=f'Distribution of DBH Size Classes for Year {year} Across Selected Hectares',
                             labels={'Count': 'Count', 'Size Class': 'DBH Size Class', 'Hectare': 'Hectare'},
                             barmode='group')
                st.plotly_chart(fig)

        def create_bar_chart_DBH_distribution_BaslArea_hectare(df, selected_years, selected_hectares):
            for year in selected_years:
                # Filter data for the selected year and hectares
                selected_data = df[(df['Year'] == year) & (df['Hectare'].isin(selected_hectares))]
                # Pivot the data to have size classes as rows and years as columns, summing basal area
                pivoted_data = selected_data.pivot_table(index='Size Class', columns='Hectare', values='Basal Area',
                                                         aggfunc='sum', fill_value=0)
                # Reset index to make 'Size Class' a column
                pivoted_data = pivoted_data.reset_index()
                # Melt the pivoted DataFrame to have a long format suitable for plotting
                melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year',
                                      value_name='Total Basal Area')
                # Create bar chart for the current year
                fig = px.bar(melted_data, x='Size Class', y='Total Basal Area', color='Year',
                             title=f'Total Basal Area for Each Size Class - Year {year}',
                             labels={'Total Basal Area': 'Total Basal Area', 'Size Class': 'DBH Size Class',
                                     'Year': 'Year'},
                             barmode='group')
                st.plotly_chart(fig)


        def create_bar_chart_DBH_distribution_Density_hectare(df, selected_years):
            for year in selected_years:
                # Filter data for the selected year and hectares
                selected_data = df[(df['Year'] == year) & (df['Hectare'].isin(selected_hectares))]
                # Pivot the data to have size classes as rows and years as columns, summing basal area
                pivoted_data = selected_data.pivot_table(index='Size Class', columns='Hectare', values='Density',
                                                         aggfunc='sum', fill_value=0)
                # Reset index to make 'Size Class' a column
                pivoted_data = pivoted_data.reset_index()
                # Melt the pivoted DataFrame to have a long format suitable for plotting
                melted_data = pd.melt(pivoted_data, id_vars='Size Class', var_name='Year',
                                      value_name='Total Density')
                # Create bar chart for the current year
                fig = px.bar(melted_data, x='Size Class', y='Total Density', color='Year',
                             title=f'Total Density for Each Size Class - Year {year}',
                             labels={'Total Density': 'TotalDensity', 'Size Class': 'DBH Size Class',
                                     'Year': 'Year'},
                             barmode='group')
                st.plotly_chart(fig)
        default_selected_years = df['Year'].unique()
        selected_years = st.sidebar.multiselect("Select Years", df['Year'].unique(), default_selected_years)
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique())

        # Streamlit UI
        col1, col2 = st.columns(2)
        with col1:
            create_bar_chart_DBH_distribution(df, selected_years)

        with col2:
            create_bar_chart_DBH_distribution_BaslArea(df, selected_years)

        col1, col2 = st.columns(2)

        with col1:
            create_bar_chart_DBH_distribution_Density(df, selected_years)

        col1, col2 = st.columns(2)
        with col1:
            create_bar_chart_DBH_distribution_hectare(df, selected_years, selected_hectares)
        with col2:
            create_bar_chart_DBH_distribution_BaslArea_hectare(df, selected_years, selected_hectares)

        create_bar_chart_DBH_distribution_Density_hectare(df, selected_years)

    if option_tomenutype == 'AGB':
        def create_bar_chart_AGB(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'AGB' for each size class
            size_class_AGB = selected_data.groupby('Size Class')['AGB'].sum().reset_index()
            # Calculate average AGB across all size classes
            average_AGB = size_class_AGB['AGB'].mean()
            # Create bar chart
            fig = px.bar(size_class_AGB, x='Size Class', y='AGB',
                         title=f'Sum of AGB Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'AGB': 'AGB'})
            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)
            # Add dashed line for average AGB
            fig.add_shape(type='line', x0=size_class_AGB['Size Class'].iloc[0], y0=average_AGB,
                          x1=size_class_AGB['Size Class'].iloc[-1], y1=average_AGB,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total AGB Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_AGB(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative AGB values
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Size Class' and calculate sum of 'AGB' for each size class
            size_class_AGB = selected_data.groupby('Size Class')['AGB'].sum().reset_index()

            # Calculate total AGB
            total_AGB = size_class_AGB['AGB'].sum()

            # Create pie chart
            fig = px.pie(size_class_AGB, values='AGB', names='Size Class',
                         title=f'Total AGB Across Size Classes for Year {selected_year}',
                         labels={'AGB': 'AGB', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for AGB distribution across size classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_AGB_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'AGB' for each size class
            size_class_AGB_rate = selected_data.groupby('Size Class')['AGB'].mean().reset_index()
            # Calculate average AGB across all size classes
            average_AGB_rate = size_class_AGB_rate['AGB'].mean()
            # Create bar chart
            fig = px.bar(size_class_AGB_rate, x='Size Class', y='AGB',
                         title=f'Average AGB Across Size Classes for Year {selected_year}')
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average AGB
            fig.add_shape(type='line', x0=-0.5, y0=average_AGB_rate, x1=len(size_class_AGB_rate) - 0.5,
                          y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average AGB Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_AGB_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative AGB values
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Size Class' and calculate average 'AGB' for each size class
            size_class_AGB_rate = selected_data.groupby('Size Class')['AGB'].mean().reset_index()

            # Calculate average AGB across all size classes
            average_AGB_rate = size_class_AGB_rate['AGB'].mean()

            # Create pie chart
            fig = px.pie(size_class_AGB_rate, values='AGB', names='Size Class',
                         title=f'Average AGB Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_AGB_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'AGB' for each age class
            age_class_AGB = selected_data.groupby('Age Class')['AGB'].mean().reset_index()
            # Calculate average AGB across all age classes
            average_AGB = age_class_AGB['AGB'].mean()
            # Create bar chart
            fig = px.bar(age_class_AGB, x='Age Class', y='AGB',
                         title=f'Average AGB Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average AGB
            fig.add_shape(type='line', x0=-0.5, y0=average_AGB, x1=len(age_class_AGB) - 0.5, y1=average_AGB,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total AGB Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_AGB_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative AGB values
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Age Class' and calculate average 'AGB' for each age class
            age_class_AGB = selected_data.groupby('Age Class')['AGB'].mean().reset_index()

            # Calculate average AGB across all age classes
            average_AGB = age_class_AGB['AGB'].mean()

            # Create pie chart
            fig = px.pie(age_class_AGB, values='AGB', names='Age Class',
                         title=f'Average AGB Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for average AGB across age classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_AGB_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'AGB' for each age class
            age_class_AGB_rate = selected_data.groupby('Age Class')['AGB'].mean().reset_index()
            # Calculate average AGB across all age classes
            average_AGB_rate = age_class_AGB_rate['AGB'].mean()
            # Create bar chart
            fig = px.bar(age_class_AGB_rate, x='Age Class', y='AGB',
                         title=f'Average AGB Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average AGB
            fig.add_shape(type='line', x0=-0.5, y0=average_AGB_rate, x1=len(age_class_AGB_rate) - 0.5,
                          y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average AGB Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_AGB_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative AGB values
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Age Class' and calculate average 'AGB' for each age class
            age_class_AGB_rate = selected_data.groupby('Age Class')['AGB'].mean().reset_index()

            # Calculate average AGB across all age classes
            average_AGB_rate = age_class_AGB_rate['AGB'].mean()

            # Create pie chart
            fig = px.pie(age_class_AGB_rate, values='AGB', names='Age Class',
                         title=f'Average AGB Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_AGB_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB = selected_data.groupby('Age Class')['AGB'].mean().reset_index()

                # Calculate average AGB across all age classes
                average_AGB = age_class_AGB['AGB'].mean()

                # Filter out negative AGB values
                age_class_AGB = age_class_AGB[age_class_AGB['AGB'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_AGB, values='AGB', names='Age Class',
                             title=f'Total AGB Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_AGB_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB = selected_data.groupby('Age Class')['AGB'].mean().reset_index()
                # Calculate average AGB across all age classes
                average_AGB = age_class_AGB['AGB'].mean()
                # Create bar chart
                fig = px.bar(age_class_AGB, x='Age Class', y='AGB',
                             title=f'Sum of AGB Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average AGB
                fig.add_shape(type='line', x0=-0.5, y0=average_AGB, x1=len(age_class_AGB) - 0.5, y1=average_AGB,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total AGB Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average AGB across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_AGB_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB_rate = selected_data.groupby('Age Class')['AGB'].mean().reset_index()

                # Calculate average AGB across all age classes
                average_AGB_rate = age_class_AGB_rate['AGB'].mean()

                # Filter out negative AGB values
                age_class_AGB_rate = age_class_AGB_rate[age_class_AGB_rate['AGB'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_AGB_rate, values='AGB', names='Age Class',
                             title=f'Average AGB Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_AGB_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB_rate = selected_data.groupby('Age Class')['AGB'].mean().reset_index()
                # Calculate average AGB across all age classes
                average_AGB_rate = age_class_AGB_rate['AGB'].mean()
                # Create bar chart
                fig = px.bar(age_class_AGB_rate, x='Age Class', y='AGB',
                             title=f'Average AGB Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average AGB
                fig.add_shape(type='line', x0=-0.5, y0=average_AGB_rate, x1=len(age_class_AGB_rate) - 0.5,
                              y1=average_AGB_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average AGB Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_AGB_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative AGB values
                selected_data = selected_data[selected_data['AGB'] >= 0]

                # Group by 'Size Class' and calculate average 'AGB' for each size class
                size_class_AGB = selected_data.groupby('Size Class')['AGB'].mean().reset_index()

                # Calculate average AGB across all size classes
                average_AGB = size_class_AGB['AGB'].mean()

                # Create pie chart
                fig = px.pie(size_class_AGB, values='AGB', names='Size Class',
                             title=f'Average AGB Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_AGB_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB = selected_data.groupby('Size Class')['AGB'].mean().reset_index()
                # Calculate average AGB across all age classes
                average_AGB = age_class_AGB['AGB'].mean()
                # Create bar chart
                fig = px.bar(age_class_AGB, x='Size Class', y='AGB',
                             title=f'Average AGB Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average AGB
                fig.add_shape(type='line', x0=-0.5, y0=average_AGB, x1=len(age_class_AGB) - 0.5, y1=average_AGB,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total AGB Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average AGB across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_AGB_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative AGB values
                selected_data = selected_data[selected_data['AGB'] >= 0]

                # Group by 'Size Class' and calculate average 'AGB' for each size class
                size_class_AGB_rate = selected_data.groupby('Size Class')['AGB'].mean().reset_index()

                # Calculate average AGB across all size classes
                average_AGB_rate = size_class_AGB_rate['AGB'].mean()

                # Create pie chart
                fig = px.pie(size_class_AGB_rate, values='AGB', names='Size Class',
                             title=f'Average AGB Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_AGB_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'AGB' for each age class
                age_class_AGB_rate = selected_data.groupby('Size Class')['AGB'].mean().reset_index()
                # Calculate average AGB across all age classes
                average_AGB_rate = age_class_AGB_rate['AGB'].mean()
                # Create bar chart
                fig = px.bar(age_class_AGB_rate, x='Size Class', y='AGB',
                             title=f'Average AGB Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average AGB
                fig.add_shape(type='line', x0=-0.5, y0=average_AGB_rate, x1=len(age_class_AGB_rate) - 0.5,
                              y1=average_AGB_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average AGB Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Hectare' and 'Species' and calculate mean 'AGB' for each species in each hectare
            species_AGB_rate = selected_data.groupby(['Hectare', 'Species'])['AGB'].mean().reset_index()
            # Sort by 'AGB' in descending order within each hectare
            species_AGB_rate['Rank'] = species_AGB_rate.groupby('Hectare')['AGB'].rank(ascending=False)
            top_species = species_AGB_rate[species_AGB_rate['Rank'] <= 5]  # Select top 5 species in each hectare
            # Calculate average AGB across all species
            average_AGB_rate = top_species['AGB'].mean()
            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='AGB', color='Species',
                         title=f'Top 5 Species with Highest AGBs for Each Hectare - Year {selected_year}',
                         labels={'AGB': 'Mean AGB', 'Hectare': 'Hectare'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_AGB_rate,
                          x1=max(top_species['Hectare']), y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mean 'AGB' for each species in each hectare
            species_AGB_rate = selected_data.groupby(['Hectare', 'Species'])['AGB'].mean().reset_index()

            # Sort by 'AGB' in descending order within each hectare
            species_AGB_rate['Rank'] = species_AGB_rate.groupby('Hectare')['AGB'].rank(ascending=False)
            top_species = species_AGB_rate[species_AGB_rate['Rank'] <= 5]  # Select top 5 species in each hectare

            # Exclude negative AGBs
            top_species = top_species[top_species['AGB'] >= 0]

            # Calculate average AGB across all species
            average_AGB_rate = top_species['AGB'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='AGB', names='Species',
                         title=f'Top 5 Species with Highest AGBs for Each Hectare - Year {selected_year}',
                         labels={'AGB': 'Mean AGB', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average AGB: {average_AGB_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]
            # Group by 'Year' and 'Species' and calculate mean 'AGB' for each species in each year
            species_AGB_rate = selected_data.groupby(['Year', 'Species'])['AGB'].mean().reset_index()
            # Calculate average AGB across all years for selected species
            average_AGB_rate = species_AGB_rate['AGB'].mean()
            # Create bar chart
            fig = px.bar(species_AGB_rate, x='Year', y='AGB', color='Species',
                         title='Mean AGB of Selected Species Across Years',
                         labels={'AGB': 'Mean AGB', 'Year': 'Year'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(species_AGB_rate['Year']), y0=average_AGB_rate,
                          x1=max(species_AGB_rate['Year']), y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Filter out negative AGBs
            selected_data = selected_data[selected_data['AGB'] >= 0]

            # Group by 'Year' and 'Species' and calculate mean 'AGB' for each species in each year
            species_AGB_rate = selected_data.groupby(['Year', 'Species'])['AGB'].mean().reset_index()

            # Calculate average AGB across all years for selected species
            average_AGB_rate = species_AGB_rate['AGB'].mean()

            # Create pie chart
            fig = px.pie(species_AGB_rate, values='AGB', names='Species',
                         title='Mean AGB of Selected Species Across Years',
                         labels={'AGB': 'Mean AGB', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average AGB: {average_AGB_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_AGBrate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'AGB' for each DBH size class in each year
            dbh_AGB_rate = df.groupby(['Year', 'Size Class'])['AGB'].mean().reset_index()
            # Calculate average AGB across all years
            average_AGB_rate = dbh_AGB_rate['AGB'].mean()
            # Create bar chart
            fig = px.bar(dbh_AGB_rate, x='Year', y='AGB', color='Size Class',
                         title='Mean AGB for Each DBH Size Class Across Years',
                         labels={'AGB': 'Mean AGB', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_AGB_rate['Year']), y0=average_AGB_rate,
                          x1=max(dbh_AGB_rate['Year']), y1=average_AGB_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_AGBrate(df):
            # Group by 'DBH Size Class' and calculate mean 'AGB' for each DBH size class across all years
            dbh_AGB_rate = df.groupby('Size Class')['AGB'].mean().reset_index()

            # Calculate average AGB across all size classes
            average_AGB_rate = dbh_AGB_rate['AGB'].mean()

            # Create pie chart
            fig = px.pie(dbh_AGB_rate, values='AGB', names='Size Class',
                         title='Mean AGB for Each DBH Size Class Across Years',
                         labels={'AGB': 'Mean AGB', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average AGB: {average_AGB_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_AGB(df):
            # Group by 'Year' and 'DBH Size Class' and calculate sum 'AGB' for each DBH size class in each year
            dbh_AGB = df.groupby(['Year', 'Size Class'])['AGB'].sum().reset_index()
            # Calculate average AGB across all years
            average_AGB = dbh_AGB['AGB'].mean()
            # Create bar chart
            fig = px.bar(dbh_AGB, x='Year', y='AGB', color='Size Class',
                         title='Sum AGB for Each DBH Size Class Across Years',
                         labels={'AGB': 'Sum AGB', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_AGB['Year']), y0=average_AGB,
                          x1=max(dbh_AGB['Year']), y1=average_AGB,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),
                                                   default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique(),
                                                  default=['CANAPA', 'PAYELU', 'SHORP2'])

        # -----------------------------------------

        # --------- Most SP
        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_AGB(df)
            with st.expander("AGB Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("AGB Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_AGB(df, selected_year)
                with col2:
                    create_bar_chart_AGB_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_AGB_age(df, selected_year)
                with col2:
                    create_bar_chart_AGB_rate_age(df, selected_year)

            with st.expander("AGB Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_AGB_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_AGB_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_AGB_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_AGB_rate_hectare_age(df, selected_hectares)

        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col2:
                create_bar_chart_BDH_all_years_AGB(df)
            with st.expander("AGB Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("AGB Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_AGB(df, selected_year)
                with col2:
                    create_pie_chart_AGB_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_AGB_age(df, selected_year)
                with col2:
                    create_pie_chart_AGB_rate_age(df, selected_year)

            with st.expander("AGB Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_AGB_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_AGB_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_AGB_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_AGB_rate_hectare_age(df, selected_hectares)

    if option_tomenutype == 'Carbon stock':
        st.write("asdasd")
        def create_bar_chart_Carbon(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Carbon' for each size class
            size_class_Carbon = selected_data.groupby('Size Class')['Carbon'].sum().reset_index()
            # Calculate average Carbon across all size classes
            average_Carbon = size_class_Carbon['Carbon'].mean()
            # Create bar chart
            fig = px.bar(size_class_Carbon, x='Size Class', y='Carbon',
                         title=f'Sum of Carbon Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'Carbon': 'Carbon'})
            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)
            # Add dashed line for average Carbon
            fig.add_shape(type='line', x0=size_class_Carbon['Size Class'].iloc[0], y0=average_Carbon,
                          x1=size_class_Carbon['Size Class'].iloc[-1], y1=average_Carbon,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Carbon Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Carbon(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Carbon values
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Size Class' and calculate sum of 'Carbon' for each size class
            size_class_Carbon = selected_data.groupby('Size Class')['Carbon'].sum().reset_index()

            # Calculate total Carbon
            total_Carbon = size_class_Carbon['Carbon'].sum()

            # Create pie chart
            fig = px.pie(size_class_Carbon, values='Carbon', names='Size Class',
                         title=f'Total Carbon Across Size Classes for Year {selected_year}',
                         labels={'Carbon': 'Carbon', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for Carbon distribution across size classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Carbon_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Carbon' for each size class
            size_class_Carbon_rate = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()
            # Calculate average Carbon across all size classes
            average_Carbon_rate = size_class_Carbon_rate['Carbon'].mean()
            # Create bar chart
            fig = px.bar(size_class_Carbon_rate, x='Size Class', y='Carbon',
                         title=f'Average Carbon Across Size Classes for Year {selected_year}')
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average Carbon
            fig.add_shape(type='line', x0=-0.5, y0=average_Carbon_rate, x1=len(size_class_Carbon_rate) - 0.5,
                          y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Carbon Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Carbon_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Carbon values
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Size Class' and calculate average 'Carbon' for each size class
            size_class_Carbon_rate = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()

            # Calculate average Carbon across all size classes
            average_Carbon_rate = size_class_Carbon_rate['Carbon'].mean()

            # Create pie chart
            fig = px.pie(size_class_Carbon_rate, values='Carbon', names='Size Class',
                         title=f'Average Carbon Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Carbon_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Carbon' for each age class
            age_class_Carbon = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()
            # Calculate average Carbon across all age classes
            average_Carbon = age_class_Carbon['Carbon'].mean()
            # Create bar chart
            fig = px.bar(age_class_Carbon, x='Age Class', y='Carbon',
                         title=f'Average Carbon Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average Carbon
            fig.add_shape(type='line', x0=-0.5, y0=average_Carbon, x1=len(age_class_Carbon) - 0.5, y1=average_Carbon,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Carbon Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Carbon_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Carbon values
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Age Class' and calculate average 'Carbon' for each age class
            age_class_Carbon = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()

            # Calculate average Carbon across all age classes
            average_Carbon = age_class_Carbon['Carbon'].mean()

            # Create pie chart
            fig = px.pie(age_class_Carbon, values='Carbon', names='Age Class',
                         title=f'Average Carbon Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for average Carbon across age classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Carbon_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Carbon' for each age class
            age_class_Carbon_rate = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()
            # Calculate average Carbon across all age classes
            average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()
            # Create bar chart
            fig = px.bar(age_class_Carbon_rate, x='Age Class', y='Carbon',
                         title=f'Average Carbon Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average Carbon
            fig.add_shape(type='line', x0=-0.5, y0=average_Carbon_rate, x1=len(age_class_Carbon_rate) - 0.5,
                          y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Carbon Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Carbon_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Carbon values
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Age Class' and calculate average 'Carbon' for each age class
            age_class_Carbon_rate = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()

            # Calculate average Carbon across all age classes
            average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()

            # Create pie chart
            fig = px.pie(age_class_Carbon_rate, values='Carbon', names='Age Class',
                         title=f'Average Carbon Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Carbon_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()

                # Calculate average Carbon across all age classes
                average_Carbon = age_class_Carbon['Carbon'].mean()

                # Filter out negative Carbon values
                age_class_Carbon = age_class_Carbon[age_class_Carbon['Carbon'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_Carbon, values='Carbon', names='Age Class',
                             title=f'Total Carbon Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Carbon_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()
                # Calculate average Carbon across all age classes
                average_Carbon = age_class_Carbon['Carbon'].mean()
                # Create bar chart
                fig = px.bar(age_class_Carbon, x='Age Class', y='Carbon',
                             title=f'Sum of Carbon Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average Carbon
                fig.add_shape(type='line', x0=-0.5, y0=average_Carbon, x1=len(age_class_Carbon) - 0.5,
                              y1=average_Carbon,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Carbon Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average Carbon across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Carbon_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon_rate = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()

                # Calculate average Carbon across all age classes
                average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()

                # Filter out negative Carbon values
                age_class_Carbon_rate = age_class_Carbon_rate[age_class_Carbon_rate['Carbon'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_Carbon_rate, values='Carbon', names='Age Class',
                             title=f'Average Carbon Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Carbon_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon_rate = selected_data.groupby('Age Class')['Carbon'].mean().reset_index()
                # Calculate average Carbon across all age classes
                average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()
                # Create bar chart
                fig = px.bar(age_class_Carbon_rate, x='Age Class', y='Carbon',
                             title=f'Average Carbon Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average Carbon
                fig.add_shape(type='line', x0=-0.5, y0=average_Carbon_rate, x1=len(age_class_Carbon_rate) - 0.5,
                              y1=average_Carbon_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Carbon Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Carbon_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative Carbon values
                selected_data = selected_data[selected_data['Carbon'] >= 0]

                # Group by 'Size Class' and calculate average 'Carbon' for each size class
                size_class_Carbon = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()

                # Calculate average Carbon across all size classes
                average_Carbon = size_class_Carbon['Carbon'].mean()

                # Create pie chart
                fig = px.pie(size_class_Carbon, values='Carbon', names='Size Class',
                             title=f'Average Carbon Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Carbon_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()
                # Calculate average Carbon across all age classes
                average_Carbon = age_class_Carbon['Carbon'].mean()
                # Create bar chart
                fig = px.bar(age_class_Carbon, x='Size Class', y='Carbon',
                             title=f'Average Carbon Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average Carbon
                fig.add_shape(type='line', x0=-0.5, y0=average_Carbon, x1=len(age_class_Carbon) - 0.5,
                              y1=average_Carbon,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Carbon Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average Carbon across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Carbon_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative Carbon values
                selected_data = selected_data[selected_data['Carbon'] >= 0]

                # Group by 'Size Class' and calculate average 'Carbon' for each size class
                size_class_Carbon_rate = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()

                # Calculate average Carbon across all size classes
                average_Carbon_rate = size_class_Carbon_rate['Carbon'].mean()

                # Create pie chart
                fig = px.pie(size_class_Carbon_rate, values='Carbon', names='Size Class',
                             title=f'Average Carbon Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Carbon_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Carbon' for each age class
                age_class_Carbon_rate = selected_data.groupby('Size Class')['Carbon'].mean().reset_index()
                # Calculate average Carbon across all age classes
                average_Carbon_rate = age_class_Carbon_rate['Carbon'].mean()
                # Create bar chart
                fig = px.bar(age_class_Carbon_rate, x='Size Class', y='Carbon',
                             title=f'Average Carbon Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average Carbon
                fig.add_shape(type='line', x0=-0.5, y0=average_Carbon_rate, x1=len(age_class_Carbon_rate) - 0.5,
                              y1=average_Carbon_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Carbon Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Hectare' and 'Species' and calculate mean 'Carbon' for each species in each hectare
            species_Carbon_rate = selected_data.groupby(['Hectare', 'Species'])['Carbon'].mean().reset_index()
            # Sort by 'Carbon' in descending order within each hectare
            species_Carbon_rate['Rank'] = species_Carbon_rate.groupby('Hectare')['Carbon'].rank(ascending=False)
            top_species = species_Carbon_rate[species_Carbon_rate['Rank'] <= 5]  # Select top 5 species in each hectare
            # Calculate average Carbon across all species
            average_Carbon_rate = top_species['Carbon'].mean()
            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='Carbon', color='Species',
                         title=f'Top 5 Species with Highest Carbons for Each Hectare - Year {selected_year}',
                         labels={'Carbon': 'Mean Carbon', 'Hectare': 'Hectare'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_Carbon_rate,
                          x1=max(top_species['Hectare']), y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mean 'Carbon' for each species in each hectare
            species_Carbon_rate = selected_data.groupby(['Hectare', 'Species'])['Carbon'].mean().reset_index()

            # Sort by 'Carbon' in descending order within each hectare
            species_Carbon_rate['Rank'] = species_Carbon_rate.groupby('Hectare')['Carbon'].rank(ascending=False)
            top_species = species_Carbon_rate[species_Carbon_rate['Rank'] <= 5]  # Select top 5 species in each hectare

            # Exclude negative Carbons
            top_species = top_species[top_species['Carbon'] >= 0]

            # Calculate average Carbon across all species
            average_Carbon_rate = top_species['Carbon'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='Carbon', names='Species',
                         title=f'Top 5 Species with Highest Carbons for Each Hectare - Year {selected_year}',
                         labels={'Carbon': 'Mean Carbon', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Carbon: {average_Carbon_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]
            # Group by 'Year' and 'Species' and calculate mean 'Carbon' for each species in each year
            species_Carbon_rate = selected_data.groupby(['Year', 'Species'])['Carbon'].mean().reset_index()
            # Calculate average Carbon across all years for selected species
            average_Carbon_rate = species_Carbon_rate['Carbon'].mean()
            # Create bar chart
            fig = px.bar(species_Carbon_rate, x='Year', y='Carbon', color='Species',
                         title='Mean Carbon of Selected Species Across Years',
                         labels={'Carbon': 'Mean Carbon', 'Year': 'Year'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(species_Carbon_rate['Year']), y0=average_Carbon_rate,
                          x1=max(species_Carbon_rate['Year']), y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Filter out negative Carbons
            selected_data = selected_data[selected_data['Carbon'] >= 0]

            # Group by 'Year' and 'Species' and calculate mean 'Carbon' for each species in each year
            species_Carbon_rate = selected_data.groupby(['Year', 'Species'])['Carbon'].mean().reset_index()

            # Calculate average Carbon across all years for selected species
            average_Carbon_rate = species_Carbon_rate['Carbon'].mean()

            # Create pie chart
            fig = px.pie(species_Carbon_rate, values='Carbon', names='Species',
                         title='Mean Carbon of Selected Species Across Years',
                         labels={'Carbon': 'Mean Carbon', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Carbon: {average_Carbon_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_Carbonrate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'Carbon' for each DBH size class in each year
            dbh_Carbon_rate = df.groupby(['Year', 'Size Class'])['Carbon'].mean().reset_index()
            # Calculate average Carbon across all years
            average_Carbon_rate = dbh_Carbon_rate['Carbon'].mean()
            # Create bar chart
            fig = px.bar(dbh_Carbon_rate, x='Year', y='Carbon', color='Size Class',
                         title='Mean Carbon for Each DBH Size Class Across Years',
                         labels={'Carbon': 'Mean Carbon', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_Carbon_rate['Year']), y0=average_Carbon_rate,
                          x1=max(dbh_Carbon_rate['Year']), y1=average_Carbon_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_Carbonrate(df):
            # Group by 'DBH Size Class' and calculate mean 'Carbon' for each DBH size class across all years
            dbh_Carbon_rate = df.groupby('Size Class')['Carbon'].mean().reset_index()

            # Calculate average Carbon across all size classes
            average_Carbon_rate = dbh_Carbon_rate['Carbon'].mean()

            # Create pie chart
            fig = px.pie(dbh_Carbon_rate, values='Carbon', names='Size Class',
                         title='Mean Carbon for Each DBH Size Class Across Years',
                         labels={'Carbon': 'Mean Carbon', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Carbon: {average_Carbon_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_Carbon(df):
            # Group by 'Year' and 'DBH Size Class' and calculate sum 'Carbon' for each DBH size class in each year
            dbh_Carbon = df.groupby(['Year', 'Size Class'])['Carbon'].sum().reset_index()
            # Calculate average Carbon across all years
            average_Carbon = dbh_Carbon['Carbon'].mean()
            # Create bar chart
            fig = px.bar(dbh_Carbon, x='Year', y='Carbon', color='Size Class',
                         title='Sum Carbon for Each DBH Size Class Across Years',
                         labels={'Carbon': 'Sum Carbon', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_Carbon['Year']), y0=average_Carbon,
                          x1=max(dbh_Carbon['Year']), y1=average_Carbon,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),
                                                   default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique(),
                                                  default=['CANAPA', 'PAYELU', 'SHORP2'])

        # -----------------------------------------

        # --------- Most SP
        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_Carbon(df)
            with st.expander("Carbon Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("Carbon Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Carbon(df, selected_year)
                with col2:
                    create_bar_chart_Carbon_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Carbon_age(df, selected_year)
                with col2:
                    create_bar_chart_Carbon_rate_age(df, selected_year)

            with st.expander("Carbon Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Carbon_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_Carbon_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Carbon_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_Carbon_rate_hectare_age(df, selected_hectares)

        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col2:
                create_bar_chart_BDH_all_years_Carbon(df)
            with st.expander("Carbon Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("Carbon Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Carbon(df, selected_year)
                with col2:
                    create_pie_chart_Carbon_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Carbon_age(df, selected_year)
                with col2:
                    create_pie_chart_Carbon_rate_age(df, selected_year)

            with st.expander("Carbon Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Carbon_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_Carbon_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Carbon_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_Carbon_rate_hectare_age(df, selected_hectares)



    if option_tomenutype == 'Mortality':


        def calculate_mortality_rate(selected_data):
            total_trees = selected_data.shape[0]
            dead_trees = selected_data[selected_data['Status'] == 'Dead'].shape[0]
            if total_trees == 0:
                return 0
            mortality_rate = (dead_trees / total_trees) * 100
            return mortality_rate

        def create_bar_chart_mortality(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Size Class' and calculate mortality rate for each size class
            size_class_mortality = selected_data.groupby('Size Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all size classes
            average_mortality_rate = size_class_mortality['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(size_class_mortality, x='Size Class', y='Mortality Rate',
                         title=f'Mortality Rate Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'Mortality Rate': 'Mortality Rate (%)'})

            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average mortality rate
            fig.add_shape(type='line', x0=size_class_mortality['Size Class'].iloc[0], y0=average_mortality_rate,
                          x1=size_class_mortality['Size Class'].iloc[-1], y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Mortality Rate Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Size Class' and calculate the count of dead trees for each size class
            size_class_mortality = selected_data[selected_data['Status'] == 'Dead'].groupby('Size Class')[
                'Status'].count().reset_index()
            size_class_mortality.rename(columns={'Status': 'Count'}, inplace=True)

            # Calculate total mortality
            total_mortality = size_class_mortality['Count'].sum()

            # Create pie chart
            fig = px.pie(size_class_mortality, values='Count', names='Size Class',
                         title=f'Mortality Distribution Across Size Classes for Year {selected_year}',
                         labels={'Count': 'Count', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_mortality_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Size Class' and calculate mortality rate for each size class
            size_class_mortality_rate = selected_data.groupby('Size Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all size classes
            average_mortality_rate = size_class_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(size_class_mortality_rate, x='Size Class', y='Mortality Rate',
                         title=f'Average Mortality Rate Across Size Classes for Year {selected_year}')

            # Customize bar appearance
            fig.update_traces(marker_color='red', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average mortality rate
            fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(size_class_mortality_rate) - 0.5,
                          y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Mortality Rate Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Size Class' and calculate the count of dead trees for each size class
            size_class_mortality = selected_data[selected_data['Status'] == 'Dead'].groupby('Size Class')[
                'Status'].count().reset_index()
            size_class_mortality.rename(columns={'Status': 'Count'}, inplace=True)

            # Calculate total mortality
            total_mortality = size_class_mortality['Count'].sum()

            # Create pie chart
            fig = px.pie(size_class_mortality, values='Count', names='Size Class',
                         title=f'Mortality Distribution Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_mortality_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Age Class' and calculate mortality rate for each age class
            age_class_mortality_rate = selected_data.groupby('Age Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all age classes
            average_mortality_rate = age_class_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(age_class_mortality_rate, x='Age Class', y='Mortality Rate',
                         title=f'Average Mortality Rate Across Age Classes for Year {selected_year}')

            # Change bar color and size
            fig.update_traces(marker_color='darkred', marker_line_color='black', marker_line_width=1.3, opacity=0.7)

            # Add dashed line for average mortality rate
            fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(age_class_mortality_rate) - 0.5,
                          y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Mortality Rate Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Age Class' and calculate the count of dead trees for each age class
            age_class_mortality = selected_data[selected_data['Status'] == 'Dead'].groupby('Age Class')[
                'Status'].count().reset_index()
            age_class_mortality.rename(columns={'Status': 'Count'}, inplace=True)

            # Create pie chart
            fig = px.pie(age_class_mortality, values='Count', names='Age Class',
                         title=f'Mortality Distribution Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_mortality_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Age Class' and calculate mortality rate for each age class
            age_class_mortality_rate = selected_data.groupby('Age Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all age classes
            average_mortality_rate = age_class_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(age_class_mortality_rate, x='Age Class', y='Mortality Rate',
                         title=f'Average Mortality Rate Across Age Classes for Year {selected_year}')

            # Change bar color and size
            fig.update_traces(marker_color='darkred', marker_line_color='black', marker_line_width=1.3, opacity=0.7)

            # Add dashed line for average mortality rate
            fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(age_class_mortality_rate) - 0.5,
                          y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Mortality Rate Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Age Class' and calculate mortality rate for each age class
            age_class_mortality_rate = selected_data.groupby('Age Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Create pie chart
            fig = px.pie(age_class_mortality_rate, values='Mortality Rate', names='Age Class',
                         title=f'Mortality Rate Distribution Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_mortality_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate mortality rate for each age class
                age_class_mortality_rate = selected_data.groupby('Age Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Create pie chart
                fig = px.pie(age_class_mortality_rate, values='Mortality Rate', names='Age Class',
                             title=f'Mortality Rate Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_mortality_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate mortality rate for each age class
                age_class_mortality_rate = selected_data.groupby('Age Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Calculate average mortality rate across all age classes
                average_mortality_rate = age_class_mortality_rate['Mortality Rate'].mean()

                # Create bar chart
                fig = px.bar(age_class_mortality_rate, x='Age Class', y='Mortality Rate',
                             title=f'Mortality Rate Across Age Classes for Hectare {hectare}')

                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)

                # Add dashed line for average mortality rate
                fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(age_class_mortality_rate) - 0.5,
                              y1=average_mortality_rate,
                              line=dict(color="black", width=1, dash='dash'))

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Mortality Rate Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)

        def create_pie_chart_mortality_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate mortality rate for each age class
                age_class_mortality_rate = selected_data.groupby('Age Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Create pie chart
                fig = px.pie(age_class_mortality_rate, values='Mortality Rate', names='Age Class',
                             title=f'Mortality Rate Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_mortality_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate mortality rate for each age class
                age_class_mortality_rate = selected_data.groupby('Age Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Calculate average mortality rate across all age classes
                average_mortality_rate = age_class_mortality_rate['Mortality Rate'].mean()

                # Create bar chart
                fig = px.bar(age_class_mortality_rate, x='Age Class', y='Mortality Rate',
                             title=f'Mortality Rate Across Age Classes for Hectare {hectare}')

                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)

                # Add dashed line for average mortality rate
                fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(age_class_mortality_rate) - 0.5,
                              y1=average_mortality_rate, line=dict(color="black", width=1, dash='dash'))

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Mortality Rate Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)

        def create_pie_chart_mortality_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Size Class' and calculate mortality rate for each size class
                size_class_mortality_rate = selected_data.groupby('Size Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Create pie chart
                fig = px.pie(size_class_mortality_rate, values='Mortality Rate', names='Size Class',
                             title=f'Mortality Rate Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_mortality_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Size Class' and calculate mortality rate for each size class
                size_class_mortality_rate = selected_data.groupby('Size Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Calculate average mortality rate across all size classes
                average_mortality_rate = size_class_mortality_rate['Mortality Rate'].mean()

                # Create bar chart
                fig = px.bar(size_class_mortality_rate, x='Size Class', y='Mortality Rate',
                             title=f'Mortality Rate Across Size Classes for Hectare {hectare}')

                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)

                # Add dashed line for average mortality rate
                fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(size_class_mortality_rate) - 0.5,
                              y1=average_mortality_rate,
                              line=dict(color="black", width=1, dash='dash'))

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Mortality Rate Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)

        def create_pie_chart_mortality_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Size Class' and calculate mortality rate for each size class
                size_class_mortality_rate = selected_data.groupby('Size Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Create pie chart
                fig = px.pie(size_class_mortality_rate, values='Mortality Rate', names='Size Class',
                             title=f'Mortality Rate Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)

        def create_bar_chart_mortality_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Size Class' and calculate mortality rate for each size class
                size_class_mortality_rate = selected_data.groupby('Size Class').apply(
                    calculate_mortality_rate).reset_index(name='Mortality Rate')

                # Calculate average mortality rate across all size classes
                average_mortality_rate = size_class_mortality_rate['Mortality Rate'].mean()

                # Create bar chart
                fig = px.bar(size_class_mortality_rate, x='Size Class', y='Mortality Rate',
                             title=f'Mortality Rate Across Size Classes for Hectare {hectare}')

                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)

                # Add dashed line for average mortality rate
                fig.add_shape(type='line', x0=-0.5, y0=average_mortality_rate, x1=len(size_class_mortality_rate) - 0.5,
                              y1=average_mortality_rate,
                              line=dict(color="black", width=1, dash='dash'))

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Mortality Rate Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)

        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mortality rate for each species in each hectare
            species_mortality_rate = selected_data.groupby(['Hectare', 'Species']).apply(
                calculate_mortality_rate).reset_index(name='Mortality Rate')

            # Sort by 'Mortality Rate' in descending order within each hectare
            species_mortality_rate['Rank'] = species_mortality_rate.groupby('Hectare')['Mortality Rate'].rank(
                ascending=False)

            # Select top 5 species in each hectare
            top_species = species_mortality_rate[species_mortality_rate['Rank'] <= 5]

            # Calculate average mortality rate across all top species
            average_mortality_rate = top_species['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='Mortality Rate', color='Species',
                         title=f'Top 5 Species with Highest Mortality Rates for Each Hectare - Year {selected_year}',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Hectare': 'Hectare'},
                         barmode='group')

            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_mortality_rate,
                          x1=max(top_species['Hectare']), y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            st.plotly_chart(fig)

        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mortality rate for each species in each hectare
            species_mortality_rate = selected_data.groupby(['Hectare', 'Species']).apply(
                calculate_mortality_rate).reset_index(name='Mortality Rate')

            # Sort by 'Mortality Rate' in descending order within each hectare
            species_mortality_rate['Rank'] = species_mortality_rate.groupby('Hectare')['Mortality Rate'].rank(
                ascending=False)

            # Select top 5 species in each hectare
            top_species = species_mortality_rate[species_mortality_rate['Rank'] <= 5]

            # Calculate average mortality rate across all top species
            average_mortality_rate = top_species['Mortality Rate'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='Mortality Rate', names='Species',
                         title=f'Top 5 Species with Highest Mortality Rates for Each Hectare - Year {selected_year}',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Species': 'Species'},
                         hole=0.3)

            # Add average annotation
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Mortality Rate: {average_mortality_rate:.2f}%',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Group by 'Year' and 'Species' and calculate mortality rate for each species in each year
            species_mortality_rate = selected_data.groupby(['Year', 'Species']).apply(
                calculate_mortality_rate).reset_index(name='Mortality Rate')

            # Calculate average mortality rate across all years for selected species
            average_mortality_rate = species_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(species_mortality_rate, x='Year', y='Mortality Rate', color='Species',
                         title='Mean Mortality Rate of Selected Species Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Year': 'Year'},
                         barmode='group')

            # Add average line
            fig.add_shape(type='line', x0=min(species_mortality_rate['Year']), y0=average_mortality_rate,
                          x1=max(species_mortality_rate['Year']), y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Update layout
            fig.update_layout(
                height=500,
                width=700,
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Group by 'Year' and 'Species' and calculate mortality rate for each species in each year
            species_mortality_rate = selected_data.groupby(['Year', 'Species']).apply(
                calculate_mortality_rate).reset_index(name='Mortality Rate')

            # Calculate average mortality rate across all years for selected species
            average_mortality_rate = species_mortality_rate['Mortality Rate'].mean()

            # Create pie chart
            fig = px.pie(species_mortality_rate, values='Mortality Rate', names='Species',
                         title='Mean Mortality Rate of Selected Species Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Mortality Rate: {average_mortality_rate:.2f}%',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def calculate_mortality(group):
            return group[group['Status'] == 'Dead'].shape[0]

        def create_bar_chart_BDH_all_years_mortality(df):
            # Group by 'Year' and 'Size Class' and calculate mortality rate for each DBH size class in each year
            dbh_mortality_rate = df.groupby(['Year', 'Size Class']).apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all years
            average_mortality_rate = dbh_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(dbh_mortality_rate, x='Year', y='Mortality Rate', color='Size Class',
                         title='Mean Mortality Rate for Each DBH Size Class Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate (%)', 'Year': 'Year',
                                 'Size Class': 'Size Class'},
                         barmode='group')

            # Add average line
            fig.add_shape(type='line', x0=min(dbh_mortality_rate['Year']), y0=average_mortality_rate,
                          x1=max(dbh_mortality_rate['Year']), y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def create_pie_chart_BDH_all_years_mortality(df):
            # Group by 'DBH Size Class' and calculate mortality rate for each DBH size class across all years
            dbh_mortality_rate = df.groupby('Size Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all size classes
            average_mortality_rate = dbh_mortality_rate['Mortality Rate'].mean()

            # Create pie chart
            fig = px.pie(dbh_mortality_rate, values='Mortality Rate', names='Size Class',
                         title='Mean Mortality Rate for Each DBH Size Class Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate (%)', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Mortality Rate: {average_mortality_rate:.2f}%',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)

        def calculate_mortality_rate(group):
            total_population = group.shape[0]
            dead_population = group[group['Status'] == 'Dead'].shape[0]
            if total_population == 0:
                return 0
            return dead_population / total_population

        def create_bar_chart_BDH_all_years_mortality_rate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'Mortality rate' for each DBH size class in each year
            dbh_mortality_rate = df.groupby(['Year', 'Size Class']).apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all years
            average_mortality_rate = dbh_mortality_rate['Mortality Rate'].mean()

            # Create bar chart
            fig = px.bar(dbh_mortality_rate, x='Year', y='Mortality Rate', color='Size Class',
                         title='Mean Mortality Rate for Each DBH Size Class Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')

            # Add average line
            fig.add_shape(type='line', x0=min(dbh_mortality_rate['Year']), y0=average_mortality_rate,
                          x1=max(dbh_mortality_rate['Year']), y1=average_mortality_rate,
                          line=dict(color="black", width=1, dash='dash'))

            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_mortality_rate(df):
            # Group by 'DBH Size Class' and calculate mean 'Mortality rate' for each DBH size class across all years
            dbh_mortality_rate = df.groupby('Size Class').apply(calculate_mortality_rate).reset_index(
                name='Mortality Rate')

            # Calculate average mortality rate across all size classes
            average_mortality_rate = dbh_mortality_rate['Mortality Rate'].mean()

            # Create pie chart
            fig = px.pie(dbh_mortality_rate, values='Mortality Rate', names='Size Class',
                         title='Mean Mortality Rate for Each DBH Size Class Across Years',
                         labels={'Mortality Rate': 'Mean Mortality Rate', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Mortality Rate: {average_mortality_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)





        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique(), default=['CANAPA', 'PAYELU', 'SHORP2'])

        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_mortality_rate(df)
            with col2:
                create_bar_chart_BDH_all_years_mortality(df)
            with st.expander("Mortality Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("Mortality Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_mortality(df, selected_year)
                with col2:
                    create_bar_chart_mortality_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_mortality_age(df, selected_year)
                with col2:
                    create_bar_chart_mortality_rate_age(df, selected_year)
            with st.expander("Mortality Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_mortality_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_mortality_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_mortality_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_mortality_rate_hectare_age(df, selected_hectares)


        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_mortality_rate(df)
            with col2:
                create_bar_chart_BDH_all_years_mortality(df)
            with st.expander("Growth Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("Mortality Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_mortality(df, selected_year)
                with col2:
                    create_pie_chart_mortality_rate(df, selected_year)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_mortality_age(df, selected_year)
                with col2:
                    create_pie_chart_mortality_rate_age(df, selected_year)

            with st.expander("Mortality Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_mortality_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_mortality_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_mortality_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_mortality_rate_hectare_age(df, selected_hectares)



    if option_tomenutype == 'Lifespan':
        def create_bar_chart_Lifespan(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Lifespan' for each size class
            size_class_Lifespan = selected_data.groupby('Size Class')['Lifespan'].sum().reset_index()
            # Calculate average Lifespan across all size classes
            average_Lifespan = size_class_Lifespan['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(size_class_Lifespan, x='Size Class', y='Lifespan',
                         title=f'Sum of Lifespan Across Size Classes for Year {selected_year}',
                         labels={'Size Class': 'Size Class', 'Lifespan': 'Lifespan'})
            # Change bar color and size
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)
            # Add dashed line for average Lifespan
            fig.add_shape(type='line', x0=size_class_Lifespan['Size Class'].iloc[0], y0=average_Lifespan,
                          x1=size_class_Lifespan['Size Class'].iloc[-1], y1=average_Lifespan,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Lifespan Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Lifespan(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Lifespan values
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Size Class' and calculate sum of 'Lifespan' for each size class
            size_class_Lifespan = selected_data.groupby('Size Class')['Lifespan'].sum().reset_index()

            # Calculate total Lifespan
            total_Lifespan = size_class_Lifespan['Lifespan'].sum()

            # Create pie chart
            fig = px.pie(size_class_Lifespan, values='Lifespan', names='Size Class',
                         title=f'Total Lifespan Across Size Classes for Year {selected_year}',
                         labels={'Lifespan': 'Lifespan', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for Lifespan distribution across size classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Lifespan_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'size class' and calculate average 'Lifespan' for each size class
            size_class_Lifespan_rate = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all size classes
            average_Lifespan_rate = size_class_Lifespan_rate['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(size_class_Lifespan_rate, x='Size Class', y='Lifespan',
                         title=f'Average Lifespan Across Size Classes for Year {selected_year}')
            fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.6)

            # Add dashed line for average Lifespan
            fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan_rate, x1=len(size_class_Lifespan_rate) - 0.5,
                          y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=500, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Lifespan Across Size Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Lifespan_rate(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Lifespan values
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Size Class' and calculate average 'Lifespan' for each size class
            size_class_Lifespan_rate = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all size classes
            average_Lifespan_rate = size_class_Lifespan_rate['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(size_class_Lifespan_rate, values='Lifespan', names='Size Class',
                         title=f'Average Lifespan Across Size Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Lifespan_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Lifespan' for each age class
            age_class_Lifespan = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all age classes
            average_Lifespan = age_class_Lifespan['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(age_class_Lifespan, x='Age Class', y='Lifespan',
                         title=f'Average Lifespan Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average Lifespan
            fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan, x1=len(age_class_Lifespan) - 0.5,
                          y1=average_Lifespan,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Total Lifespan Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Lifespan_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Lifespan values
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Age Class' and calculate average 'Lifespan' for each age class
            age_class_Lifespan = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all age classes
            average_Lifespan = age_class_Lifespan['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(age_class_Lifespan, values='Lifespan', names='Age Class',
                         title=f'Average Lifespan Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        # Function to create bar chart for average Lifespan across age classes for a selected year
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_bar_chart_Lifespan_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Age Class' and calculate average 'Lifespan' for each age class
            age_class_Lifespan_rate = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all age classes
            average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(age_class_Lifespan_rate, x='Age Class', y='Lifespan',
                         title=f'Average Lifespan Across Age Classes for Year {selected_year}')
            # Change bar color and size
            fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=0.7)
            # Add dashed line for average Lifespan
            fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan_rate, x1=len(age_class_Lifespan_rate) - 0.5,
                          y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            # Change chart size
            fig.update_layout(height=450, width=700)
            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis=dict(
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    mirror=True
                ),
                yaxis=dict(
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                    mirror=True
                ),
                title=dict(
                    text=f'Average Lifespan Across Age Classes for Year {selected_year}',
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )
            st.plotly_chart(fig)


        def create_pie_chart_Lifespan_rate_age(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Filter out negative Lifespan values
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Age Class' and calculate average 'Lifespan' for each age class
            age_class_Lifespan_rate = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all age classes
            average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(age_class_Lifespan_rate, values='Lifespan', names='Age Class',
                         title=f'Average Lifespan Across Age Classes for Year {selected_year}',
                         hole=0.3)

            # Change chart size
            fig.update_layout(height=450, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Lifespan_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()

                # Calculate average Lifespan across all age classes
                average_Lifespan = age_class_Lifespan['Lifespan'].mean()

                # Filter out negative Lifespan values
                age_class_Lifespan = age_class_Lifespan[age_class_Lifespan['Lifespan'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_Lifespan, values='Lifespan', names='Age Class',
                             title=f'Total Lifespan Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Lifespan_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()
                # Calculate average Lifespan across all age classes
                average_Lifespan = age_class_Lifespan['Lifespan'].mean()
                # Create bar chart
                fig = px.bar(age_class_Lifespan, x='Age Class', y='Lifespan',
                             title=f'Sum of Lifespan Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average Lifespan
                fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan, x1=len(age_class_Lifespan) - 0.5,
                              y1=average_Lifespan,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Lifespan Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average Lifespan across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Lifespan_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan_rate = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()

                # Calculate average Lifespan across all age classes
                average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()

                # Filter out negative Lifespan values
                age_class_Lifespan_rate = age_class_Lifespan_rate[age_class_Lifespan_rate['Lifespan'] >= 0]

                # Create pie chart
                fig = px.pie(age_class_Lifespan_rate, values='Lifespan', names='Age Class',
                             title=f'Average Lifespan Across Age Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Lifespan_rate_hectare_age(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan_rate = selected_data.groupby('Age Class')['Lifespan'].mean().reset_index()
                # Calculate average Lifespan across all age classes
                average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()
                # Create bar chart
                fig = px.bar(age_class_Lifespan_rate, x='Age Class', y='Lifespan',
                             title=f'Average Lifespan Across Age Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='blue', marker_line_color='black', marker_line_width=1.3, opacity=0.8)
                # Add dashed line for average Lifespan
                fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan_rate, x1=len(age_class_Lifespan_rate) - 0.5,
                              y1=average_Lifespan_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Lifespan Across Age Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Lifespan_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative Lifespan values
                selected_data = selected_data[selected_data['Lifespan'] >= 0]

                # Group by 'Size Class' and calculate average 'Lifespan' for each size class
                size_class_Lifespan = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()

                # Calculate average Lifespan across all size classes
                average_Lifespan = size_class_Lifespan['Lifespan'].mean()

                # Create pie chart
                fig = px.pie(size_class_Lifespan, values='Lifespan', names='Size Class',
                             title=f'Average Lifespan Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Lifespan_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()
                # Calculate average Lifespan across all age classes
                average_Lifespan = age_class_Lifespan['Lifespan'].mean()
                # Create bar chart
                fig = px.bar(age_class_Lifespan, x='Size Class', y='Lifespan',
                             title=f'Average Lifespan Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average Lifespan
                fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan, x1=len(age_class_Lifespan) - 0.5,
                              y1=average_Lifespan,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Total Lifespan Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        # Function to create bar chart for average Lifespan across age classes for selected hectares
        import plotly.express as px
        import plotly.graph_objects as go
        import streamlit as st


        def create_pie_chart_Lifespan_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]

                # Filter out negative Lifespan values
                selected_data = selected_data[selected_data['Lifespan'] >= 0]

                # Group by 'Size Class' and calculate average 'Lifespan' for each size class
                size_class_Lifespan_rate = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()

                # Calculate average Lifespan across all size classes
                average_Lifespan_rate = size_class_Lifespan_rate['Lifespan'].mean()

                # Create pie chart
                fig = px.pie(size_class_Lifespan_rate, values='Lifespan', names='Size Class',
                             title=f'Average Lifespan Across Size Classes for Hectare {hectare}',
                             hole=0.3)

                # Change chart size
                fig.update_layout(height=450, width=700)

                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    title=dict(
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )

                st.plotly_chart(fig)


        def create_bar_chart_Lifespan_rate_hectare(df, selected_hectares):
            for hectare in selected_hectares:
                # Filter data for the selected hectare
                selected_data = df[df['Hectare'] == hectare]
                # Group by 'Age Class' and calculate average 'Lifespan' for each age class
                age_class_Lifespan_rate = selected_data.groupby('Size Class')['Lifespan'].mean().reset_index()
                # Calculate average Lifespan across all age classes
                average_Lifespan_rate = age_class_Lifespan_rate['Lifespan'].mean()
                # Create bar chart
                fig = px.bar(age_class_Lifespan_rate, x='Size Class', y='Lifespan',
                             title=f'Average Lifespan Across Size Classes for Hectare {hectare}')
                # Change bar color and size
                fig.update_traces(marker_color='dark blue', marker_line_color='black', marker_line_width=1.3, opacity=1)
                # Add dashed line for average Lifespan
                fig.add_shape(type='line', x0=-0.5, y0=average_Lifespan_rate, x1=len(age_class_Lifespan_rate) - 0.5,
                              y1=average_Lifespan_rate,
                              line=dict(color="black", width=1, dash='dash'))
                # Change chart size
                fig.update_layout(height=450, width=700)
                # Add border around the chart
                fig.update_layout(
                    margin=dict(l=10, r=10, t=10, b=10),
                    paper_bgcolor="white",
                    plot_bgcolor="white",
                    xaxis=dict(
                        showline=True,
                        linewidth=2,
                        linecolor='black',
                        mirror=True
                    ),
                    yaxis=dict(
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                        mirror=True
                    ),
                    title=dict(
                        text=f'Average Lifespan Across Size Classes for Hectare {hectare}',
                        x=0.5,
                        y=.97,
                        xanchor='center',
                        yanchor='top',
                        font=dict(size=16)
                    )
                )
                st.plotly_chart(fig)


        def create_bar_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]
            # Group by 'Hectare' and 'Species' and calculate mean 'Lifespan' for each species in each hectare
            species_Lifespan_rate = selected_data.groupby(['Hectare', 'Species'])['Lifespan'].mean().reset_index()
            # Sort by 'Lifespan' in descending order within each hectare
            species_Lifespan_rate['Rank'] = species_Lifespan_rate.groupby('Hectare')['Lifespan'].rank(ascending=False)
            top_species = species_Lifespan_rate[
                species_Lifespan_rate['Rank'] <= 5]  # Select top 5 species in each hectare
            # Calculate average Lifespan across all species
            average_Lifespan_rate = top_species['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(top_species, x='Hectare', y='Lifespan', color='Species',
                         title=f'Top 5 Species with Highest Lifespans for Each Hectare - Year {selected_year}',
                         labels={'Lifespan': 'Mean Lifespan', 'Hectare': 'Hectare'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(top_species['Hectare']), y0=average_Lifespan_rate,
                          x1=max(top_species['Hectare']), y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_5_top_sp(df, selected_year):
            # Filter data for the selected year
            selected_data = df[df['Year'] == selected_year]

            # Group by 'Hectare' and 'Species' and calculate mean 'Lifespan' for each species in each hectare
            species_Lifespan_rate = selected_data.groupby(['Hectare', 'Species'])['Lifespan'].mean().reset_index()

            # Sort by 'Lifespan' in descending order within each hectare
            species_Lifespan_rate['Rank'] = species_Lifespan_rate.groupby('Hectare')['Lifespan'].rank(ascending=False)
            top_species = species_Lifespan_rate[
                species_Lifespan_rate['Rank'] <= 5]  # Select top 5 species in each hectare

            # Exclude negative Lifespans
            top_species = top_species[top_species['Lifespan'] >= 0]

            # Calculate average Lifespan across all species
            average_Lifespan_rate = top_species['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(top_species, values='Lifespan', names='Species',
                         title=f'Top 5 Species with Highest Lifespans for Each Hectare - Year {selected_year}',
                         labels={'Lifespan': 'Mean Lifespan', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Lifespan: {average_Lifespan_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]
            # Group by 'Year' and 'Species' and calculate mean 'Lifespan' for each species in each year
            species_Lifespan_rate = selected_data.groupby(['Year', 'Species'])['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all years for selected species
            average_Lifespan_rate = species_Lifespan_rate['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(species_Lifespan_rate, x='Year', y='Lifespan', color='Species',
                         title='Mean Lifespan of Selected Species Across Years',
                         labels={'Lifespan': 'Mean Lifespan', 'Year': 'Year'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(species_Lifespan_rate['Year']), y0=average_Lifespan_rate,
                          x1=max(species_Lifespan_rate['Year']), y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_sp_year(df, selected_species):
            # Filter data for selected species
            selected_data = df[df['Species'].isin(selected_species)]

            # Filter out negative Lifespans
            selected_data = selected_data[selected_data['Lifespan'] >= 0]

            # Group by 'Year' and 'Species' and calculate mean 'Lifespan' for each species in each year
            species_Lifespan_rate = selected_data.groupby(['Year', 'Species'])['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all years for selected species
            average_Lifespan_rate = species_Lifespan_rate['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(species_Lifespan_rate, values='Lifespan', names='Species',
                         title='Mean Lifespan of Selected Species Across Years',
                         labels={'Lifespan': 'Mean Lifespan', 'Species': 'Species'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Lifespan: {average_Lifespan_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_Lifespanrate(df):
            # Group by 'Year' and 'DBH Size Class' and calculate mean 'Lifespan' for each DBH size class in each year
            dbh_Lifespan_rate = df.groupby(['Year', 'Size Class'])['Lifespan'].mean().reset_index()
            # Calculate average Lifespan across all years
            average_Lifespan_rate = dbh_Lifespan_rate['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(dbh_Lifespan_rate, x='Year', y='Lifespan', color='Size Class',
                         title='Mean Lifespan for Each DBH Size Class Across Years',
                         labels={'Lifespan': 'Mean Lifespan', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_Lifespan_rate['Year']), y0=average_Lifespan_rate,
                          x1=max(dbh_Lifespan_rate['Year']), y1=average_Lifespan_rate,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        def create_pie_chart_BDH_all_years_Lifespanrate(df):
            # Group by 'DBH Size Class' and calculate mean 'Lifespan' for each DBH size class across all years
            dbh_Lifespan_rate = df.groupby('Size Class')['Lifespan'].mean().reset_index()

            # Calculate average Lifespan across all size classes
            average_Lifespan_rate = dbh_Lifespan_rate['Lifespan'].mean()

            # Create pie chart
            fig = px.pie(dbh_Lifespan_rate, values='Lifespan', names='Size Class',
                         title='Mean Lifespan for Each DBH Size Class Across Years',
                         labels={'Lifespan': 'Mean Lifespan', 'Size Class': 'Size Class'},
                         hole=0.3)

            # Add average line
            fig.add_annotation(
                x=0.5,
                y=0.5,
                text=f'Average Lifespan: {average_Lifespan_rate:.2f}',
                showarrow=False,
                font=dict(size=12)
            )

            # Change chart size
            fig.update_layout(height=500, width=700)

            # Add border around the chart
            fig.update_layout(
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="white",
                plot_bgcolor="white",
                title=dict(
                    x=0.5,
                    y=0.97,
                    xanchor='center',
                    yanchor='top',
                    font=dict(size=16)
                )
            )

            st.plotly_chart(fig)


        def create_bar_chart_BDH_all_years_Lifespan(df):
            # Group by 'Year' and 'DBH Size Class' and calculate sum 'Lifespan' for each DBH size class in each year
            dbh_Lifespan = df.groupby(['Year', 'Size Class'])['Lifespan'].sum().reset_index()
            # Calculate average Lifespan across all years
            average_Lifespan = dbh_Lifespan['Lifespan'].mean()
            # Create bar chart
            fig = px.bar(dbh_Lifespan, x='Year', y='Lifespan', color='Size Class',
                         title='Sum Lifespan for Each DBH Size Class Across Years',
                         labels={'Lifespan': 'Sum Lifespan', 'Year': 'Year', 'Size Class': 'Size Class'},
                         barmode='group')
            # Add average line
            fig.add_shape(type='line', x0=min(dbh_Lifespan['Year']), y0=average_Lifespan,
                          x1=max(dbh_Lifespan['Year']), y1=average_Lifespan,
                          line=dict(color="black", width=1, dash='dash'))
            st.plotly_chart(fig)


        st.sidebar.header("Setting")
        selected_year = st.sidebar.radio("Select Year", df['Year'].unique())
        selected_hectares = st.sidebar.multiselect("Select Hectares", df['Hectare'].unique(),
                                                   default=df['Hectare'].unique())
        selected_species = st.sidebar.multiselect("Select Species", df['Species'].unique(),
                                                  default=['CANAPA', 'PAYELU', 'SHORP2'])

        # -----------------------------------------

        # --------- Most SP
        chart_type = st.sidebar.radio("Select Chart Type", ("Bar Chart", "Pie Chart"))
        if chart_type == "Bar Chart":
            # ----------------------------------- the Main
            col1, col2 = st.columns(2)
            with col1:
                create_bar_chart_BDH_all_years_Lifespan(df)
            with st.expander("Lifespan Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_5_top_sp(df, selected_year)
                with col2:
                    create_bar_chart_sp_year(df, selected_species)

            with st.expander("Lifespan Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Lifespan(df, selected_year)
                with col2:
                    create_bar_chart_Lifespan_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Lifespan_age(df, selected_year)
                with col2:
                    create_bar_chart_Lifespan_rate_age(df, selected_year)

            with st.expander("Lifespan Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Lifespan_hectare(df, selected_hectares)
                with col2:
                    create_bar_chart_Lifespan_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_bar_chart_Lifespan_hectare_age(df, selected_hectares)
                with col2:
                    create_bar_chart_Lifespan_rate_hectare_age(df, selected_hectares)

        if chart_type == "Pie Chart":
            col1, col2 = st.columns(2)
            with col2:
                create_bar_chart_BDH_all_years_Lifespan(df)
            with st.expander("Lifespan Trends in Species"):
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_5_top_sp(df, selected_year)
                with col2:
                    create_pie_chart_sp_year(df, selected_species)

            with st.expander("Lifespan Trends in All Hectares (By Size class and Age Class)"):
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Lifespan(df, selected_year)
                with col2:
                    create_pie_chart_Lifespan_rate(df, selected_year)
                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Lifespan_age(df, selected_year)
                with col2:
                    create_pie_chart_Lifespan_rate_age(df, selected_year)

            with st.expander("Lifespan Trends in Selected Hectare (By Size class and Age Class)"):
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

                st.write("To see the trend in selected hectare please first choose your desire hectares")
                st.subheader("DBH Size Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Lifespan_hectare(df, selected_hectares)
                with col2:
                    create_pie_chart_Lifespan_rate_hectare(df, selected_hectares)

                st.subheader("Age Class")
                col1, col2 = st.columns(2)
                with col1:
                    create_pie_chart_Lifespan_hectare_age(df, selected_hectares)
                with col2:
                    create_pie_chart_Lifespan_rate_hectare_age(df, selected_hectares)
if option_tomenu == "Prescription Scenarios":
    # ---------------------------------------------- Show the first texts
    st.title('⛑ Biodiversity Dynamic Prescription:')
   # st.subheader("Biodiversity Dynamic prescription:")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    text = (
        "In this section we will see the suitable prescription.\n"
        "Also the implication of the prescription is explained below.\n"
        "\n Please select 👇 your desired year and desired prescription method and your Priority.\n"
    )

    font_size = 18
    font_color = "black"
    border_color = "#910603"  # Orange
    border_width = 3

    # Display the bordered text box for design visualization
    st.markdown(
        f"""
            <div style="padding:10px; border: {border_width}px solid {border_color}; border-radius: 5px;">
                <p style="font-size: {font_size}px; color: {font_color};">{text}</p>
            </div>
            """,
        unsafe_allow_html=True,
    )

    # -------------------------------------  selection box
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    col1, col2, col3  = st.columns(3)

    with col1:
        optionyear = st.selectbox(
            'Select Year to be prescriptive',
            ("2019", "2021"), index=0
        )

    with col2:
        option_objective = st.selectbox(
            "Select your Priority",
            ("to save Species","to keep Diversity","to keep Dominance"), index=0
        )


    column_mapping = {
        "to save Species": "Species-based",
        "to keep Diversity": "Diversity",
        "to keep Dominance": "Dominance"
    }
# ------------------------------------------------------------------v------------------ seleced 2019

    if optionyear == '2019':

        # ------------- show the first table
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        st.markdown(
            "<h3>Recommended Harvesting Action Plan: </h3>",
            unsafe_allow_html=True)
        data = {
            'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based',
                          'Dominance',
                          'Dominance', 'Dominance'],
            'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
            'Carbon Loss': [9.02, 11.51, 13.41, 8.87, 11.66, 13.91, 8.81, 11.43, 13.36],
            'Carbon Loss(M) in 2055': [6.44, 8.41, 10.44, 5.9, 7.23, 9.22, 6.12, 7.12, 8.16],
            'Tree to Harvest': [396, 169, 34, 396, 169, 34, 396, 169, 34],
            'Remaining Density': [433.73, 1638.80, 1921.84, 422.92, 1678.20, 1934.32, 438.01, 1568.80, 1919.08],
            'New AGB': [331.41, 1249.54, 1465, 340.88, 1299.22, 1471.43, 355.11, 1279.22, 1465.45],
            'Remaining Species': [307, 342, 360, 307, 342, 360, 307, 342, 360]
        }

        # Create DataFrame
        df = pd.DataFrame(data)
        df = df[df['Objective'] == column_mapping[option_objective]]
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
                        <td style="font-size: 18px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Objective']}</td>
                        <td style="font-size: 18px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Regime']}</td>
                        <td style="font-size: 18px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Tree to Harvest']}</td>
                        <td style="font-size: 18px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Remaining Density']}</td>
                        <td style="font-size: 18px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Remaining Species']}</td>
                        <td style="font-size: 18px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['New AGB']}</td>
                        <td style="font-size: 18px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Carbon Loss']}</td>
                        <td style="font-size: 18px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">{row['Carbon Loss(M) in 2055']}</td>
                    </tr></tbody>"""


        # Generate HTML code for the table with color-coding
        html_code = """<table style="font-size: 20px; text-align: left; border-collapse: collapse; width: 100%;"><thead><tr>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 18px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objective</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 18px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regime</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 18px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Tree to Harvest</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 18px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 18px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Species</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 18px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 18px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss(M)</th>
                        <th style="background-color: #851a15; color: #FFFFFF; font-size: 18px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss(M) in 2055</th>
                    </tr></thead>"""

        # Iterate through rows to create HTML table rows with color-coding
        for index, row in df_sorted.iterrows():
            html_code += generate_row_html(row)
            break
        html_code += "</table>"

        st.markdown(html_code, unsafe_allow_html=True)

        # --------------------------------------------------
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        st.markdown(
            "<h3>Detail:</h3>",
            unsafe_allow_html=True)
        if df_sorted['Regime'].iloc[0]  == 'heavy':
            def display_table_objective(selected_objective):

                html_table = """
                <table style="font-size: 28px; border-collapse: collapse; width: 100%;">
                    <thead>
                        <tr style="background-color: #132A13; color: #dfe6da; font-size: 18px; border-bottom: 3px solid #ddd;">
                            <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24+</th>
                            <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                            <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                            <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                            <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                            <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                            <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
                        </tr>
                    </thead>
                    <tbody>"""

                if selected_objective == "Diversity Objective":
                    html_table += """<tr style="text-align: left; font-size: 18px;">
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">29</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">78</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">210</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">40</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">355.01</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">8.81M</td>
                        </tr>"""
                elif selected_objective == "Species-based Objective":
                    html_table += """<tr style="text-align: left; font-size: 18px;">
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">29</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">78</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">210</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">40</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">340.85</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">8.87M</td>
                        </tr>"""
                elif selected_objective == "Dominance Objective":
                    html_table += """<tr style="text-align: left; font-size: 18px;">
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">29</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">78</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">210</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">40</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">331.41</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">9.02M</td>
                        </tr>"""
                elif selected_objective == "Economical Objective":
                    html_table += """<tr style="text-align: left; font-size: 18px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">396</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                        </tr>"""

                html_table += """
                        </tbody>
                    </table>
                """

                st.markdown(html_table, unsafe_allow_html=True)


            # Assume 'selected_objective' holds the currently selected objective
            selected_objective = f"{column_mapping[option_objective]} Objective"  # Change this value as needed

            # Call the function to display the table based on the selected objective
            display_table_objective(selected_objective)
        if df_sorted['Regime'].iloc[0]  == 'medium':
            def display_table_objective():
                html_table = """
                   <table style="border-collapse: collapse; width: 100%;">
                    <thead>
                        <tr style="background-color: #31572C; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
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
                            <td style="padding: 8px; border-right: 1px solid #ddd;">169</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">31</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">63</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">11</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1568.80</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1279.22</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">11.41M</td>
                        </tr>
                        <tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">169</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">31</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">63</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">11</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1878.02</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1299.22</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">11.66M</td>
                        </tr>
                            <tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">169</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">31</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">63</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">11</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1638.8</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1249.54</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">11.51M</td>
                        </tr>
                            <tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">169</td>
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
        if df_sorted['Regime'].iloc[0]  == 'light':
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
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">360</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">5</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1919.08</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1465.45</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">13.36M</td>
                        </tr>
                        <tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">360</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">5</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1934.32</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1471.43</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">13.91M</td>
                        </tr>
                            <tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">360</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">5</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1921.81</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">1465.01</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">13.41M</td>
                        </tr>
                            <tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
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


        regime = df_sorted['Regime'].iloc[0]
        objective = column_mapping[option_objective]

        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)

        st.markdown(
            "<h3>Predicted Implication in the next 30 years.</h3>",
            unsafe_allow_html=True)
        tab2, tab1, tab3 = st.tabs(["Predictions","3D vision" ,"Download Info"])

        # ----------------------
        if regime == "heavy" and objective=="Diversity":

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
        if regime == "heavy" and objective=="Species-based":
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
        if regime == "heavy" and objective=="Dominance":
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
        if regime == "medium" and objective=="Diversity":
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
        if regime == "light" and objective=="Diversity":
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
        ##############################################################################################
        # ------------------------------------------------------------------------------------------- the Main table
        html = f"""
            <table style="font-size: 22px; text-align: left; border-collapse: collapse; width: 100%;">
                <thead>
                    <tr>
                        <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Plan ID</th>
                        <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">#trees to harvest</th>
                        <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon loss</th>
                        <th style="background-color: #919B3e; color: #222577A; font-size: 14px; padding: 8px; border-bottom: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd; border-right: 3px solid #ddd;">Economic value</th>
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

        # _--------______-----_____------_____-------
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        st.markdown(
            "<h3>Other Harvesting Plan Options their ranking based on carbon loss.</h3>",
            unsafe_allow_html=True)
        data = {
            'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based',
                          'Dominance',
                          'Dominance', 'Dominance'],
            'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
            'Carbon Loss': [9.02, 11.51, 13.41, 8.87, 11.66, 13.91, 8.81, 11.43, 13.36],
            'Carbon Loss(M) in 2055': [6.44, 8.41, 10.44, 5.9, 7.23, 9.22, 6.12, 7.12, 8.16],
            'Tree to Harvest': [396, 169, 34, 396, 169, 34, 396, 169, 34],
            'Remaining Density': [433.73, 1638.80, 1921.84, 422.92, 1678.20, 1934.32, 438.01, 1568.80, 1919.08],
            'New AGB': [331.41, 1249.54, 1465, 340.88, 1299.22, 1471.43, 355.11, 1279.22, 1465.45],
            'Remaining Species': [307, 342, 360, 307, 342, 360, 307, 342, 360]
        }

        # Create DataFrame
        df = pd.DataFrame(data)
        df = df[df['Objective'] == column_mapping[option_objective]]
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

        st.markdown(html_code, unsafe_allow_html=True)


    if optionyear == "2021":

        # ------------- show the first table
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        st.markdown(
            "<h3>Now you can see the best of the harvesting plan scenarios (Regime) based on current situation of the forest.</h3>",
            unsafe_allow_html=True)
        data = {
            'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based',
                          'Dominance',
                          'Dominance', 'Dominance'],
            'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
            'Carbon Loss': [9.02, 11.51, 13.41, 8.87, 11.66, 13.91, 8.81, 11.43, 13.36],
            'Carbon Loss(M) in 2055': [6.44, 8.41, 10.44, 5.9, 7.23, 9.22, 6.12, 7.12, 8.16],
            'Tree to Harvest': [396, 169, 34, 396, 169, 34, 396, 169, 34],
            'Remaining Density': [433.73, 1638.80, 1921.84, 422.92, 1678.20, 1934.32, 438.01, 1568.80, 1919.08],
            'New AGB': [331.41, 1249.54, 1465, 340.88, 1299.22, 1471.43, 355.11, 1279.22, 1465.45],
            'Remaining Species': [307, 342, 360, 307, 342, 360, 307, 342, 360]
        }

        # Create DataFrame
        df = pd.DataFrame(data)
        df = df[df['Objective'] == column_mapping[option_objective]]
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
            break
        html_code += "</table>"

        st.markdown(html_code, unsafe_allow_html=True)

        # --------------------------------------------------
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        st.markdown(
            "<h3>Detail of the Harvesting Plan and the result of the harvesting</h3>",
            unsafe_allow_html=True)
        if df_sorted['Regime'].iloc[0] == 'heavy':
            def display_table_objective(selected_objective):
                html_table = """<table style="border-collapse: collapse; width: 100%;">
                        <thead>
                            <tr style="background-color: #132A13; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
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
                        <tbody>"""

                if selected_objective == "Diversity Objective":
                    html_table += """<tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Diversity Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">396</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">307</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">29</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">78</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">210</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">40</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">438.01</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">355.01</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">8.81M</td>
                        </tr>"""
                elif selected_objective == "Species-based Objective":
                    html_table += """<tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">396</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">307</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">29</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">78</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">210</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">40</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">442.99</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">340.85</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">8.87M</td>
                        </tr>"""
                elif selected_objective == "Dominance Objective":
                    html_table += """<tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">396</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">307</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">29</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">78</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">210</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">40</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">433.73</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">331.41</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">9.02M</td>
                        </tr>"""
                elif selected_objective == "Economical Objective":
                    html_table += """<tr style="text-align: left; font-size: 14px;">
                            <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">396</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                            <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                        </tr>"""

                html_table += """
                        </tbody>
                    </table>
                """

                st.markdown(html_table, unsafe_allow_html=True)


            # Assume 'selected_objective' holds the currently selected objective
            selected_objective = f"{column_mapping[option_objective]} Objective"  # Change this value as needed

            # Call the function to display the table based on the selected objective
            display_table_objective(selected_objective)
        if df_sorted['Regime'].iloc[0] == 'medium':
            def display_table_objective():
                html_table = """
                           <table style="border-collapse: collapse; width: 100%;">
                            <thead>
                                <tr style="background-color: #31572C; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
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
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">169</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">31</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">63</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">11</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1568.80</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1279.22</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">11.41M</td>
                                </tr>
                                <tr style="text-align: left; font-size: 14px;">
                                    <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">169</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">31</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">63</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">11</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1878.02</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1299.22</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">11.66M</td>
                                </tr>
                                    <tr style="text-align: left; font-size: 14px;">
                                    <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">169</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">31</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">63</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">11</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1638.8</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1249.54</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">11.51M</td>
                                </tr>
                                    <tr style="text-align: left; font-size: 14px;">
                                    <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">169</td>
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
        if df_sorted['Regime'].iloc[0] == 'light':
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
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">360</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">5</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1919.08</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1465.45</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">13.36M</td>
                                </tr>
                                <tr style="text-align: left; font-size: 14px;">
                                    <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">360</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">5</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1934.32</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1471.43</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">13.91M</td>
                                </tr>
                                    <tr style="text-align: left; font-size: 14px;">
                                    <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">360</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">5</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1921.81</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">1465.01</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">13.41M</td>
                                </tr>
                                    <tr style="text-align: left; font-size: 14px;">
                                    <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                                    <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
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

        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
        st.subheader("In the following table, you can see three regimes available based on selected year for Pasoh.")

        regime = df_sorted['Regime'].iloc[0]
        objective = column_mapping[option_objective]
        tab2, tab1, tab3 = st.tabs(["Predictions","3D vision" ,"Downlaod Info"])

        ####################################################################################
        if regime == "heavy" and objective=="Diversity":

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
        if regime == "heavy" and objective=="Species-based":
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
        if regime == "heavy" and objective=="Dominance":
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
        if regime == "medium" and objective=="Diversity":
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
        if regime == "light" and objective=="Diversity":
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

        #_--------______-----_____------_____-------
        st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
        st.markdown(
            "<h3>Now you can see the best of the harvesting plan scenarios (Regime) based on carbon loss.</h3>",
            unsafe_allow_html=True)
        data = {
            'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based',
                          'Dominance',
                          'Dominance', 'Dominance'],
            'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
            'Carbon Loss': [9.02, 11.51, 13.41, 8.87, 11.66, 13.91, 8.81, 11.43, 13.36],
            'Carbon Loss(M) in 2055': [6.44, 8.41, 10.44, 5.9, 7.23, 9.22, 6.12, 7.12, 8.16],
            'Tree to Harvest': [396, 169, 34, 396, 169, 34, 396, 169, 34],
            'Remaining Density': [433.73, 1638.80, 1921.84, 422.92, 1678.20, 1934.32, 438.01, 1568.80, 1919.08],
            'New AGB': [331.41, 1249.54, 1465, 340.88, 1299.22, 1471.43, 355.11, 1279.22, 1465.45],
            'Remaining Species': [307, 342, 360, 307, 342, 360, 307, 342, 360]
        }

        # Create DataFrame
        df = pd.DataFrame(data)
        df = df[df['Objective'] == column_mapping[option_objective]]
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

        st.markdown(html_code, unsafe_allow_html=True)

if option_tomenu == "Simulation":

    # Streamlit app
    st.title("Harvest Simulation")

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_year = st.selectbox("Select the Year", [2019, 2021])
    with col2:
        selected_objective = st.selectbox("Select the Prescription Method",['BDq'])
    with col3:
        selected_ranked = st.selectbox("to be Ranked by", ["Remaining Density", "New AGB", "Carbon Loss"])
    data = {
        'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based',
                      'Dominance',
                      'Dominance', 'Dominance'],
        'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
        'Carbon Loss': [9.07, 11.71, 13.67, 9, 11.80, 14.01, 9.1, 11.66, 13.66],
        'Carbon Loss(M) in 2055': [8.71, 9.71, 11.67, 7, 8.80, 10.01, 7.1, 8.66, 10.66],
        'Tree to Harvest': [385, 164, 32, 385, 164, 32, 385, 164, 32],
        'Remaining Density': [440.73, 1653.80, 1930.84, 432.92, 1698.20, 1948.32, 456.01, 1586.80, 1931.08],
        'New AGB': [334.63, 1255.66, 1466, 341.51, 1301.42, 1482.17, 360.08, 1282.21, 1467.02],
        'Remaining Species': [308, 342, 361, 308, 342, 361, 308, 342, 361]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Sort the DataFrame by Carbon Loss

    if selected_ranked == 'Carbon Loss':
        df_sorted = df.sort_values(by=selected_ranked)
        min_index = df_sorted[selected_ranked].idxmin()
    if selected_ranked == 'New AGB':
        df_sorted = df.sort_values(by=selected_ranked, ascending=False)
        min_index = df_sorted[selected_ranked].idxmax()
    if selected_ranked == 'Remaining Density':
        df_sorted = df.sort_values(by=selected_ranked, ascending=False)
        min_index = df_sorted[selected_ranked].idxmax()

    # Find the row index with the smallest Carbon Loss


    # Define a function to generate color-coded HTML for each row
    def generate_row_html(row):

        if selected_ranked == 'Carbon Loss':
            if row['Carbon Loss'] < 10:
                row_color = 'background-color: #37FF8F'  # Green
            elif 10 <= row['Carbon Loss'] <= 12:
                row_color = 'background-color: #E4FF37;'  # Yellow
            else:
                row_color = 'background-color: #FF4747;'  # Red

        if selected_ranked == 'New AGB':
            if row['New AGB'] > 1300:
                row_color = 'background-color: #37FF8F'  # Green
            elif 10 <= row['New AGB'] >= 1250:
                row_color = 'background-color: #E4FF37;'  # Yellow
            else:
                row_color = 'background-color: #FF4747;'  # Red

        if selected_ranked == 'Remaining Density':
            if row['Remaining Density'] > 1650:
                row_color = 'background-color: #37FF8F'  # Green
            elif 10 <= row['Remaining Density'] >= 1250:
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
    st.markdown(html_code , unsafe_allow_html=True)


    # Select the year (only 2021)
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_objective = st.selectbox("Select the Objective", ["to save Species","to keep Diversity","to keep Dominance"])
    with col2:
        selected_reguime = st.selectbox("Select the Regime", ["Heavy","Medium","Light"])
    with col3:
        selected_ml = st.selectbox("Select the Machine Learning Model", ['SVMOptimal', 'SVMV1', 'SVMV2', 'GRUV1'])

    data = {
        'Species': ['Oak', 'Pine', 'Maple', 'Birch', 'Spruce'],
        'D2019': [30, 25, 20, 18, 22],
        'D2021':[28,33,15,19,14]
    }

    # Create DataFrame
    df = pd.DataFrame(data)
    # Select the number of trees to harvest using a slider
    total_trees_2021 = df[f'D2019'].sum()
    if selected_reguime == 'Heavy':
        max_slider_value = 390
    if selected_reguime == 'Medium':
        max_slider_value = 164
    if selected_reguime == 'Light':
        max_slider_value = 32

        # Ensure the max_value doesn't exceed the total number of trees
    trees_to_harvest = st.slider("Number of Trees to Harvest", min_value=10, max_value=max_slider_value,
                                 value=total_trees_2021 // 2)

    # Number input fields for DBH classes
    dbh_classes = ['DBH Class 1', 'DBH Class 2', 'DBH Class 3', 'DBH Class 4', 'DBH Class 5']
    dbh_inputs = []

    initial_trees_per_class = trees_to_harvest // 5

    for i, dbh_class in enumerate(dbh_classes):
        max_trees = min(trees_to_harvest, df[f'D{selected_year}'].iloc[i])
        trees_for_dbh_class = st.number_input(f"Number of Trees for {dbh_class}", min_value=0,
                                              max_value=max_slider_value, value=initial_trees_per_class)
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
            # df = pd.read_csv('Prediction/DBHPrediction2055.csv')
            # Remove 385 rows randomly
            import requests
            import pandas as pd

            url = f'https://5557-34-125-115-229.ngrok-free.app/Predictionto2055{selected_ml}'

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
            # st.write(average_per_year)
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

            import numpy as np
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