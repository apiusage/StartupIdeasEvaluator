import streamlit as st
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

customer_group = customerProblem = business_model = product = None
hair_on_fire_factor = access_to_market = None
day_1_revenue = revenueScalability = defensibility = lackofCompetitors = None
personal_Passion = unfair_Advantage = ipCreation = acquisition_Potential = None

# Pack list
data = (customer_group, customerProblem, business_model, product,
        hair_on_fire_factor, access_to_market, 
        day_1_revenue, revenueScalability, defensibility, lackofCompetitors, 
        personal_Passion, unfair_Advantage, ipCreation, acquisition_Potential)

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS \
        startupIdea( \
            customer_group TEXT, \
            customerProblem TEXT, \
            business_model TEXT, \
            product TEXT, \
            hair_on_fire_factor TEXT, \
            access_to_market TEXT, \
            day_1_revenue TEXT, \
            revenueScalability TEXT, \
            defensibility TEXT, \
            lackofCompetitors TEXT, \
            personal_Passion TEXT, \
            unfair_Advantage TEXT, \
            ipCreation TEXT, \
            acquisition_Potential TEXT \
        )')

# https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
def add_data(*data):
    c.execute('INSERT INTO startupIdea(customer_group, customerProblem, business_model, product, \
        hair_on_fire_factor, access_to_market, \
        day_1_revenue, revenueScalability, defensibility, lackofCompetitors, \
        personal_Passion, unfair_Advantage, ipCreation, acquisition_Potential) \
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM startupIdea')
    data = c.fetchall()
    return data

def view_all_product():
    c.execute('SELECT DISTINCT product FROM startupIdea')
    data = c.fetchall()
    return data

def get_product_by_name(product):
    c.execute('SELECT * FROM startupIdea WHERE product = "{}"'.format(product))
    data = c.fetchall()
    return data

def edit_product_data(*updatedData):
    c.execute("UPDATE startupIdea SET \
                customer_group=?,\
                customerProblem=?,\
                business_model=?,\
                product=?,\
                hair_on_fire_factor=?,\
                access_to_market=?,\
                day_1_revenue=?,\
                revenueScalability=?,\
                defensibility=?,\
                lackofCompetitors=?,\
                personal_Passion=?, \
                unfair_Advantage=?, \
                ipCreation=?, \
                acquisition_Potential=? WHERE \
                product=?", updatedData)
    conn.commit()
    data = c.fetchall()
    return data

def delete_data(product):
    c.execute('DELETE FROM startupIdea WHERE product = "{}"'.format(product))
    conn.commit()