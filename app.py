import hashlib
import hmac
import os

from dotenv import load_dotenv
from flask import request, Flask
from helper import HMAC_Helper

load_dotenv()
app = Flask(__name__)


@app.route("/", methods=['POST'])
def add_hmac_signature():
    """
    POST Request: receive data from the user and add HMAC Signature
    :return: Signed user data
    """
    if request.method == "POST":
        data = request.get_data() #Fetch data from request body
        # Check if data exist and its not empty
        if not data:
            return "BAD REQUEST", 403 # Return 403 if data is empty
        add_sign = HMAC_Helper(data)
        return add_sign.create_hmac_signature() # Return signed data
    return "METHOD NOT ALLOWED", 405 # Return 405 if not Request is not POST

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
