import pandas as pd
df = pd.read_csv("train.csv")

# Yıllara Göre Gruplayarak Toplam Satış Grafiği

import pandas as pd
import matplotlib.pyplot as plt

df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y').dt.strftime('%Y')

sales_by_year = df.groupby('Ship Date')['Sales'].sum()

plt.bar(sales_by_year.index, sales_by_year.values)
plt.title('Yıllara Göre Toplam Satış')
plt.xlabel('Yıl')
plt.ylabel('Toplam Satış')
plt.show()

# En Fazla Satış Yapılan 20 Müşteri
import pandas as pd
import matplotlib.pyplot
customer_sales = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False)[:20]
customer_sales.plot(kind='bar', figsize=(10,6))
plt.title('İlk 20 Müşteri')
plt.xlabel('Müşteri Adı')
plt.ylabel('Satış Miktarı')
plt.show()

# En Fazla Satış Yapılan 20 Şehir
import pandas as pd
import matplotlib.pyplot as plt
customer_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)[:20]
customer_sales.plot(kind='bar', figsize=(10,6))
plt.title('İlk 20 Şehir')
plt.xlabel('Şehirler')
plt.ylabel('Satış Miktarı')
plt.show()

# Kategorilerin Satış İle İlişkisi
import pandas as pd
import matplotlib.pyplot as plt
customer_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
customer_sales.plot(kind='bar', figsize=(10,6))
plt.title('Kategori-Satış')
plt.xlabel('Kategoriler')
plt.ylabel('Satış Miktarı')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
customer_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)[:20]
customer_sales.plot(kind='bar', figsize=(10,6))
plt.title('İlk 20 Alt Kategori')
plt.xlabel('Alt Kategoriler')
plt.ylabel('Satış Miktarı')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
customer_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)[:20]
customer_sales.plot(kind='bar', figsize=(10,6))
plt.title('İlk 20 Ürün')
plt.xlabel('Ürün Adı')
plt.ylabel('Satış Miktarı')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
customer_sales = df.groupby('Product ID')['Sales'].sum().sort_values(ascending=False)[:20]
customer_sales.plot(kind='bar', figsize=(10,6))
plt.title('İlk 20 Ürün')
plt.xlabel('Ürün kodu')
plt.ylabel('Satış Miktarı')
plt.show()

# Customer Name'i Aynı Olan Customer ID'si Farklı Olanların Tespiti

selected_df = df[['Customer Name', 'Customer ID']]
grouped = df.groupby('Customer Name')['Customer ID'].nunique()
result = grouped[grouped > 1]
print(result)

# Product Name'i Aynı Olan Product ID'si Farklı Olanların Tespiti

selected_df = df[['Product Name', 'Product ID']]
grouped = df.groupby('Product Name')['Product ID'].nunique()
result = grouped[grouped > 1]
print(result)

# en fazla satış yapılan 500 müşteri

data_top_customer = df.groupby('Customer Name').agg({'Sales': 'sum'}).reset_index()
data_top_customer.sort_values(by='Sales',ascending=False, inplace=True)
data_top_customer_top20 = data_top_customer.head(500)
x = data_top_customer_top20["Customer Name"]
y = data_top_customer_top20["Sales"]

plt.scatter(x, y)
plt.xlabel("Customer Name")
plt.ylabel("Sales")
plt.title("Top 500 Customers' Sales")
plt.show()
