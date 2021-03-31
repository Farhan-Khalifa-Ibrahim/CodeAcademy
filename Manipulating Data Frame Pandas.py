import pandas as pd
import numpy as np

ad_clicks = pd.read_csv('ad_clicks.csv')

#check the table
print(ad_clicks.head(5))

#get the most user visited
ad_clicks_source = ad_clicks.groupby(['utm_source']).user_id.count().reset_index()
print(ad_clicks_source)

#Make a new column
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(5))

#Grouping 2 columns
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

#pivoting
clicks_pivot = clicks_by_source.pivot(columns='is_click',index='utm_source',values='user_id')
print(clicks_pivot)

#new column
clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])
print(clicks_pivot)

#A/B Test Analysis
experimental_group = ad_clicks.groupby(['experimental_group']).user_id.count().reset_index()
print(experimental_group)

# number clicked by experimental_group
experimental_group_clicked = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().pivot(columns='is_click',index='experimental_group',values='user_id')
print(experimental_group_clicked)

#click by day
a_clicks = ad_clicks[ad_clicks['experimental_group']=='A']
b_clicks = ad_clicks[ad_clicks['experimental_group']=='B']
print(a_clicks)
print(b_clicks)


#percentage click per day
a_clicks_pivot = a_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(index='day',columns='is_click',values='user_id').reset_index()

a_clicks_pivot['click_percentage'] = a_clicks_pivot[True]/(a_clicks_pivot[True]+a_clicks_pivot[False])

print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(index='day',columns='is_click',values='user_id').reset_index()

b_clicks_pivot['click_percentage'] = b_clicks_pivot[True]/(b_clicks_pivot[True]+b_clicks_pivot[False])

print(a_clicks_pivot)
