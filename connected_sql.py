import pandas as pd


from sqlalchemy import create_engine

def connect_database():
    try:
        engine=create_engine(url="mssql+pyodbc://@YOUR_SERVER_NAME/food_delivery""?driver=ODBC+Driver+18+for+SQL+Server"
                             "&trusted_connection=yes""&TrustServerCertificate=yes")
    except:
        return None,False
    else:
        return engine,True
    
        
def connect_tables():
    try:
        engine,_=connect_database()
        if engine is not None:
            Customers=pd.read_sql_query("select * from Customers",engine())
            Menu_item=pd.read_sql_query("select * from Menu_item",engine())
            Orders=pd.read_sql_query("select * from Orders",engine())
            Resturants=pd.read_sql_query("select * from Resturants",engine())
            Delivery=pd.read_sql_query("select * from Delivery",engine())
    except:
        print("Table name is incorrect...")
    else:
        return Customers,Menu_item,Orders,Resturants,Delivery


    
