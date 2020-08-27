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
    if request.method != "POST":
        return "METHOD NOT ALLOWED", 405  # Return 405 if not Request is not POST
    data = request.get_data()  # Fetch data from request body
    # Check if data exist and its not empty
    if not data:
        return "BAD REQUEST", 403  # Return 403 if data is empty
    add_sign = HMAC_Helper(data)
    return add_sign.create_hmac_signature(), 200 # Return signed data


@app.route("/validate", methods=['POST'])
def validate_hmac_signature():
    """
    POST Request: receive data from the user and verify HMAC Signature
    :return: Signed user data
    """
    if request.method != "POST":
        return "METHOD NOT ALLOWED", 405  # Return 405 if not Request is not POST
    data = request.get_data()  # Fetch data from request body
    raw_data = data.decode("utf-8")
    # Check if data exist and its not empty
    if not data or "&Signature=" not in raw_data:
        return "Cannot process request, BAD REQUEST", 400    # Return 403 if data is empty
    cleaned_data = raw_data.split("&Signature=")
    add_sign = HMAC_Helper(cleaned_data[0].encode())
    verified = add_sign.verify_hmac_signature(cleaned_data[1])
    return "Verified", 200 if verified else "Not Verified", 403 # Return Verified data


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
