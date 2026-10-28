import pandas as pd
from connected_sql import connect_tables

def load_data():
    tables= connect_tables()
    tablesname= ["Customers","Menu","Orders","Resturants","Delivery"]
    i=0
    for table in tables:
        table.to_csv(f"Data_SQL/{tablesname[i]}.csv")
        i+=1
    data={}
    i=0
    for table in tablesname:
        data[table]= tables[i]
        i+=1
    return data

print(load_data())

def clean_data(df= pd.DataFrame()):
    null_values = df.isnull().sum()
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    for col in df.select_dtypes(include="object").columns:
        df[col]= df[col].str.strip()
        df[col]= df[col].str.lower()
    return df

def load_clean_data():
    data= load_data()
    clean_df= {}
    for table_name,table_data in data.items():
        clean_df[table_name]= clean_data(table_data)
    return(clean_df)

load_clean_data()
    
        
