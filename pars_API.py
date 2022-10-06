import requests
import json


url = "https://hotels4.p.rapidapi.com/properties/v2/list"

payload = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"destination": {"regionId": "6054439"},
	"checkInDate": {
		"day": 10,
		"month": 10,
		"year": 2022
	},
	"checkOutDate": {
		"day": 15,
		"month": 10,
		"year": 2022
	},
	"rooms": [
		{
			"adults": 2,
			"children": [{"age": 5}, {"age": 7}]
		}
	],
	"resultsStartingIndex": 0,
	"resultsSize": 200,
	"sort": "PRICE_LOW_TO_HIGH",
	"filters": {"price": {
			"max": 150,
			"min": 100
		}}
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c6bd41c353msh6e62228fb43bea0p160630jsn3d480b1581c8",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

with open('hostel.json', 'w', encoding='utf-8') as file:
	json.dump(response.text, file, ensure_ascii=False, indent=4)



print(response.text)