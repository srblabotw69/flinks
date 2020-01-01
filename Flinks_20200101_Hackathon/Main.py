from flask import Flask, render_template
from flask import request, redirect, url_for

from requests import get, post
import json

DEBUG = True
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('start.html')


@app.route('/flinks', methods=['POST'])
def flinks():
    # POST request from start.html
    if request.method == 'POST':
        print('Incoming...')
        print(request.get_json())  # parse as JSON

        headers = {'Content-Type': 'application/json'}

        # parse data
        x = request.get_json()
        # convert links value into JSON:
        y = json.dumps(x["links"][0])
        # get links value from JSON:
        z = json.loads(y)
        links_example = z["example"]
        print(links_example)

        try:
            response = get(links_example).json()

            # print entire data
            print(response)

            # print selected data
            array_length = len(response)
            # print(array_length)
            for i in range(array_length):
                print(" ")
                print("==================================")
                print("Title: " + response["Accounts"][i]["Title"]),
                print("Balance: " + json.dumps(response["Accounts"][i]["Balance"])),
                print("Category: " + response["Accounts"][i]["Category"]),
                print("Type: " + response["Accounts"][i]["Type"]),
                print("Currency: " + response["Accounts"][i]["Currency"])

            print(" ")

        except Exception as e:
            print(e)

    return 'OKie', 200

    # # GET request
    # else:
    #     message = {'greeting':'Hello from Flask!'}
    #     return jsonify(message)  # serialize and use JSON headers


if __name__ == '__main__':
    app.run(debug=True)


# {'Links': [{'rel': 'AccountsDetail', 'href': '/GetAccountsDetail', 'example': None},
#            {'rel': 'AccountsSummary', 'href': '/GetAccountsSummary', 'example': None},
#            {'rel': 'Statements', 'href': '/GetStatements', 'example': None}],
#  'HttpStatusCode': 200,
#  'Login': {'Username': 'Greatday', 'IsScheduledRefresh': False, 'LastRefresh': '2019-10-04T09:08:07.8216522',
#            'Type': 'Personal', 'Id': 'a5c1923b-c61a-4783-eca4-08d74861abc3'},
#  'Institution': 'FlinksCapital', 'RequestId': '27ad4fb0-1441-41e4-82ce-54ef1f2896cc'}
