from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
	# Change the message to something unique
	return jsonify({"message": "Kali hates me! Student 16!"})

if __name__ == "__main__":
	pp.run(threaded=True, host= '0.0.0.0', port=3000)
