## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}       
    - slot{"budget": "between 300 to 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
* restaurant_search{"email": "test@msn.in"}    
    - slot{"email": "test@msn.in"}
    - action_send_mail
* goodbye    
    - utter_goodbye
    - export




## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}       
    - slot{"budget": "between 300 to 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affrim    
    - utter_ask_email
* deny  
    - utter_goodbye
    - export


## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}       
    - slot{"budget": "between 300 to 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* deny  
    - utter_goodbye
    - export


## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}    
    - slot{"budget": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
* restaurant_search{"email": "testgas3534@rez.df"}    
    - slot{"email": "testgas3534@rez.df"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}   
    - slot{"budget": "more than 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
* restaurant_search{"email": "testgas3534@rez.df"}
    - slot{"email": "testgas3534@rez.df"}
    - action_send_mail


## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - action_location_check
    - slot{"location_check": false}
    - utter_donotoperate   
* goodbye
    - utter_goodbye


## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - action_location_check
    - slot{"location_check": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}   
    - slot{"location": "Ranchi"}
    - utter_ask_budget
* restaurant_search{"budget": "lesser than 300"}   
    - slot{"budget": "lesser than 300"}
    - slot{"location": "Ranchi"}
    - slot{"cuisine": "Mexican"}  
    - action_search_restaurants
    - slot{"restaurant_avail":false}
* goodbye
    - utter_goodbye 

## complete path 5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chandini Chowk"}
    - slot{"location": "Chandini Chowk"}
    - action_location_check
    - slot{"location_check": false} 
    - utter_donotoperate
* goodbye
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_location_check
    - slot{"location_check": true}      
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"} 
    - slot{"location": "Patna"}
    - utter_ask_budget
* restaurant_search{"budget": "lesser than 300"}    
    - slot{"budget": "lesser than 300"}
    - slot{"location": "Patna"}
    - slot{"cuisine": "Italian"} 
    - action_search_restaurants
    - slot{"location": "Patna"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
* restaurant_search{"email":"Gabriel_Everett1415@brety.org"}    
    - slot{"email":"Gabriel_Everett1415@brety.org"}
    - action_send_mail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_location_check
    - slot{"location_check": true}      
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"} 
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": "lesser than 300"}    
    - slot{"budget": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}   
    - slot{"restaurant_avail":false}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Moradabad"}
    - slot{"location": "Moradabad"}
    - action_location_check
    - slot{"location_check": false}      
    - utter_donotoperate




## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true} 
* restaurant_search{"cuisine": "chinese", "location": "delhi"}    
    - utter_ask_budget
 * restaurant_search{"budget": "lesser than 300"}   
    - slot{"budget": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
* restaurant_search{"email":"Gverett1415@gmail.com"}    
    - slot{"email":"Gverett1415@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Begusarai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Begusarai"}
    - action_location_check
    - slot{"location_check": false}  
    - utter_donotoperate
* affirm
    - utter_goodbye
     

## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}       
    - slot{"budget": "between 300 to 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affrim    
    - utter_ask_email
* restaurant_search{"email": "testgas3534@rez"} 
    - slot{"email": "testgas3534@rez"}
* deny  
    - utter_goodbye
    - export


## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}       
    - slot{"budget": "between 300 to 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* deny  
    - utter_goodbye
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_location_check
    - slot{"location_check": true}      
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"} 
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": "lesser than 300"}    
    - slot{"budget": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"restaurant_avail":false}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Moradabad"}
    - slot{"location": "Moradabad"}
    - action_location_check
    - slot{"location_check": false}      
    - utter_donotoperate




## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true} 
* restaurant_search{"cuisine": "chinese", "location": "delhi"}    
    - utter_ask_budget
* restaurant_search{"budget": "lesser than 300"}   
    - slot{"budget": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
* restaurant_search{"email":"Gverett1415@gmail.com"}    
    - slot{"email":"Gverett1415@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Begusarai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Begusarai"}
    - action_location_check
    - slot{"location_check": false}  
    - utter_donotoperate
* affirm
    - utter_goodbye
     

## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}       
    - slot{"budget": "between 300 to 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affrim    
    - utter_ask_email
* restaurant_search{"email":"testgas3534@rez"}    
    - slot{"email": "testgas3534@rez"}
* deny  
    - utter_goodbye
    - export


## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Madras"}
    - slot{"location": "Madras"}
    - action_location_check
    - slot{"location_check": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}       
    - slot{"budget": "between 300 to 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":false}


## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}    
    - slot{"budget": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email

    - slot{"email": "testgas3534@rez.df"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}   
    - slot{"budget": "more than 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
    - slot{"email": "asdsa@rez.df"}
    - action_send_mail
* goodbye    
    - utter_goodbye


## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"location_check": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}   
    - slot{"budget": "more than 700"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"restaurant_avail":false}


## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_location_check
    - slot{"location_check": true}
    - utter_ask_budget 
* restaurant_search{"budget": "more than 700"}    
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"budget": "more than 700"}   
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
* restaurant_search{"email":"Owen21@irrepsy.com"}
    - slot{"email":"Owen21@irrepsy.com"}
    - action_send_mail





## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Faridabad"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Faridabad"}
    - action_location_check
    - slot{"location_check": true}    
    - utter_ask_budget 
* restaurant_search{"budget": "more than 700"}   
    - slot{"cuisine": "italian"}
    - slot{"location": "Faridabad"}
    - slot{"budget": "more than 700"}   
    - action_search_restaurants
    - slot{"cuisine": "italian"}
    - slot{"location": "Faridabad"}
    - slot{"budget": "more than 700"} 
     slot{"restaurant_avail":true}
    - utter_sendemail
* affirm
    - utter_ask_email
* restaurant_search{"email":"Owe43534n21@irresy.biz"}       
    - slot{"email":"Owe43534n21@irresy.biz"}
    - action_send_mail 

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_location_check
    - slot{"location_check": true}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}     
    - slot{"budget": "between 300 to 700"} 
    - slot{"location": "delhi"}  
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_avail":true}
    - utter_sendemail
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Mexico"}
    - slot{"location": "Mexico"}
    - slot{"cuisine": "chinese"}
    - action_location_check
    - slot{"location_check": false}   
    - utter_donotoperate
* affirm
    - utter_goodbye