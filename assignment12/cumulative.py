import sqlite3 
import pandas as pd
import matplotlib.pyplot as plt



#Connect to database 
conn = sqlite3.connect("/home/lilly/Documents/python-assignment12/lesson.db")

#Create a DataFrame with order_id and total_price for each order

query = """
SELECT o.order_id, SUM(price * quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id;
"""
#Load into DataFrame
df= pd.read_sql_query(query, conn)
#close connection 
conn.close()
#Cumulative columns 
#def cumulative(row):
#   totals_above = df['total_price'][0:row.name+1]
#   return totals_above.sum()

df['cumulative'] = df['total_price'].cumsum()
print(df)

#Plot
df.plot(
    kind="line",
    x="order_id",   
    y="cumulative",
    color="blue",
    figsize=(10, 6)
)
plt.title("Cumulative Revenue Over Orders")
plt.xlabel("Order ID", fontsize=15)
plt.ylabel("Cumulative Revenue", fontsize=15)
plt.tight_layout()
plt.savefig('cumulative_revenue.png', dpi=150)
plt.show()