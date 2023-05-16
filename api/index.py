from flask import Flask, request, jsonify

app = Flask(__name__)

html_content = ""


@app.route('/api/get', methods=['GET'])
def get_data():
    global html_content
    response = {'message': 'Date sent successfully', 'data': html_content}
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(response), 200


@app.route('/api/email', methods=['POST'])
def send_email():
    data = request.get_json()

    # Extract data from the request
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')
    html_content = data.get(
        'html_content'
    )

    print(html_content)

    # Code to send the email using your preferred email service provider

    # Return a response
    response = {'message': 'Email sent successfully', 'data': html_content}
    return jsonify(response), 200


if __name__ == '__main__':
    app.run()
