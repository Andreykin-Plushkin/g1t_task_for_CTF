from flask import Flask, render_template, request

@app.route('/')
def index():
	return "Take flag"

@app.route('/get_flag')
def read():
	if request.args.get('secret_key'):
		if request.args.get('secret_key') == "32f297":
			return "CTF{LEAK_CODE_1}"
	else:
		return "You can't get flag!"
