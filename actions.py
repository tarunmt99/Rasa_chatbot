from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from pandas.core.frame import DataFrame

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from send_email import sendmail
import pandas as pd
import json

ZomatoData = pd.read_csv('zomato.csv',encoding='latin1')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine,budget):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	TEMP =  TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']].sort_values(by=['Aggregate rating'], ascending=False)
	if budget=="more than 700":
		TEMP = TEMP.loc[lambda TEMP: TEMP['Average Cost for two'] > 700.0]

	if budget=="lesser than 300":
		TEMP = TEMP.loc[lambda TEMP: TEMP['Average Cost for two'] < 300.0]


	if budget=="between 300 to 700":
		TEMP = TEMP.loc[lambda TEMP: TEMP['Average Cost for two'] > 300.0].loc[lambda TEMP: TEMP['Average Cost for two'] < 700.0]

	return TEMP

def ValidateLocation(loc):
		if loc.lower() in (string.lower() for string in WeOperate):
			return True
		else:
			return False

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,budget=budget)
		response=""
		if results.shape[0] == 0:
			res_avail=False
			response= "no results"
		else:
			res_avail=True			
			for restaurant in results.iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found below top 5 restaurants \n {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc),SlotSet('restaurant_avail',res_avail)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		response = ""
		sendmail(MailID,response)
		return [SlotSet('mail_id',MailID)]

	

class ActionCheckLocation(Action):
	def name(self):
		return 'action_location_check'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		check_value = ValidateLocation(loc)
		print("----")
		print(check_value)
		return [SlotSet('location_check',check_value)]	

		