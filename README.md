# HMAC Signature 

## SETUP

* Rename `.env.example` to `.env`
* Replace or edit `.env` file and fill in the `SHARED_SECRET_KEY`. Do not add quotes `""` eg: `SHARED_SECRET_KEY=ThWmZq4t7w!z%C*F)J@NcRfUjXn2r5u8`
* Create a virtual venv and activate it
* run `$ pip install -r requirements.txt`

## Run Unit Test

To run included unit test, run: 

```shell script

$ python -m unittest tests.test_app.AppTests
```


## Test by posting data

* Run Flask server: `$ flask run`
* Once your flask server is running, run and command below:

```shell script
$ curl --data "id=MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz" http://localhost:5000

{id=MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz&Signature=12259b08d69bb116033f16ba9627ef11b97456fdbe8ee4c70ecdf19a69e9c0b5}
```
