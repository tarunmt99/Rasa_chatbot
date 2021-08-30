from send_email import sendmail
import pandas as pd

ZomatoData = pd.read_csv('zomato.csv',encoding='latin1')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
Cuisine = "Chinese"
City = "Bangalore"
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
r = TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']].sort_values(by=['Aggregate rating'], ascending=False).loc[lambda TEMP: TEMP['Average Cost for two'] < 2000.0].loc[lambda TEMP: TEMP['Average Cost for two'] > 300.0]
#print(TEMP['Aggregate rating'].describe)
print(r)

sendmail("tarun.mt99@gmail.com",TEMP)