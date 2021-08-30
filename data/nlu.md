## intent:affirm
- yes
- yea
- sure
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks
- k
- y
- yea
- yes accept please
- great
- oh cool
## intent:deny
- no
- nope
- nah
- never
- n
- no need
- don't like that
- I don't think so
- great choice
- no thanks
- decline
- deny
- I decline
- no!
- don't
- I don't want

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hi
- hi
- hello

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine:Chinese) restaurants
- show me [chines](cuisine:Chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine:Mexican) place in the [centre](location)
- i am looking for an [Mexican](cuisine:Mexican) spot called olaolaolaolaolaola
- search for restaurants
- recommened restaurant
- [lesser than 300](budget) 
- Could you find me a restaurant to eat at [Ranchi](location)?
- recommed good restaurants for [asian fusion](cuisine:Chinese)
- [between 300 to 700](budget)
- show me restaurants in [Vizag](location)
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine:Chinese) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [Italian](cuisine:Italian)
- [Chinese](cuisine:Chinese)
- [North Indian](cuisine)
- [South Indian](cuisine)
- [Mexican](cuisine)
- [American](cuisine)
- [Lithuania](location)
- [more than 700](budget)
- Oh, sorry, in [Italy](location)
- [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine:Mexican)
- [central](location) [italian](cuisine:Italian) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:Chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine:Italian)
- please find me [Chinese](cuisine:Chinese) restaurant in [delhi](location)
- can you find me a [Chinese](cuisine:Chinese) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine:Italian) restaurants in [bangalore](location)
- [Valentina_Lyon4520@gmail.com](email)
- [Gwen_Roman7613@joiniaa.com](email)
- [Ruth_Vollans4025@qater.org](email)
## synonym:4
- four

## synonym:mumbai
- bombay

## synonym:New Delhi
- Delhi
- Dilli
- deli
## synonym:chennai
 - madras

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines
- asian

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:email
-  [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}