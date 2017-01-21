from flask import Flask, request
import requests
import sys
import os
import json
from Credentials import *
from testmsghandler import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
        return request.args.get('hub.challenge', 200)
    else:
        return 'Error, wrong validation token'


@app.route('/', methods=['POST'])
def handle_messages():
    data = request.get_json()
    log(data)

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["message"]["text"]

                    """
                    nums = [int(s) for s in message_text.split() if s.isdigit()]
                    sum, i  = 0, 0
                    while i < nums.length:
                        sum += nums[i]
                        i += 1
                    """

                    #message_back = "How are you?"
                    #if message_text == "Hi":
                        #message_back = "Hello " + sender_id


                    #create another class that can handle how to send messages? 
                    """
                    nums = [int(s) for s in message_text.split() if s.isdigit()]
                    answer = 0
                    i = 0
                    while i < len(nums):
                        answer += nums[i]
                        i += 1
                    """
                    calculator = Handler(message_text)
                    answer = calculator.sum_from_text()
                    send_message(sender_id, answer) #sends back a message 

                if messaging_event.get("delivery"):
                    pass

                if messaging_event.get("optin"):
                    pass

                if messaging_event.get("postback"):
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):
    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
    log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
