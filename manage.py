from flask import Flask
from flask import request

import json
from config import DevelopmentConfig

from handler import recived_message

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
#creando url para el
@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
	if request.method == 'GET':#verificando el token
		verify_token = request.args.get('hub.verify_token','')
		if verify_token == app.config['SECRET_KEY']:#validando que solo fb este intentando acceder
			return request.args.get('hub.challenge','')
		return 'Error while validating SECRET KEY'

	elif request.method == 'POST':
		payload = request.get_data()
		data = json.loads(payload)

		for page_entry in data['entry']:#descomponiendo el mensaje en formato json

			for message_event in page_entry['messaging']:

				if 'message' in message_event:
					recived_message(message_event, app.config['PAGE_ACCESS_TOKEN'])

		return "ok"

@app.route('/', methods = ['GET'])#por el moento los metodos que acepta es GET
def index():
	return 'hiii Botci, hii niña!'

if __name__ == '__main__':
	app.run(port = 8000)
