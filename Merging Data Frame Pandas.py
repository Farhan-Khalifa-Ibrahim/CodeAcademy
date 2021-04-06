# Merging two table

import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders,products,\
left_on = 'product_id',right_on='id',suffixes=['_orders','_products'])

print(orders_products)

# Mismatached merges

import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

print(orders)
print(products)

merged_df = pd.merge(orders,products)
print(merged_df)

'''
merge pandas function is a inner join sql if there is no how parameter
'''

# Outer merge

import codecademylib
import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_outer = pd.merge(store_a,store_b,how='outer')
print(store_a_b_outer)

'''
We can use df.fillna(0minplace=True) to fill NaN Value
'''

# Left or right merge

import codecademylib
import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_left = pd.merge(store_a,store_b,how='left')
print(store_a_b_left)

store_b_a_left = pd.merge(store_b,store_a,how='left')
print(store_b_a_left)

# Concatenate Data Frames

import codecademylib
import pandas as pd

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery,ice_cream])
print(menu)

# Combination of above methods

import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print(visits)
print(checkouts)

v_to_c = pd.merge(visits,checkouts)
print(v_to_c)

v_to_c['time'] = v_to_c.checkout_time - \
                 v_to_c.visit_time
print(v_to_c)

print(v_to_c.time.mean())