import requests
import json
import pprint

#name = input("Please enter your name:")
#dc = input("How many decks would you like?")
name = "David"
dc = "6"
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=" + str(dc)

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

deckJson = response.json()

id = deckJson['deck_id']

print("The cards have been shuffled for you " + name + " your deck id is" + id )
#print(response.text)

url = "https://deckofcardsapi.com/api/deck/16ga7moqqbll/draw/?count=1"

payload={}
headers = {}

drawresponse = requests.request("GET", url, headers=headers, data=payload)

handJson = drawresponse.json()
cards = handJson['cards']
for items in cards[0:3]:
    print(code)
print(cards[0:3])
#for cards in handJson():
    #print(cards['code'])
#print(handJson['cards']['value'])
#deal = handJson['cards']




#print(deal['value'])
