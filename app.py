from flask import Flask, render_template, request
from dotenv import load_dotenv
import os


# --- 		New defense 		---
os.system("sh make_secret_key.sh")
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
FLAG = os.getenv('FLAG')
# ---------------------------------

print(FLAG)

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
           )


@app.route('/')
def index():
	return "Take flag"

@app.route('/get_flag')
def read():
	if request.args.get('secret_key'):
		if request.args.get('secret_key') == SECRET_KEY:
			return f"{FLAG}"
		else:
			return f"Invalid code!"
	else:
		return "You can't get flag!"

app.run(debug=True, host='0.0.0.0', port=5002)
