
from cleaning_data import load_clean_data
orders= load_clean_data()["Orders"]

print(load_clean_data())
print(orders.columns)


def analyze_orders(Orders):
    revenue= Orders["total_price"].sum()
    total_orders= Orders["order_id"].nunique()
    average_order_value= Orders["total_price"].mean()
    
    return{"Revenue":float(revenue),"Total_Orders":int(total_orders),"Average Orders Value":float(average_order_value)}
print(analyze_orders(orders))


def monthly_orders(orders):
    orders["months"]= orders["order_datetime"].dt.to_period("M").astype("str")
    return orders[["order_id","months"]].groupby("months").count()
        
print(monthly_orders(orders))
    
