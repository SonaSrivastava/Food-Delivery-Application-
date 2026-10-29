import streamlit as st 
from cleaning_data import load_clean_data
from customer_analysis import customer_analysis
from orders_analysis import analyze_orders, monthly_orders
from delivery_analysis import analyze_delivery, delivery_status
import os 
from connected_sql import connect_database

st.set_page_config(page_title="Food Delivery Analysis",layout="wide")

st.title("Food Delivery Analysis App 🥪🛵")    

try:
    data= load_clean_data()
    customer= data["Customers"]
    order= data["Orders"]
    menu= data["Menu"]
    resturants= data["Resturants"]
    delivery= data["Delivery"]
    print("All Table Loaded")
except:
    print("Database connection Failed")
    
CA,OA,DA= st.tabs(["Customer Analysis","Order Analysis","Delivery Analysis"])

with CA:
    st.header("Customer Analysis Report")
    st.divider()
    col1,col2,col3= st.columns(3)
    customer_analysis_data= customer_analysis(customer,order)
    col1.header("Total Customer")
    col1.subheader(customer_analysis_data["Total_customers"])
    col2.header("Repeated Customer")
    col2.subheader(customer_analysis_data["repeted_customers"])
    col3.header("New Customer")
    col3.subheader(customer_analysis_data["new customers"])
    st.divider()
    st.header("Gender Analysis")
    st.bar_chart(customer_analysis_data["Gender count"])
    st.divider()
    st.header("Area Analysis")
    st.divider()
    st.bar_chart(customer_analysis_data["city_count"])
    
with OA:
    st.header("Order Analysis Report 🥪")
    orders_analysis_data= analyze_orders(order)
    st.divider()
    col1,col2,col3= st.columns(3)
    col1.header("Total Revenue")
    col1.subheader(orders_analysis_data["Revenue"])
    col2.header("Total Orders")
    col2.subheader(orders_analysis_data["Total_Orders"])
    col3.header("Average Order Value")
    col3.subheader(orders_analysis_data["Average Orders Value"])
    st.divider()
    monthly_orders_data= monthly_orders(order)
    st.header("Monthly Order Analysis")
    st.divider()
    st.line_chart(monthly_orders_data)
    
with DA:
    st.header("Delivery Analysis Report 🛵")
    st.divider()
    d_m= analyze_delivery(order,delivery)["delivery_minutes"]
    average_delivery_minutes= d_m.mean()
    st.header("Average delivery time")
    st.subheader(average_delivery_minutes)
    # st.matric("Average delivery time","%.1f"%average_delivery_minutes)
    st.divider()
    st.header("Delivery Status")
    status= delivery_status(delivery)
    st.bar_chart(status)
    st.divider()
    st.subheader("Delivery Data Record")
    st.dataframe(analyze_delivery(order,delivery))
st.sidebar.header("Food Delivery Database")
st.sidebar.subheader("Status")

engine= connect_database()

if engine is not None:
    st.sidebar.subheader("Status: 🟢 Connected")
else:
    st.sidebar.subheader("Status: 🔴 Not Connected")
    




    

