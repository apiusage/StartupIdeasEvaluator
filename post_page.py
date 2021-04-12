import streamlit as st
from db import * 
import pandas as pd

def run_startup_idea_page():
    create_table()
    addIdea()
    updateIdea()
    deleteIdea()
    
def addIdea(): 
    with st.beta_expander("Add Ideas"):
        customer_group = st.selectbox("Customer Group:", 
        ["As a frequent traveler", "As a worker in a remote team",
        "As a social media influencer", "As an owner of an independent gym / yoga studio"])
        customerProblem = st.text_area("Customer Problem:")
        business_model = st.selectbox("Business Model:", 
        ["SaaS", "Ecommerce", "Enterprise SaaS", "Online course", "Advertising"])
        product = st.text_input("Product:")
        
        col1, col2 = st.beta_columns(2)
        with col1: 
            hair_on_fire_factor = st.radio("Hair on Fire Factor:", ["1", "2", "3"])    
            access_to_market = st.radio("Access to Market:", ["1", "2", "3"])   
            day_1_revenue = st.radio("Day 1 Revenue:", ["1", "2", "3"])   
            revenueScalability = st.radio("Revenue Scalability:", ["1", "2", "3"])   
            defensibility = st.radio("Defensibility:", ["1", "2", "3"])   
        
        with col2:
            lackofCompetitors = st.radio("Lack of Competitors:", ["1", "2", "3"])   
            personal_Passion = st.radio("Personal Passion:", ["1", "2", "3"])   
            unfair_Advantage = st.radio("Unfair Advantage:", ["1", "2", "3"])   
            ipCreation = st.radio("IP Creation:", ["1", "2", "3"])   
            acquisition_Potential = st.radio("Acquisition Potential:", ["1", "2", "3"]) 

        if st.button("Add Start Up Idea"):
            add_data(customer_group, customerProblem, business_model, product, 
                    hair_on_fire_factor, access_to_market, day_1_revenue, 
                    revenueScalability, defensibility, lackofCompetitors,
                    personal_Passion, unfair_Advantage, ipCreation, acquisition_Potential)
            st.success("Added {}".format(product))        

def updateIdea():
    with st.beta_expander("Update Ideas"):
        list_of_product = [i[0] for i in view_all_product()]
        selected_product = st.selectbox("Product", list_of_product)
        product_result = get_product_by_name(selected_product)
        if product_result:
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

            updateCol1, updateCol2, updateCol3 = st.beta_columns([3,1,1])

            with updateCol1:
                new_customer_group = st.selectbox("Update Customer Group:", ["As a frequent traveler", "As a worker in a remote team",
                "As a social media influencer", "As an owner of an independent gym / yoga studio"])
                new_customerProblem = st.text_area("Update Customer Problem:", customerProblem)
                new_business_model = st.selectbox("Update Business Model:", 
                ["SaaS", "Ecommerce", "Enterprise SaaS", "Online course", "Advertising"])
                new_product = st.text_input("Update Product:", product)
        
            with updateCol2: 
                new_hair_on_fire_factor = st.radio("Update Hair on Fire Factor:", ["1", "2", "3"], index=int(int(hair_on_fire_factor)-1))    
                new_access_to_market = st.radio("Update Access to Market:", ["1", "2", "3"], index=int(int(access_to_market)-1))   
                new_day_1_revenue = st.radio("Update Day 1 Revenue:", ["1", "2", "3"], index=int(int(day_1_revenue)-1))   
                new_revenueScalability = st.radio("Update Revenue Scalability:", ["1", "2", "3"], index=int(int(revenueScalability)-1))   
                new_defensibility = st.radio("Update Defensibility:", ["1", "2", "3"], index=int(int(defensibility)-1))   
        
            with updateCol3:
                new_lackofCompetitors = st.radio("Update Lack of Competitors:", ["1", "2", "3"], index=int(int(lackofCompetitors)-1))   
                new_personal_Passion = st.radio("Update Personal Passion:", ["1", "2", "3"], index=int(int(personal_Passion)-1))   
                new_unfair_Advantage = st.radio("Update Unfair Advantage:", ["1", "2", "3"], index=int(int(unfair_Advantage)-1))   
                new_ipCreation = st.radio("Update IP Creation:", ["1", "2", "3"], index=int(int(ipCreation)-1))   
                new_acquisition_Potential = st.radio(" Update Acquisition Potential:", ["1", "2", "3"], index=int(int(acquisition_Potential)-1)) 

            if st.button("Update Product"):
                edit_product_data(new_customer_group, new_customerProblem, new_business_model, new_product,
                                new_hair_on_fire_factor, new_access_to_market, new_day_1_revenue, new_revenueScalability, new_defensibility, 
                                new_lackofCompetitors, new_personal_Passion, new_unfair_Advantage, new_ipCreation, new_acquisition_Potential, product)
                st.success("Updated {}".format(product))

def deleteIdea():
    with st.beta_expander("Delete Ideas"):
        result = view_all_data()
        df = pd.DataFrame(result, columns=["Customer Group", "Customer Problem", "Business Model", "Product",
                                            "Hair on Fire Factor", "Access to Market", "Day 1 Revenue", "Revenue Scalability",
                                            "Defensibility", "Lack of Competitors", "Personal Passion", "Unfair Advantage", 
                                            "IP Creation", "Acquisition Potential"] )
        st.dataframe(df)
        unique_list = [i[0] for i in view_all_product()]
        delete_by_product_name = st.selectbox("Product to Delete", unique_list)
        
        if st.button("Delete"):
            delete_data(delete_by_product_name)
            st.warning("Deleted {}".format(delete_by_product_name))
            
        result2 = view_all_data()
        new_df = pd.DataFrame(result2, columns=["Customer Group", "Customer Problem", "Business Model", "Product",
                                            "Hair on Fire Factor", "Access to Market", "Day 1 Revenue", "Revenue Scalability",
                                            "Defensibility", "Lack of Competitors", "Personal Passion", "Unfair Advantage", 
                                            "IP Creation", "Acquisition Potential"] )
        st.dataframe(new_df)