# import Flask class from the flask module
from flask import Flask

# Create Flask object to run
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return "Hi, Welcome to Flask!!"

if __name__ == "__main__":

	print("**Starting Server...")
		
	# Run Server
	app.run()