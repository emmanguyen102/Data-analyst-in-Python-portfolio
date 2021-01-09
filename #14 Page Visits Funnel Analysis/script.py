##########################################################
# The funnel is going to describe the following process: #
#  1. A user visits CoolTShirts.com                      #
#  2. A user adds a t-shirt to their cart                #
#  3. A user clicks "checkout"                           #
#  4. A user actually purchases a t-shirt                #
##########################################################


import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# Explore data sets
print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))


# Merge visits and cart data set to the left, meaning that all information of 
# visits data set remains the same with modification only to cart data set

visits_cart = pd.merge(visits, cart, how="left")
visits_cart_num = len(visits_cart)
nulla = visits_cart[visits_cart.cart_time.isnull()]

# percent of users who visited Cool T-shirts Inc. ended up not placing a t-shirt in their cart
print(float(len(nulla))/visits_cart_num*100)


# Merge cart and checkout data set

cart_checkout = pd.merge(cart, checkout, how="left")
cart_checkout_len = len(cart_checkout)

null_checkout_len =len(cart_checkout[cart_checkout.checkout_time.isnull()])

# percentage of not checking out but putting orders into carts
print(float(null_checkout_len)/cart_checkout_len*100)

all_data = visits.merge(cart,how="left")\
                 .merge(checkout, how="left")\
                 .merge(purchase, how ="left")

# percentage of checking out but not purchasing
checkout_purchase = pd.merge(checkout, purchase, how="left")
print(float(len(checkout_purchase[checkout_purchase.purchase_time.isnull()]))/len(checkout_purchase)*100)

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase)

# mean time period from visiting the website till purchasing items
print(all_data.time_to_purchase.mean())
