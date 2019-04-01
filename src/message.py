import requests
import json


config = None
with open('config.json') as f:
	config = json.load(f)

def message(text, description):
	data = {
		"text": text + '\n' + '>>>\n' + description,
		"mrkdwn": True
	}
	response = requests.post(config.get("HOOK_URL"), json=data)
	print(response.text)