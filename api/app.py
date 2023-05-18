from flask import Flask, request, jsonify
from pymongo import MongoClient


connection_string = "mongodb+srv://dbgo:dbgo@cluster0.rvcfm.mongodb.net/?retryWrites=true&w=majority"

app = Flask(__name__)
app.config['MONGO_URI'] = connection_string
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.get_database('flask')
coll = db.summernote
# client = MongoClient(connection_string)
# db = client.flask
# collection = db.summernote
# print(collection)


data = coll.find().limit(1).sort([('$natural', -1)])
print(data[0]['name'])


@ app.route('/api/get', methods=['GET'])
def get_data():

    response = jsonify(
        {'response': 'ok', 'data': data[0]['name']})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200


@ app.route('/api/email', methods=['POST'])
def send_email():
    data = request.get_json()

    # Extract data from the request
    html_content = data.get(
        'html_content'
    )
    coll.insert_one({'name': html_content})

    # print(html_content)

    # Code to send the email using your preferred email service provider

    # Return a response
    response = {'message': 'Email sent successfully', 'data': html_content}
    return jsonify(response), 200


if __name__ == '__main__':
    app.run()
