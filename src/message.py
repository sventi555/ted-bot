import requests

def message(webhook, text, description):
	"""
	Sends a message to slack workspace determined by `webhook`.
	The message will be `text` followed by `description` in blockquotes.

	Parameters
	----------
	webhook : string
		The webhook url configured for the Slack workspace.
	text : string
		The primary text to send in the message.
	description : string
		The secondary text to send as a blockquote in the message.
	"""
	data = {
		"text": text + '\n' + '>>>\n' + description,
		"mrkdwn": True
	}
	response = requests.post(webhook, json=data)
	print('DEBUG: slack message status is "{}"'.format(response.text))
