import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))

visits_carts = pd.merge(visits,cart,how='left')
print(visits_carts)

print(len(visits_carts))
print("People not checkout",visits_carts['cart_time'].isnull().sum())

print("Percentage people not adding to cart",float(visits_carts['cart_time'].isnull().sum())/len(visits_carts)*100)

carts_checkouts = pd.merge(cart,checkout,how='left')
print("Percentage people adding to cart but not checkout",float(carts_checkouts['checkout_time'].isnull().sum())/len(carts_checkouts)*100)

all_data = visits\
          .merge(cart,how='left')\
          .merge(checkout,how='left')\
          .merge(purchase,how='left')
print(all_data)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())

#Percentage people checkout but didn't purchase
checkout_purchase = pd.merge(checkout,purchase,how='left')
print("number of people checkout but didn't purchase",len(checkout_purchase[checkout_purchase['purchase_time'].isnull()])/float(len(checkout_purchase))*100)
