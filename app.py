import hashlib
import hmac
import os

from dotenv import load_dotenv
from flask import request, Flask

load_dotenv()
app = Flask(__name__)


@app.route("/", methods=['POST'])
def add_hmac_signature():
    if request.method == "POST":
        add_sign = hmac_helper(request.get_data())
        return add_sign.create_hmac_signature()
    return "METHOD NOT ALLOWED", 405


class hmac_helper:

    def __init__(self, data):
        self.data = data
        self.secret_key = os.getenv("SHARED_SECRET_KEY").encode()
        self.signature = hmac.new(self.secret_key, self.data, hashlib.sha256).hexdigest()
        self.encoding = "utf-8"

    def create_hmac_signature(self):
        data = self.data.decode(self.encoding) + "&Signature=" + self.signature
        # return data,200
        return_data_type = "{" + data + "}"
        return return_data_type, 200


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
