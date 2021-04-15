import streamlit as st
from post_page import *
from insights import interestbyRegion
from db import * 
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import streamlit.components.v1 as stc
from PIL import Image

img = Image.open("Logo.jpg")
PAGE_CONFIG = {"page_title": "Startup Ideas Evaluator", "page_icon":img, "layout":"centered", "initial_sidebar_state": "collapsed" }
st.set_page_config(**PAGE_CONFIG)

LOGO_BANNER = """
    <div style="background-color:#464e5f;padding:3px;border-radius:10px";>
    <h1 style="color:white;text-align:center;"> Startup Ideas Evaluator </h1>
    </div>
    """

# Hide "Streamlit" from menu and footer
# MainMenu {visibility: hidden;}
hide_streamlit_style = """
    <style> 
         footer {visibility: hidden;}
         footer:after {
	        content:'Made by Bryson'; 
	        visibility: visible;
	        display: block;
	        position: relative;
	        # background-color: #464e5f;
	        top: 2px;
            }
    </style>
    """

def main():
        stc.html(LOGO_BANNER)

        menu = ["Start up Ideas", "Insights", "About"]
        choice = st.sidebar.selectbox("Menu", menu)
        create_table()

        if choice == "Start up Ideas":
            run_Data_Analysis()
            analytics()
            run_startup_idea_page()

        elif choice == "Insights":
            interestbyRegion()

        elif choice == "About":
            st.header("About")
            st.write("There is a lack of tool to evaluate whether a startup idea is viable. \
                    This tool is built to help out any individuals out there to evaluate their startup ideas. \
                    Inspired by https://blog.yongfook.com/12-startups-in-12-months.html ")
            st.balloons()
        
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        

def run_Data_Analysis(): 
    try:
        result = view_all_data()
        df = pd.DataFrame(result, columns=colOptions)
        c1, c2 = st.beta_columns([1,3])
        with c1:
            list_of_product = [i[0] for i in view_all_product()]
            selected_product = st.selectbox("Select Product: ", list_of_product)

        with c2:
            product_result = get_product_by_name(selected_product)
            customerProblem = product_result[0][0]
            productFeatures = product_result[0][1]
            business_model = product_result[0][2]
            product = product_result[0][3]
            hair_on_fire_factor = product_result[0][4]
            access_to_market = product_result[0][5]
            day_1_revenue = product_result[0][6]
            revenueScalability = product_result[0][7]
            defensibility = product_result[0][8]
            lackofCompetitors = product_result[0][9]
            personal_Passion = product_result[0][10]
            unfair_Advantage = product_result[0][11]
            ipCreation = product_result[0][12]
            acquisition_Potential = product_result[0][13]

            st.info("__Product__: {}".format(product))
            longCustProblemText = "__Customer Problem:__ {}".format("\n" + customerProblem)
            custText = ' '.join([longCustProblemText])
            st.markdown(custText)
            st.markdown("__Product Features:__ {}".format(productFeatures))
            st.markdown("__Business Model:__ {}".format(business_model))
            st.markdown("__Hair on fire factor:__ {}".format(hair_on_fire_factor))
            st.markdown("__Access to market:__ {}".format(access_to_market))
            st.markdown("__Day 1 revenue:__ {}".format(day_1_revenue))
            st.markdown("__Revenue Scalability:__ {}".format(revenueScalability))
            st.markdown("__Defensibility:__ {}".format(defensibility))
            st.markdown("__Lack of Competitors:__ {}".format(lackofCompetitors))
            st.markdown("__Personal Passion:__ {}".format(personal_Passion))
            st.markdown("__Unfair Advantage:__ {}".format(unfair_Advantage))
            st.markdown("__IP Creation:__ {}".format(ipCreation))
            st.markdown("__Acquisition Potential:__ {}".format(acquisition_Potential))
    except:
        pass


def search():
    search_term = st.text_input("Search product")
    if st.button("Search"):
        search_result = get_product_by_name(search_term)
        st.write(search_result)

def analytics():
    result = view_all_data()
    df = pd.DataFrame(result, columns=colOptions)

    df[["Hair on Fire Factor", "Access to Market", "Day 1 Revenue", "Revenue Scalability",
         "Defensibility", "Lack of Competitors", "Personal Passion", "Unfair Advantage",
         "IP Creation", "Acquisition Potential" ]] = df[["Hair on Fire Factor", "Access to Market", 
         "Day 1 Revenue", "Revenue Scalability", "Defensibility", "Lack of Competitors", 
         "Personal Passion", "Unfair Advantage", "IP Creation", "Acquisition Potential"]].apply(pd.to_numeric)
    sum_column = df['Hair on Fire Factor'] + df['Access to Market'] + \
        df['Day 1 Revenue'] + df['Revenue Scalability'] + df['Defensibility'] + \
        df['Lack of Competitors'] + df['Personal Passion'] + \
        df['Unfair Advantage'] + df['IP Creation'] + df['Acquisition Potential'] 
    df["Rating"] = sum_column
    
    # Pie chart
    p1 = px.pie(df,names='Product',values='Rating')
    st.plotly_chart(p1, use_container_width=True)	

    # Bar chart
    fig2 = px.bar(df, x = 'Product', y = 'Rating')
    st.plotly_chart(fig2, use_container_width=True)

    search()
    st.dataframe(df.sort_values(by='Rating', ascending=False))

if __name__ == '__main__':
    main()
