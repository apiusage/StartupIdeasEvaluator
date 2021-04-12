import streamlit as st
from post_page import run_startup_idea_page
from db import * 
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import streamlit.components.v1 as stc
from PIL import Image

img = Image.open("Logo.jpg")
PAGE_CONFIG = {"page_title": "Startup Ideas Evaluator", "page_icon":img, "layout":"centered", "initial_sidebar_state": "expanded" }
st.set_page_config(**PAGE_CONFIG)

LOGO_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;"> Startup Validator </h1>
    <p style="color:white;text-align:center;">Built with Bryson</p>
    </div>
    """

def main():
    stc.html(LOGO_BANNER)
    # st.title("Startup Idea Evaluator")

    menu = ["Start up Ideas", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Start up Ideas":
        run_Data_Analysis()
        analytics()
        run_startup_idea_page()


    elif choice == "About":
        st.header("About")
        st.write("There is a lack of tool to evaluate whether a startup idea is viable. \
                This tool is built to help out any individuals out there to evaluate their startup ideas. \
                Inspired by https://blog.yongfook.com/12-startups-in-12-months.html ")
        st.balloons()

def search():
    search_term = st.text_input("Search product")

    if st.button("Search"):
        search_result = get_product_by_name(search_term)
        st.write(search_result)

def analytics():
    result = view_all_data()
    df = pd.DataFrame(result, columns=["Customer Group", "Customer Problem", "Business Model", "Product",
                                            "Hair on Fire Factor", "Access to Market", "Day 1 Revenue", "Revenue Scalability",
                                            "Defensibility", "Lack of Competitors", "Personal Passion", "Unfair Advantage", 
                                            "IP Creation", "Acquisition Potential"] )

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

def run_Data_Analysis(): 
    result = view_all_data()
    df = pd.DataFrame(result, columns=["Customer Group", "Customer Problem", "Business Model", "Product",
                                        "Hair on Fire Factor", "Access to Market", "Day 1 Revenue", "Revenue Scalability",
                                        "Defensibility", "Lack of Competitors", "Personal Passion", "Unfair Advantage", 
                                        "IP Creation", "Acquisition Potential"] )
    c1, c2 = st.beta_columns([1,3])
    with c1:
        list_of_product = [i[0] for i in view_all_product()]
        selected_product = st.selectbox("Select Products", list_of_product)

    with c2:
        product_result = get_product_by_name(selected_product)
        customer_group = product_result[0][0]
        customerProblem = product_result[0][1]
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

        st.info("Product: {}".format(product))
        longCustProblemText = "Customer Problem: {}".format("\n" + customerProblem)
        custText = ' '.join([longCustProblemText])
        st.markdown(custText)
        st.markdown("Customer Group: {}".format(customer_group))
        st.markdown("Business Model: {}".format(business_model))
        st.markdown("Hair on fire factor: {}".format(hair_on_fire_factor))
        st.markdown("Access to market: {}".format(access_to_market))
        st.markdown("Day 1 revenue: {}".format(day_1_revenue))
        st.markdown("Revenue Scalability: {}".format(revenueScalability))
        st.markdown("Defensibility: {}".format(defensibility))
        st.markdown("Lack of Competitors: {}".format(lackofCompetitors))
        st.markdown("Personal Passion: {}".format(personal_Passion))
        st.markdown("Unfair Advantage: {}".format(unfair_Advantage))
        st.markdown("IP Creation: {}".format(ipCreation))
        st.markdown("Acquisition Potential: {}".format(acquisition_Potential))

if __name__ == '__main__':
    main()