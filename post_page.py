import streamlit as st
from openpyxl import Workbook
from db import * 
import pandas as pd

options = ["1", "2", "3"]
colOptions = ["Customer Problem", "Product Features", "Business Model", "Product",
              "Hair on Fire Factor", "Access to Market", "Day 1 Revenue", "Revenue Scalability", "Defensibility", 
              "Lack of Competitors", "Personal Passion", "Unfair Advantage", "IP Creation", "Acquisition Potential"]

def run_startup_idea_page():
    addIdea()
    updateIdea()
    deleteIdea()
    
def addIdea(): 
    businessModelDF = pd.read_excel('data/Business Model.xlsx', engine='openpyxl')  
    businessModelDF = businessModelDF['Business Models'].values.tolist()
    
    with st.beta_expander("Add Product"):
        customerProblem = st.text_area("Describe Customer Problem:")
        productFeatures = st.text_area("Product features (tackle problems):")
        business_model = st.selectbox("Choose a Business Model:", businessModelDF)
        product = st.text_input("Product Name:")
        
        col1, col2 = st.beta_columns(2)
        with col1: 
            hair_on_fire_factor = st.radio("Hair on Fire Factor:", options)    
            access_to_market = st.radio("Access to Market:", options)   
            day_1_revenue = st.radio("Day 1 Revenue:", options)   
            revenueScalability = st.radio("Revenue Scalability:", options)   
            defensibility = st.radio("Defensibility:", options)   
        with col2:
            lackofCompetitors = st.radio("Lack of Competitors:", options)   
            personal_Passion = st.radio("Personal Passion:", options)   
            unfair_Advantage = st.radio("Unfair Advantage:", options)   
            ipCreation = st.radio("IP Creation:", options)   
            acquisition_Potential = st.radio("Acquisition Potential:", options) 

        if st.button("Add Start Up Idea"):
            add_data(customerProblem, productFeatures, business_model, product, 
                    hair_on_fire_factor, access_to_market, day_1_revenue, revenueScalability, defensibility, 
                    lackofCompetitors, personal_Passion, unfair_Advantage, ipCreation, acquisition_Potential)
            st.success("Added {}".format(product))        

def updateIdea():
    businessModelDF = pd.read_excel('data/Business Model.xlsx', engine='openpyxl')  
    businessModelDF = businessModelDF['Business Models'].values.tolist()

    with st.beta_expander("Update Product"):
        list_of_product = [i[0] for i in view_all_product()]
        selected_product = st.selectbox("Choose a product to update: ", list_of_product)
        product_result = get_product_by_name(selected_product)
        if product_result:
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

            updateCol1, updateCol2, updateCol3 = st.beta_columns([3,1,1])

            with updateCol1:
                new_customerProblem = st.text_area("Update Customer Problem:", customerProblem)
                new_productFeatures = st.text_area("Update Product features:", productFeatures)
                new_business_model = st.selectbox("Update Business Model:", businessModelDF)
                new_product = st.text_input("Update Product Name:", product)
        
            with updateCol2: 
                new_hair_on_fire_factor = st.radio("Update Hair on Fire Factor:", options, index=int(int(hair_on_fire_factor)-1))    
                new_access_to_market = st.radio("Update Access to Market:", options, index=int(int(access_to_market)-1))   
                new_day_1_revenue = st.radio("Update Day 1 Revenue:", options, index=int(int(day_1_revenue)-1))   
                new_revenueScalability = st.radio("Update Revenue Scalability:", options, index=int(int(revenueScalability)-1))   
                new_defensibility = st.radio("Update Defensibility:", options, index=int(int(defensibility)-1))   
        
            with updateCol3:
                new_lackofCompetitors = st.radio("Update Lack of Competitors:", options, index=int(int(lackofCompetitors)-1))   
                new_personal_Passion = st.radio("Update Personal Passion:", options, index=int(int(personal_Passion)-1))   
                new_unfair_Advantage = st.radio("Update Unfair Advantage:", options, index=int(int(unfair_Advantage)-1))   
                new_ipCreation = st.radio("Update IP Creation:", options, index=int(int(ipCreation)-1))   
                new_acquisition_Potential = st.radio(" Update Acquisition Potential:", options, index=int(int(acquisition_Potential)-1)) 

            if st.button("Update Product"):
                edit_product_data(new_customerProblem, new_productFeatures, new_business_model, new_product,
                                  new_hair_on_fire_factor, new_access_to_market, new_day_1_revenue, new_revenueScalability, new_defensibility, 
                                  new_lackofCompetitors, new_personal_Passion, new_unfair_Advantage, new_ipCreation, new_acquisition_Potential, product)
                st.success("Updated {}".format(product))

def deleteIdea():
    with st.beta_expander("Delete Product"):
        result = view_all_data()
        df = pd.DataFrame(result, columns=colOptions)
        st.dataframe(df)
        productList = [i[0] for i in view_all_product()]
        productName = st.selectbox("Product to Delete", productList)
        
        if st.button("Delete"):
            delete_data(productName)
            st.warning("Deleted {}".format(productName))
            
        result2 = view_all_data()
        new_df = pd.DataFrame(result2, columns=colOptions)
        st.dataframe(new_df)