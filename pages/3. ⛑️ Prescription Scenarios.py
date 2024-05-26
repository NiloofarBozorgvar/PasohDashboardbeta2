import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px


# ----------------------------------------------------------------------------------------------------Text Box1

def display_design_element():
    st.subheader("Regime and Objective-based Simulation for Stand Prescription:")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    text = (
        "In this section we will see the different prescription scenarios.\n"
        "Also the implication of the prescription is explained below.\n"
        "\n Please select 👇 your desired year and desired prescription method to see the scenarios.\n"
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


# ----------------------------------------------------------------------------------------------------Text Box1
def display_design_elementv2(text):
    textconvert = (text)
    font_size = 15
    font_color = "#333333"  # Dark grey
    border_color = "#919B3e"  # Orange
    border_width = 1.5

    # Display the bordered text box for design visualization
    st.markdown(
        f"""
        <div style="padding:10px; border: {border_width}px solid {border_color}; border-radius: 5px;">
            <p style="font-size: {font_size}px; color: {font_color};">{textconvert}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
#---------------------------------------------------------------------------------------------------Text Box 2

def display_design_elementv3(text):
    textconvert = (text)
    font_size = 15
    font_color = "#287443"  # Dark grey
    border_color = "#bdbc25"  # Orange
    border_width = 1.5

    # Display the bordered text box for design visualization
    st.markdown(
        f"""
        <div style="padding:10px; border: {border_width}px solid {border_color}; border-radius: 5px;">
            <p style="font-size: {font_size}px; color: {font_color};">{textconvert}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    #---------------------------------------------------------------------------------------------Radio Buttons
def display_objective_selection():
    selected_objective = st.radio('Select you forest management objective:', ['Economical (Note: Data for Economical objective is not available now.)', 'Diversity', 'Species-based', 'Dominance'] , index=None)
    return selected_objective

def main():
    st.title('⛑️ Prescription Scenarios')
    display_design_element()



# ------------------------------------------------------------------------------------objective economicsal Sub table
def display_custom_table_Objective_economical():
    html_table = """
    <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #104f17; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Stock</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Carbon Loss</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Heavy Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1</td>
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
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Meduim Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">832</td>
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
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Light Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">742</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">832</td>
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


# ------------------------------------------------------------------------------------ objective diversity Sub Table
def display_custom_table_objective_Diversity():
    html_table = """
    <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #266b1c; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Heavy Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">385</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">308</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">77</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">209</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">440.73</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">334.63</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">9.07M</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Meduim Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">72</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">19</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1653.80</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1255.66</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">11.71M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Light Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">361</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">20</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">12</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">2</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1930.84</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1466</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">13.67M</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)


# ---------------------------------------------------------------------------------------objective species Sub Table
def display_custom_table_objective_species():
    html_table = """
       <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #4b872b; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Heavy Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">385</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">320</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">77</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">209</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">432.92</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">341.51</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">9M</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Meduim Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">72</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">348</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">19</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1698.20</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1301.42</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">11.80M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Light Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">358</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">20</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">12</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">2</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1948.32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1482.17</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">14.01M</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)
# ---------------------------------------------------------------------------------------objective dominance Sub Table
def display_custom_table_objective_dominance():
    html_table = """
       <table style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr style="background-color: #4b872b; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Regimes</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Total # Trees to Harvest</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Remaining Species</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 24<</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 18-23</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 12-17</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 6-11</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;"># Trees to harvest in DBH Class 1-5</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">Remaining Density</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New AGB</th>
                <th style="padding: 8px; border-right: 3px solid #ddd; border-top: 3px solid #ddd;">New Carbon Stock</th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Heavy Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">385</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">288</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">77</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">209</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">456.01</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">360.08</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">9.1M</td>
            </tr>
            <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Meduim Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">72</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">25</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">19</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1586.80</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1282.21</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">11.66M</td>
            </tr>
                <tr style="text-align: left; font-size: 14px;">
                <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Light Regime</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">34</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">362</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">20</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">12</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">2</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">-</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1931.08</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">1467.02</td>
                <td style="padding: 8px; border-right: 1px solid #ddd;">13.66M</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------Call Text Box


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



if __name__ == "__main__":
    main()
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# --------------------------------------------------------------------------------------------------------regimes table
# Create the data for the table
import streamlit as st
import pandas as pd

datatable = {
    'Plan ID': ['Plan 1: BDq Heavy regime', 'Plan 2: BDq Medium regime', 'Plan 3: BDq Light regime'],
    '#trees to harvest': [385, 72, 33],
    'Carbon loss': [7175435, 1379174, 298168],
    'Economic value': [742169, 532467, 149835]
}

dataobjectiveheavy = {
    'Objective': ['Economical', 'Diversity', 'Species-based', 'Dominance'],
    '# Trees to Harvest': [385, 74, None, None],
    '# Remaining Trees': [385, 74, None, None],
    '# Remaining Species': [385, 74, None, None],
    'Remaining Density': [385, 74, None, None],
    'New AGB': [385, 74, None, None],
    'Carbon Stock': [385, 74, None, None],
    'Carbon Loss': [385, 74, None, None],
}

dataobjectivemedium = {
    'Objective': ['Economical', 'Diversity', 'Species-based', 'Dominance'],
    '# Trees to Harvest': [385, 74, None, None],
    '# Remaining Trees': [385, 74, None, None],
    '# Remaining Species': [385, 74, None, None],
    'Remaining Density': [385, 74, None, None],
    'New AGB': [385, 74, None, None],
    'Carbon Stock': [385, 74, None, None],
    'Carbon Loss': [385, 74, None, None],
}

dataobjectivelight = {
    'Objective': ['Economical', 'Diversity', 'Species-based', 'Dominance'],
    '# Trees to Harvest': [385, 74, None, None],
    '# Remaining Trees': [385, 74, None, None],
    '# Remaining Species': [385, 74, None, None],
    'Remaining Density': [385, 74, None, None],
    'New AGB': [385, 74, None, None],
    'Carbon Stock': [385, 74, None, None],
    'Carbon Loss': [385, 74, None, None],
}
# -------------------------------------------------- Select Box for the prescription method and years


col1 , col2 = st.columns(2)

with col1:
    optionyear = st.selectbox(
        'Select Year',
        ("2019" , "2021"), index=0
    )

with col2:
    option = st.selectbox(
        "Select the Prescription Method",
        ("BDq",), index=0
    )
if optionyear == '2019':
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

    # Create a DataFrame
    df = pd.DataFrame(datatable)
    # -------------------------------------------------------------------------------------------
    data = {
        'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based', 'Dominance',
                      'Dominance', 'Dominance'],
        'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
        'Carbon Loss': [9.07, 11.71, 13.67, 9, 11.80, 14.01, 9.1, 11.66, 13.66],
        'Carbon Loss(M) in 2055': [8.71, 9.71, 11.67, 7, 8.80, 10.01, 7.1, 8.66, 10.66],
        'Tree to Harvest' :[385,164,32,385,164,32,385,164,32],
        'Remaining Density' :[440.73,1653.80,1930.84, 432.92,1698.20,1948.32, 456.01 , 1586.80,1931.08],
        'New AGB': [334.63,1255.66,1466,341.51,1301.42,1482.17,360.08,1282.21,1467.02],
        'Remaining Species':[308,342,361,308,342,361,308,342,361]
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
    col1, col2, col3 = st.columns(3)
    if col1.button('***Heavy regime***'):
        def display_table_objective():
            html_table = """
               <table style="border-collapse: collapse; width: 100%;">
                <thead>
                    <tr style="background-color: #132A13; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                        <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objectives</th>
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
                        <td style="padding: 8px; border-right: 1px solid #ddd;">385</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">308</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">77</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">209</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">440.73</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">334.63</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">9.07M</td>
                    </tr>
                    <tr style="text-align: left; font-size: 14px;">
                        <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">385</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">308</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">77</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">209</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">432.92</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">341.51</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">9M</td>
                    </tr>
                        <tr style="text-align: left; font-size: 14px;">
                        <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">385</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">308</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">28</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">77</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">209</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">39</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">456.01</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">360.08</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">9.1M</td>
                    </tr>
                        <tr style="text-align: left; font-size: 14px;">
                        <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">385</td>
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
    if col2.button('***Medium regime***'):
        def display_table_objective():
            html_table = """
               <table style="border-collapse: collapse; width: 100%;">
                <thead>
                    <tr style="background-color: #31572C; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                        <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objectives</th>
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
                        <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">30</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">62</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">24</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">10</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">1653.80</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">1255.66</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">11.71M</td>
                    </tr>
                    <tr style="text-align: left; font-size: 14px;">
                        <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Species-Based Objective</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">348</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">60</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">24</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">10</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">1698.20</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">1301.42</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">11.80M</td>
                    </tr>
                        <tr style="text-align: left; font-size: 14px;">
                        <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Dominance Objective</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">342</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">38</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">32</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">64</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">22</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">8</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">1586.80</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">1282.21</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">11.66M</td>
                    </tr>
                        <tr style="text-align: left; font-size: 14px;">
                        <td style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-bottom: 3px solid #ddd;">Economical Objective</td>
                        <td style="padding: 8px; border-right: 1px solid #ddd;">164</td>
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
    if col3.button('***Light regime***'):
        def display_table_objective():
            html_table = """
               <table style="border-collapse: collapse; width: 100%;">
                <thead>
                    <tr style="background-color: #4F772D; color: #dfe6da; font-size: 9.2px; border-bottom: 3px solid #ddd;">
                        <th style="padding: 8px; border-right: 3px solid #ddd; border-left: 3px solid #ddd; border-top: 3px solid #ddd;">Objectives</th>
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

    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    ##############################################################################################
    st.markdown("<h3>Now you can see the ranking of the harvesting plan scenarios (regimes and objectives) based on carbon loss.</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    # Display HTML code in a Markdown block
    st.markdown(html_code, unsafe_allow_html=True)
    # ------------------------------------------------------------------------------------------- select the regime and objective
    st.write("")
    st.write("Now you can select the regime and objective to see more information about them.")
    col1 , col2 = st.columns(2)

    with col1:
        regime = st.selectbox(
            'Select Regime',
            ("heavy" , "medium", "light"), index=0
        )

    with col2:
        objective = st.selectbox(
            "Select the Objective",
            ("Species-based", "Diversity", "Dominance"), index=0
        )
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
        <table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;">
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


if optionyear == "2021":
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
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">396</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">7175735</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">741345</td>
                </tr>
                <tr>
                    <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">Plan 1: BDq Medium regime</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">169</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">1379044</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">533211</td>
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

    # Create a DataFrame
    df = pd.DataFrame(datatable)
    # -------------------------------------------------------------------------------------------
    data = {
        'Objective': ['Diversity', 'Diversity', 'Diversity', 'Species-based', 'Species-based', 'Species-based', 'Dominance',
                      'Dominance', 'Dominance'],
        'Regime': ['heavy', 'medium', 'light', 'heavy', 'medium', 'light', 'heavy', 'medium', 'light'],
        'Carbon Loss': [9.02, 11.51, 13.41, 8.87, 11.66, 13.91, 8.81, 11.43, 13.36],
        'Carbon Loss(M) in 2055': [6.44, 8.41, 10.44, 5.9, 7.23, 9.22, 6.12, 7.12, 8.16],
        'Tree to Harvest' :[396,169,34,396,169,34,396,169,34],
        'Remaining Density' :[433.73,1638.80,1921.84, 422.92,1678.20,1934.32, 438.01 , 1568.80,1919.08],
        'New AGB': [331.41,1249.54,1465,340.88,1299.22,1471.43,355.11,1279.22,1465.45],
        'Remaining Species':[307,342,360,307,342,360,307,342,360]
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
    col1, col2, col3 = st.columns(3)
    if col1.button('***Heavy regime***'):
        def display_table_objective():
            html_table = """
               <table style="border-collapse: collapse; width: 100%;">
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
                <tbody>
                    <tr style="text-align: left; font-size: 14px;">
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
                    </tr>
                    <tr style="text-align: left; font-size: 14px;">
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
                    </tr>
                        <tr style="text-align: left; font-size: 14px;">
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
                    </tr>
                        <tr style="text-align: left; font-size: 14px;">
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
                    </tr>
                </tbody>
            </table>
            """
            st.markdown(html_table, unsafe_allow_html=True)
        display_table_objective()
    if col2.button('***Medium regime***'):
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
    if col3.button('***Light regime***'):
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

    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
    st.markdown("<h3>Now you can see the ranking of the harvesting plan scenarios (regimes and objectives) based on carbon loss.</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    # Display HTML code in a Markdown block
    st.markdown(html_code, unsafe_allow_html=True)
    # ------------------------------------------------------------------------------------------- select the regime and objective
    st.write("")
    st.write("Now you can select the regime and objective to see more information about them.")
    col1 , col2 = st.columns(2)

    with col1:
        regime = st.selectbox(
            'Select Regime',
            ("heavy" , "medium", "light"), index=0
        )

    with col2:
        objective = st.selectbox(
            "Select the Objective",
            ("Species-based", "Diversity", "Dominance"), index=0
        )
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
    ##############################################################################################
    # ------------------------------------------------------------------------------------------- the Main table
    html = f"""
        <table style="font-size: 18px; text-align: left; border-collapse: collapse; width: 100%;">
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
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">164</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">1379174</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">532467</td>
                </tr>
                <tr>
                    <td style="font-size: 14px; color: #423025; padding: 12px; border-bottom: 3px solid #ddd; border-right: 3px solid #ddd; border-left: 3px solid #ddd;">Plan 1: BDq Light regime</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">32</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">298168</td>
                    <td style="font-size: 14px; color: #4f483f; padding: 8px; border-bottom: 1px solid #ddd;">149835</td>
                </tr>
            </tbody>
        </table>
    """
