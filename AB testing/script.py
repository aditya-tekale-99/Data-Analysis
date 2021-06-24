import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(10))

utm_source_max = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print (utm_source_max)

ad_clicks['is_click']= ~ad_clicks.ad_click_timestamp.isnull()
  
print (ad_clicks)
	
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print (clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id')
print (clicks_pivot)

clicks_pivot['percent_clicked'] = \
	clicks_pivot[True] /\
  (clicks_pivot[True] + 
  clicks_pivot[False])
  
print (clicks_pivot)

count = ad_clicks.groupby('experimental_group').user_id.count()
print (count)

experimental = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

experimental_pivot = experimental.pivot(columns='is_click', index='experimental_group', values='user_id')
experimental_pivot['percent_clicked'] = \
	experimental_pivot[True] /\
  (experimental_pivot[True] + 
  experimental_pivot[False])
print (experimental_pivot)

a_clicks= ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks= ad_clicks[ad_clicks.experimental_group == 'B']

aclicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
bclicks= b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

aclicks_pivot = aclicks.pivot(columns='is_click',index='day',values='user_id')
aclicks_pivot['percent_clicked'] = \
	aclicks_pivot[True] /\
  (aclicks_pivot[True] + 
  aclicks_pivot[False])
print (aclicks_pivot)
bclicks_pivot = bclicks.pivot(columns='is_click',index='day',values='user_id')
bclicks_pivot['percent_clicked'] = \
	bclicks_pivot[True] /\
  (bclicks_pivot[True] + 
  bclicks_pivot[False])
print (bclicks_pivot)
