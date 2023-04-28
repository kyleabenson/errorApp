from flask import Flask, request
import random
import os

app = Flask(__name__)

@app.route("/hello")
def hello():
    # Generate a random number between 0 and 100
    random_number = random.randint(0, 100)
    print("Random number is " + str(random_number))
    # If the random number is less than 90, return a 200 status code
    if random_number < 90:
        return "Hello World!", 200

    # Otherwise, return a 500 status code
    else:
        return "We've got an error here.", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))